# Import the Scapy library
import scapy.all as scapy
# Import the regular expression library
import re
def arp_scan():
    # Define a regular expression pattern to match a valid IP address range
    ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    # Prompt the user to enter an IP address range
    ip_add_range_input = input("Please enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")

    # Check if the user input matches the regular expression pattern
    if ip_range_pattern.search(ip_add_range_input):
        # Use the Scapy library's "arping()" function to send ARP requests to all the IP addresses in the specified range
        print(f"{ip_add_range_input} is a valid ip address range")

    # Return the results of the ARP scan
    arp_result = scapy.arping(ip_add_range_input)