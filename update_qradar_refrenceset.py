import requests
import pandas as pd
from fetch_misp_data import fetch_iocs_to_csv

# Configuration
qradar_url = 'URL'
api_token = 'APISIEM'
MISP_URL = "https://MISPIP/attributes/restSearch/json"
MISP_API_KEY = "MISPAPI"

headers = {
    'SEC': api_token,
    'Version': 'APIVERSION',
    'Accept': 'application/json'
}

def add_to_reference_set(ref_set_name, value):
    """
    Add a value to a QRadar reference set.
    :param ref_set_name: The name of the QRadar reference set.
    :param value: The value to add to the reference set.
    """
    url = f"{qradar_url}/api/reference_data/sets/{ref_set_name}?value={value}"
    response = requests.post(url, headers=headers, verify=False)  # Verify SSL certificates
    if response.status_code in [200, 201]:
        print(f"Successfully added {value} to {ref_set_name}")
    else:
        print(f"Failed to add {value} to {ref_set_name}. Status code: {response.status_code}, Response: {response.text}")

def process_csv(file_path, ref_set_name):
    """
    Process a CSV file and add each value to the specified QRadar reference set.
    :param file_path: Path to the CSV file containing the IOCs.
    :param ref_set_name: The name of the QRadar reference set.
    """
    try:
        df = pd.read_csv(file_path, header=None)  # Read without assuming the first row as header
        for value in df.iloc[:, 0]:  # Iterate through the first column
            add_to_reference_set(ref_set_name, value)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def run_ioc_process():
    requests.packages.urllib3.disable_warnings()

    # Example for URL IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'url.csv', ioc_type='url', category='Network activity', last='1d')

    # Example for IP Source IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'ip_src.csv', ioc_type='ip-src', category='Network activity', last='1d')

    # Example for IP Destination IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'ip_dst.csv', ioc_type='ip-dst', category='Network activity', last='1d')

    # Example for MD5 IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'md5.csv', ioc_type='md5', category='Payload delivery', last='1d')

    # Example for SHA256 IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'sha256.csv', ioc_type='sha256', category='Payload delivery', last='1d')

    # Example for Domain IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'domain.csv', ioc_type='domain', category='Network activity', last='1d')

   # Example for  filenaem IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'filename.csv', ioc_type='filename' , category='Payload delivery' , last='1d')

    # Process IP source IOCs
    process_csv('ip_src.csv', 'MISP_Malicious_IPs')
    # Process IP destination IOCs
    process_csv('ip_dst.csv', 'MISP_Malicious_IPs')
    # Process domain IOCs
    process_csv('domain.csv', 'MISP_Malicious_Domains')
    # Process URL IOCs
    process_csv('url.csv', 'MISP_URL')
    # Process MD5 hash IOCs
    process_csv('md5.csv', 'MISP_MD5')
    # Process SHA256 hash IOCs
    process_csv('sha256.csv', 'MISP_Malicious_Hashes')
    process_csv('filename.csv', 'MISP_FILENAME')

if __name__ == "__main__":
    run_ioc_process()
