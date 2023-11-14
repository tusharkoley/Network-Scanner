import nmap3
import pandas as pd
import concurrent.futures
import socket
import ipaddress

class NetworkScanner:
    def __init__(self):
        self.nmap = nmap3.NmapHostDiscovery()

    def validate_ip(self, ip):
        """
        Validate if the given IP address is in a valid format.

        Parameters:
        - ip (str): The IP address to validate.

        Returns:
        - bool: True if the IP is valid, False otherwise.
        """
        try:
            ipaddress.IPv4Address(ip)  # Change to IPv6Address for IPv6 validation
            return True
        except ipaddress.AddressValueError:
            return False
    
    def scan_a_host(self, host):
        """
        Scan a host for open ports.

        Parameters:
        - host (str): The hostname or IP address to scan.

        Returns:
        - dict: A dictionary containing host information, including IP and open ports.
        """
        results = self.nmap.nmap_portscan_only(host, args="-open -p 20,21,22,23,25,53,69,80,443,3301")
        
        ip = list(results.keys())[0] 
        res_dict = dict()
        res_dict['host'] = host
        if self.validate_ip(ip):
            ports = [port_data['portid'] for port_data in results[ip]['ports']]
            
            res_dict['ip'] = ip
            res_dict['ports'] = ports
        else:
            res_dict['ip'] = 'Invalid'
            res_dict['ports'] = ['NA']
            
        return res_dict

    def get_ip_address(self, hostname):
        """
        Get the IP address for a given hostname.

        Parameters:
        - hostname (str): The hostname to resolve.

        Returns:
        - str: The IP address of the hostname.
        """
        try:
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except socket.error as e:
            print(f"Error: {e}")
            return None


# Main execution
THREAD_POOL_SIZE = 5
all_results_dict = dict()

# Read hosts from 'hosts.txt'
with open('hosts.txt') as f:
    data = f.read()
    hosts = list(set(data.split()))

# Initialize NetworkScanner
network_scanner = NetworkScanner()

# Use ThreadPoolExecutor for concurrent scanning
with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as pool:
    # Submit host scanning tasks
    host_submit_dict = {host: pool.submit(network_scanner.scan_a_host, host) for host in hosts}

# Collect results
host_lst = []
ips = []
ports = []
print(f'Started Collecting the results {len(hosts)}')
for host in hosts:
    res = host_submit_dict[host].result()
    host_lst.append(res['host'])
    ips.append(res['ip'])
    ports.append(res['ports'])

# Create a DataFrame from the results
data = pd.DataFrame({'host': host_lst, 'ip': ips, 'ports': ports})

data.to_csv('output.csv')

print('Succesffuly Created the output file')