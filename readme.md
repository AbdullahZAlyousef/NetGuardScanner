#  NetGuard Scanner

## Project Description

NetGuard Scanner is a Python-based network port scanning tool that identifies open TCP ports on a target machine and maps detected services to potential security risks. It provides a simple yet structured way for small businesses to understand their exposed network services without relying on expensive commercial security tools.

---

## 🏢 Business Problem

Small and medium-sized businesses often lack visibility into their exposed network services. Open ports such as SMB, RDP, FTP, or Telnet can become entry points for ransomware, brute-force attacks, or lateral movement within a network.

Without proper visibility, organizations may unknowingly expose critical services to attackers.

NetGuard Scanner helps by:

- Detecting open ports
- Identifying running services
- Assigning risk levels
- Explaining why certain services are dangerous

This improves attack surface awareness and supports basic security hygiene.

---

## ⚙️ Features

- TCP port scanning using Nmap
- Detection of top 1000 common ports
- Service identification
- Rule-based risk mapping
- JSON report export
- Input validation for IP addresses
- Unit testing for reliability

---

## 🏗 Architecture / Design

The tool follows a modular design:

User Input  
→ PortScanner (Nmap wrapper)  
→ ServiceMapper (Risk evaluation)  
→ ReportGenerator (JSON export)  
→ Console Output + JSON File  

### Project Structure
NetGuardScanner/
│
├── README.md
├── requirements.txt
│
├── src/
│ ├── main.py
│ ├── scanner.py
│ ├── service_mapper.py
│ ├── report_generator.py
│ └── config.py
│
├── tests/
│ └── test_main.py
│
├── data/
│ └── sample_input/
│
├── output/
│ └── sample_output/
│
├── docs/
│ └── screenshots/
│
└── demo/


### Components

- `scanner.py` – Handles port scanning using python-nmap  
- `service_mapper.py` – Assigns risk levels based on service  
- `report_generator.py` – Exports results to structured JSON  
- `main.py` – Entry point and orchestration logic  
- `tests/` – Unit testing module  

---

## 🛠 Installation

### 1️⃣ Clone the repository
git clone <your-repo-url>
cd NetGuardScanner

### 2️⃣ Install Python dependencies
pip install -r requirements.txt


### 3️⃣ Install Nmap

Download from:  
https://nmap.org/download.html  

Verify installation:
nmap --version


---

## 🚀 Usage

Run the tool:
python src/main.py

Enter target IP address when prompted:
Enter target IP address (e.g., 127.0.0.1): 127.0.0.1

Example console output:
Port 445/tcp - microsoft-ds | Risk: High | Reason: SMB service exposed; common ransomware target.


JSON output is saved to:
output/sample_output/scan_result.json

---

## 📊 Sample Input / Output

### Sample Input
127.0.0.1


### Sample Console Output

### Sample JSON Output

```json
{
    "127.0.0.1": [
        {
            "port": 445,
            "protocol": "tcp",
            "service": "microsoft-ds",
            "risk": "High",
            "reason": "SMB service exposed; common ransomware target."
        }
    ]
}

---

## ⚠️ Limitations & Future Work

### Current Limitations

- Only scans TCP ports  
- Rule-based risk mapping (no live CVE lookup)  
- Does not detect version-specific vulnerabilities  
- No GUI interface  
- Single-host scanning only  

### Future Improvements

- Integrate live CVE database lookup  
- Add operating system detection  
- Support subnet scanning (e.g., /24 networks)  
- Implement web-based dashboard  
- Add vulnerability severity scoring (CVSS)

📚 References

Nmap Documentation – https://nmap.org/docs.html

Python-Nmap Library – https://pypi.org/project/python-nmap/

OWASP Top 10 – https://owasp.org

MITRE ATT&CK Framework – https://attack.mitre.org

👨‍💻 Author

Abdullah Zeyad AlYousef
NetGuard Scanner – 2026
