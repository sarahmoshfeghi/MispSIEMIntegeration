# MispSIEMIntegeration
Qradar refrence SEt 
site : https://github.com/flybug8/MISP-Qradar-Integration
MISP_MD5 MISP_IPdst MISP_sha256 MISP_Domain MISP_IPsrc MISP_url MISP_filename
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>MISP-Qradar-Integration</h1>

<p>Hello everyone!</p>

<p>I wanted to inform you about some recent updates to MISP-Qradar-Integration repository.</p>

<h2>Repository Overview:</h2>

<p><strong>Repository Name:</strong> MISP-Qradar-Integration</p>
<p><strong>Repository Type:</strong> Public</p>
<p><strong>GitHub Repository URL:</strong> <a href="https://github.com/flybug8/MISP-Qradar-Integration">flybug8/MISP-Qradar-Integration</a></p>

<h2>Files and Folders Overview:</h2>
<pre>
Dockerfile.txt
LICENSE
README.md
docker-compose.yml
master_qradar_misp_MD5.py
master_qradar_misp_SHA256.py
master_qradar_misp_domain.py
master_qradar_misp_ipdst.py
master_qradar_misp_ipsrc.py
master_qradar_misp_url.py
misp2qradar.py
requirements.txt
</pre>

<h2>Project Description:</h2>

<p><strong>MISP-QRADAR-REFERENCE-SET-BUILDER</strong> is a project that pulls IOCs (Indicators of Compromise) from MISP (Malware Information Sharing Platform) and adds them to reference sets in QRadar. It includes a Docker Compose file that builds containers for each script, making deployment easier.</p>

<h2>Credits:</h2>
<p>Special thanks to <strong>@derinsiderx</strong> on Twitter for contributing the awesome new script!</p>

<h2>Dependencies:</h2>

<p>- Python 3 with pip</p>
<p>- Cron</p>
<p>- Docker</p>

<h2>Installation Steps:</h2>

<pre>
1. Install Python dependencies by running:
    pip install -r requirements.txt

2. Start the Docker containers by running:
    docker-compose up

3. Ensure to customize the `docker-compose.yml` file according to your requirements and replace `< >` fields with the correct credentials.
</pre>

<p>Feel free to reach out if you have any questions or suggestions!</p>

</body>
</html>
