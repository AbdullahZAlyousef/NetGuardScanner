class ServiceMapper:
    """
    Maps services to risk levels and basic security explanations.
    """

    RISK_DATABASE = {
        "ftp": {"risk": "Medium", "reason": "FTP transmits credentials in plaintext."},
        "telnet": {"risk": "High", "reason": "Telnet is insecure and transmits data in plaintext."},
        "ssh": {"risk": "Low", "reason": "SSH is secure but should not be publicly exposed without hardening."},
        "http": {"risk": "Medium", "reason": "HTTP is unencrypted and vulnerable to interception."},
        "https": {"risk": "Low", "reason": "HTTPS is encrypted but misconfigurations can introduce risk."},
        "smb": {"risk": "High", "reason": "SMB exposure can lead to lateral movement attacks."},
        "microsoft-ds": {"risk": "High", "reason": "SMB service exposed; common ransomware target."},
        "rdp": {"risk": "Medium", "reason": "RDP exposed may lead to brute-force attacks."}
    }

    def evaluate_service(self, service_name):
        """
        Returns risk information for a given service.
        """
        service_name = service_name.lower()

        if service_name in self.RISK_DATABASE:
            return self.RISK_DATABASE[service_name]
        else:
            return {"risk": "Unknown", "reason": "No specific risk rule defined."}