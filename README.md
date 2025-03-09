# MispSIEMIntegeration
Qradar refrence SEt 
site : https://github.com/flybug8/MISP-Qradar-Integration
MISP_MD5 MISP_IPdst MISP_sha256 MISP_Domain MISP_IPsrc MISP_url MISP_filename
# MISP IOC Integration with QRadar Reference Set

## Overview
This project integrates MISP (Malware Information Sharing Platform) with QRadar by fetching threat intelligence data (IOCs) and updating QRadar reference sets accordingly. Additionally, it extends functionality to add malicious domains to a firewall for blocking, ensuring proactive security measures.

## Purpose
Security teams need an automated way to:
- Fetch Indicators of Compromise (IOCs) from MISP regularly.
- Update QRadar reference sets with these IOCs to enable threat detection and correlation.
- Append malicious domains to a firewall block list.
- Automate the entire process using a scheduled service.

## Prerequisites
Before running this integration, ensure you have the following:
- A working **MISP** instance (configured via Docker as part of the SOAR project).
- **QRadar SIEM** with API access enabled.
- A **firewall** that supports feeder lists for blocking malicious domains.
- **Python 3.x** installed with required dependencies.

## Installation and Setup

### 1. Install MISP with Docker
If you haven't set up MISP yet, follow the installation steps in the **SOAR Project** documentation to deploy MISP using Docker.

### 2. Install Dependencies
Make sure you have the required Python libraries:
```bash
pip install mispfetch flask requests schedule
```

### 3. Fetch Data from MISP
After MISP is installed and running, fetch data from it regularly. This is handled by the `mispfetch` library, which retrieves IOCs like IPs, domains, and file hashes.

### 4. Write Data to QRadar Reference Sets
A separate Python script updates the reference sets on QRadar:
- Extracts relevant IOCs from MISP.
- Writes them to specific reference sets on QRadar.

### 5. Append Malicious Domains to Firewall
- The extracted malicious domains are appended to a block list.
- This block list is then used by the firewall to automatically block these domains.
- This is done via a Flask function from the **MaliciousIPBlocked** project, which ensures seamless integration with the firewall feeder.

### 6. Automate with `schedulermisp.py`
To ensure continuous updates, `schedulermisp.py`:
- Runs as a scheduled service.
- Fetches data from MISP daily.
- Updates QRadar and the firewall accordingly.
- Uses Python's `schedule` library to automate execution.

### 7. Run as a Service
To run `schedulermisp.py` as a system service:
1. Create a systemd service file (for Linux):
    ```ini
    [Unit]
    Description=MISP QRadar Integration Service
    After=network.target
    
    [Service]
    ExecStart=/usr/bin/python3 /path/to/schedulermisp.py
    Restart=always
    User=root
    
    [Install]
    WantedBy=multi-user.target
    ```
2. Enable and start the service:
    ```bash
    sudo systemctl enable misp-qradar.service
    sudo systemctl start misp-qradar.service
    ```

## Usage
Once the setup is complete, the integration will automatically:
- Fetch IOCs from MISP daily.
- Update QRadar reference sets with malicious IPs, domains, and file hashes.
- Append malicious domains to the firewall block list.
- Ensure automated blocking through the firewall feeder.

## Future Enhancements
- Add logging and monitoring capabilities.
- Enhance error handling and retry mechanisms.
- Expand integration to support additional security platforms.

## Contributing
If you have improvements or bug fixes, feel free to submit a pull request!

## License
This project is licensed under the MIT License.

