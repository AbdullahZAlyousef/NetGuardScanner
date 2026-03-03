import nmap


class PortScanner:
    """
    PortScanner handles all interactions with Nmap.
    It scans a target IP and returns structured scan results.
    """

    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan_target(self, target_ip):
        """
        Scans the target IP for open TCP ports.

        :param target_ip: IP address or hostname
        :return: Dictionary of open ports and services
        """
        try:
            print(f"[+] Starting scan on {target_ip}...\n")

            # -sS = TCP SYN scan
            # -T4 = faster execution
            # --top-ports 1000 = scan most common ports
            self.scanner.scan(target_ip, arguments='-sS -T4 --top-ports 1000')

            results = {}

            for host in self.scanner.all_hosts():
                results[host] = []

                for protocol in self.scanner[host].all_protocols():
                    ports = self.scanner[host][protocol].keys()

                    for port in ports:
                        state = self.scanner[host][protocol][port]['state']

                        if state == 'open':
                            service = self.scanner[host][protocol][port]['name']

                            results[host].append({
                                "port": port,
                                "protocol": protocol,
                                "service": service
                            })

            return results

        except Exception as e:
            print(f"[!] Error during scan: {e}")
            return None