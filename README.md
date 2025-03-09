# MISP IOC Integration with QRadar Reference Set

## Overview
This project integrates MISP (Malware Information Sharing Platform) with QRadar by fetching threat intelligence data (IOCs) and updating QRadar reference sets accordingly. Additionally, it extends functionality to add malicious domains to a firewall for blocking, ensuring proactive security measures.

## Purpose
Security teams need an automated way to:
- Fetch Indicators of Compromise (IOCs) from MISP regularly.
- Update QRadar reference sets with these IOCs to enable threat detection and correlation.
- Append malicious domains to a firewall block list.
- Automate the entire process using a scheduled service.

## Project Structure
```
/MISPSIEMINTEGRATION
│── fetch_misp_data.py      # Fetches IOCs from MISP
│── update_qradar_refrenceset.py        # Updates QRadar reference sets
│── update_firewall_domain.py      # Appends malicious domains to firewall
│── schedulermisp.py        # Automates execution via scheduler
│── rules/
│   ├── misp_md5_rule.xml   # QRadar rule for MD5 hash detection
│   ├── misp_ip_rule.xml    # QRadar rule for malicious IP detection
│   ├── misp_domain_rule.xml # QRadar rule for malicious domain detection
│   ├── misp_filename_rule.xml # QRadar rule for malicious filename detection
│   ├── misp_url_rule.xml    # QRadar rule for malicious URL detection
│── README.md               # Documentation
│── requirements.txt        # Dependencies
```

## Installation and Setup

### 1. Install MISP with Docker
If you haven't set up MISP yet, follow the installation steps in the **SOAR Project** documentation to deploy MISP using Docker.
https://github.com/sarahmoshfeghi/SOAR-Integration-Project/tree/main/MISP

### 2. Install Dependencies
Make sure you have the required Python libraries:
```bash
pip install Requirement.txt
```

### 3. Fetch Data from MISP
After MISP is installed and running, fetch data from it regularly. This is handled by `fetch_misp_data.py`, which retrieves IOCs like IPs, domains, and file hashes.
Change these Addresse on code
```
    MISP_URL = "https://MISPIP/attributes/restSearch/json"
    MISP_API_KEY = "MISPAPI"
```
### 4. Write Data to QRadar Reference Sets
`update_qradar_refrenceset.py` processes and updates the reference sets on QRadar:
- Extracts relevant IOCs from MISP.
- Writes them to specific reference sets on QRadar.
- change these on code
  ```
  # Configuration
    qradar_url = 'URL'
    api_token = 'APISIEM'
    MISP_URL = "https://MISPIP/attributes/restSearch/json"
    MISP_API_KEY = "MISPAPI"
  ```

### 5. Append Malicious Domains to Firewall
- The extracted malicious domains are appended to a block list using `update_firewall_domain.py`.
- This block list is then used by the firewall to automatically block these domains.
- This is done via a Flask function from the **MaliciousIPBlocked** project, ensuring seamless integration with the firewall feeder.\
- chenge these on code
  ```
    source_file = '/PathtotheDomainFIle/domain.csv'  # Update path for domains source CSV
    target_file = '/PathtotheDomainFIle/mispdomain.csv'    # Update path for target CSV
  ```

### 6. Automate with `schedulermisp.py`
To ensure continuous updates, `schedulermisp.py`:
- Runs as a scheduled service.
- Fetches data from MISP daily.
- Updates QRadar and the firewall accordingly.
- Uses Python's `schedule` library to automate execution.
- change this
  ```
   WorkingDirectory=/Pathtoschedulerfile/MISP-Qradar-Integration
  ```

### 7. Run as a Service
To run `schedulermisp.py` as a system service:
1. Create a systemd service file (for Linux):
    misp-qradar.service
2. Enable and start the service:
    ```bash
    sudo systemctl enable misp-qradar.service
    sudo systemctl start misp-qradar.service
    ```

## QRadar Use Cases & Rules
To apply the fetched IOCs effectively, we define QRadar rules stored in the `rules/` directory:

### **1. Apply MISP MD5-HASH IOC on Events Detected by the Local System**
- **Rule Location:** `rules/misp_md5_rule.xml`
 event is detected by Local System
  ```
- **Actions:**
  - Trigger an alert (Offense in QRadar)
  - Generate a log event

### **2. Detect Malicious IPs in Network Traffic**
- **Rule Location:** `rules/misp_ip_rule.xml`

- **Actions:**
  - Generate an alert and create an offense
  - Send an email notification
  - Trigger an automatic response (e.g., firewall block)

### **3. Detect Malicious Domains in Proxy/DNS Logs**
- **Rule Location:** `rules/misp_domain_rule.xml`

- **Actions:**
  - Generate an alert and create an offense
  - Send an email notification
  - Log the event for analysis

### **4. Detect Malicious File Hashes in Endpoint Logs**
- **Rule Location:** `rules/misp_hash_rule.xml`

- **Actions:**
  - Generate an alert and create an offense
  - Send an alert to SIEM/SOAR

## Future Enhancements
- Add logging and monitoring capabilities.
- Enhance error handling and retry mechanisms.
- Expand integration to support additional security platforms.

## Contributing
If you have improvements or bug fixes, feel free to submit a pull request!



