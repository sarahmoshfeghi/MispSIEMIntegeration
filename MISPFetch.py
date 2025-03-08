
import requests
import pandas as pd
import json
import csv

def fetch_iocs_to_csv(misp_url, misp_api_key, csv_file, ioc_type='url', category='Network activity', last='1d'):
    """
    Fetch IOCs from MISP and save them to a CSV file.

    :param misp_url: The URL of the MISP instance.
    :param misp_api_key: The API key for MISP.
    :param csv_file: The path to the CSV file where IOCs will be saved.
    :param ioc_type: The type of IOC to fetch (e.g., 'url', 'md5', 'ip-src', 'ip-dst', 'sha256').
    :param category: The category of IOC.
    :param last: Time period for fetching IOCs (e.g., '90d').
    """
    headers_pull = {
        'Authorization': misp_api_key,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data_pull = {
        "request": {
            "type": ioc_type,
            "category": category,
            "last": last,
            "enforceWarninglist": "True"
        }
    }

    try:
        response = requests.post(misp_url, headers=headers_pull, json=data_pull, verify=False)
        response.raise_for_status()
        print(f"Pull from MISP complete for {ioc_type}... extracting IOCs from JSON...")

        data = response.json()
        attributes = data['response']['Attribute']

        # Extract IOCs
        iocs = [attr['value'] for attr in attributes]

        # Save IOCs to CSV
        df = pd.DataFrame(iocs, columns=['value'])
        df.to_csv(csv_file, index=False)
        print(f"IOCs saved to {csv_file}.")
    except Exception as e:
        print(f"Error fetching IOCs of type {ioc_type}: {e}")

if __name__ == "__main__":
    # Example usage
    MISP_URL = "https://MISPIP/attributes/restSearch/json"
    MISP_API_KEY = "MISPAPI"
    requests.packages.urllib3.disable_warnings()
    # Example for URL IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'url.csv', ioc_type='url' , category='Network activity' , last='1d')

    # Example for IP Source IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'ip_src.csv', ioc_type='ip-src', category='Network activity' , last='1d')

    # Example for IP Destination IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'ip_dst.csv', ioc_type='ip-dst' , category='Network activity' , last='1d')

    # Example for MD5 IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'md5.csv', ioc_type='md5' ,category='Payload delivery' , last='1d')

    # Example for SHA256 IOCs
    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'sha256.csv', ioc_type='sha256' ,category='Payload delivery' , last='1d')

    # Example for Domain IOCs

    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'domain.csv', ioc_type='domain' , category='Network activity' , last='1d')

    # Example for  filenaem IOCs

    fetch_iocs_to_csv(MISP_URL, MISP_API_KEY, 'filename.csv', ioc_type='filename' , category='Network activity' , last='1d')

