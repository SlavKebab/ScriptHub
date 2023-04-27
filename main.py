# importing libraries
import pyfiglet
from colorama import init
import network_sca
import port_sca
import socket

# Define a variable to control the main loop of the program
exit = False

# Define a function to display the main menu
def menu():
    init()
    # Generate an ASCII art banner for the program title
    ascii_banner = pyfiglet.figlet_format("SCRIPT HUB")
    print(ascii_banner)
    print("---------------------------v1.0-----------------------------")
    print("-----------------Developed by Jamie Young-------------------\n")

    # Display the available scanning options to the user
    print("[1] Port Scanner (auto 1-1024)")
    print("[2] Single Port Scanner ")
    print("[3] Custom Range Port Scanner ")
    print("[4] Network Range Scanner")
    print("[0] Exit ")

    # Read the user's input for which scanning task to perform
    option = int(input("Enter Your Option >> "))

    # Create a new instance of the port_sca.Scanner() class to use for scanning
    scanner = port_sca.Scanner()

    # Perform the selected scanning task based on the user's input
    if option == 1:
        # Prompt the user for an IP address to scan
        target = input("please enter an ip address >>> ")
        # Call the portscan() method of the Scanner class to perform the scan
        scanner.portscan(((target)))


    elif option == 2:
        # Prompt the user for an IP address and port number to scan
        target = input("please enter an ip address >>> ")
        portNumber = input("please enter an port number >>> ")
        # Call the portscan() method with the target IP address and port number
        scanner.portscan(((target)), ((portNumber)))


    elif option == 3:
        # Prompt the user for an IP address and a range of ports to scan
        target = input("please enter an ip address >>> ")
        MIN = input("please enter beginning of port scan range >>> ")
        MAX = input("please enter end of port scan range >>> ")
        # Convert the range inputs from strings to integers
        MIN = int(MIN)
        MAX = int(MAX)
        # Swap the values of MIN and MAX if necessary to ensure MIN <= MAX
        if MIN > MAX:
            temp = MIN
            MIN = MAX
            MAX = temp
        # Call the portscan() method with the target IP address and port range
        scanner.portscan(((target)), ((MIN)), ((MAX)))

    elif option == 4:
        # Call the arp_scan() function from the network_sca module to perform an ARP scan
        network_sca.arp_scan()


    elif option == 0:
        # If the user selects "Exit", set exit = True to terminate the main loop
        return True

    # Return False to indicate that the program should continue running
    return False

# While loop executes until the variable "exit" is True
while (exit != True):
    exit = menu()
