import scapy.all as scapy
import re
def arp_scan():

    ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    ip_add_range_input = input("Please enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")

    if ip_range_pattern.search(ip_add_range_input):
        print(f"{ip_add_range_input} is a valid ip address range")

    arp_result = scapy.arping(ip_add_range_input)