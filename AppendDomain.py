
import csv
import logging
import re

# Configure logging
logging.basicConfig(filename='/var/log/domain_append_service.log', level=logging.INFO, format='%(asctime)s %(message)s')

def is_valid_domain(domain):
    """
    Validate a domain using a regular expression.
    """
    # Regex pattern for validating domain names
    domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.(?!-)[A-Za-z0-9-]{1,63}(?<!-)$'
    return re.match(domain_regex, domain) is not None

def read_existing_domains(file_path):
    """Read existing domains from a CSV file and return a set of valid domains."""
    existing_domains = set()
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                domain = row[0].strip()  # Assumes domain is in the first column
                if is_valid_domain(domain):
                    existing_domains.add(domain)
    except FileNotFoundError:
        # File does not exist, so no existing domains
        pass
    return existing_domains

def append_unique_data(source_file, target_file):
    """Append unique and valid domains from source_file to target_file."""
    existing_domains = read_existing_domains(target_file)

    with open(source_file, 'r') as source, open(target_file, 'a', newline='') as target:
        reader = csv.reader(source)
        writer = csv.writer(target)

        headers_written = False
        for row in reader:
            domain = row[0].strip()  # Assumes domain is in the first column
            if is_valid_domain(domain) and domain not in existing_domains:
                if not headers_written:
                    # Write header if it's the first time
                    writer.writerow(['Domain'])  # Adjust header if necessary
                    headers_written = True
                writer.writerow([domain])
                existing_domains.add(domain)

    logging.info("Valid and unique domains appended successfully!")

if __name__ == "__main__":
    source_file = '/PathtotheDomainFIle/domain.csv'  # Update path for domains source CSV
    target_file = '/PathtotheDomainFIle/mispdomain.csv'    # Update path for target CSV

    append_unique_data(source_file, target_file)
    logging.info("Domain append task completed.")
