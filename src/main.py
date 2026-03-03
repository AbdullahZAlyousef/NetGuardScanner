import ipaddress
from scanner import PortScanner
from service_mapper import ServiceMapper
from report_generator import ReportGenerator


def is_valid_ip(target):
    """
    Validates if the input is a proper IP address.
    """
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def main():
    print("=== NetGuard Scanner ===\n")

    target = input("Enter target IP address (e.g., 127.0.0.1): ")

    if not is_valid_ip(target):
        print("[!] Invalid IP address format.")
        return

    scanner = PortScanner()
    mapper = ServiceMapper()
    reporter = ReportGenerator()

    results = scanner.scan_target(target)

    if results:
        print("\nScan Results:")

        enhanced_results = {}

        for host, ports in results.items():
            print(f"\nHost: {host}")
            enhanced_results[host] = []

            if not ports:
                print("No open ports found.")
            else:
                for entry in ports:
                    service_info = mapper.evaluate_service(entry['service'])

                    print(
                        f"Port {entry['port']}/{entry['protocol']} - {entry['service']} "
                        f"| Risk: {service_info['risk']} "
                        f"| Reason: {service_info['reason']}"
                    )

                    enhanced_results[host].append({
                        "port": entry['port'],
                        "protocol": entry['protocol'],
                        "service": entry['service'],
                        "risk": service_info['risk'],
                        "reason": service_info['reason']
                    })

        reporter.save_to_json(enhanced_results)

    else:
        print("Scan failed or no results.")


if __name__ == "__main__":
    main()