# Network Scanner

## Overview

The Network Scanner is a Python script designed to perform concurrent scanning of hosts for open ports. It utilizes the `nmap3` library for port scanning and supports multi-threading for efficient scanning of multiple hosts simultaneously.

## Features

- **IP Validation:** The script includes a method to validate the format of an IP address.
- **Host Scanning:** Scans hosts for open ports using the Nmap tool with specified port numbers.
- **Concurrent Execution:** Leverages Python's `concurrent.futures.ThreadPoolExecutor` for concurrent scanning of multiple hosts.
- **Output Generation:** Outputs the scan results, including hostnames, IP addresses, and open ports, to a CSV file ('output.csv').

## Dependencies

- `nmap3`
- `pandas`

## Usage

1. **Installation:**
   - Install the required dependencies using `pip install -r requirements.txt`.

2. **Host List:**
   - Create a file named 'hosts.txt' containing a list of hosts (hostnames or IP addresses) to be scanned, with each host on a new line.

3. **Execution:**
   - Run the script using `python network_scanner.py`.
   - The script will perform concurrent scanning of the hosts and generate an 'output.csv' file with the scan results.

## Output Format

The generated 'output.csv' file will have the following columns:

- `host`: Hostname or IP address of the scanned host.
- `ip`: IP address of the host.
- `ports`: List of open ports on the host.

## Notes

- The script uses Nmap for port scanning, and it should be installed on the system for accurate results.
- Adjust the list of ports to scan in the `args` parameter of the `nmap_portscan_only` method if needed.

## Example

```bash
$ python network_scanner.py
