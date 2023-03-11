import pyfiglet
from colorama import init
import port_sca
import network_sca
import socket

exit = False


def menu():
    init()
    ascii_banner = pyfiglet.figlet_format("SCRIPT HUB")
    print(ascii_banner)
    print("[1] Port Scanner (auto 1-1024) ")
    print("[2] Single Port Scanner ")
    print("[3] Custom Range Port Scanner ")
    print("[4] Network Host Discover ")
    print("[0] Exit ")

    option = int(input("Enter Your Option >> "))
    scanner = port_sca.Scanner()
    if option == 1:
        target = input("please enter an ip address >>> ")
        scanner.portscan(((target)))


    elif option == 2:
        target = input("please enter an ip address >>> ")
        portNumber = input("please enter an port number >>> ")
        scanner.portscan(((target)), ((portNumber)))

    elif option == 3:
        target = input("please enter an ip address >>> ")
        MIN = input("please enter beginning of port scan range >>> ")
        MAX = input("please enter end of port scan range >>> ")

        MIN = int(MIN)
        MAX = int(MAX)

        #bubble sort
        if MIN > MAX:
            temp = MIN
            MIN = MAX
            MAX = temp

        scanner.portscan(((target)), ((MIN)), ((MAX)))

    elif option == 4:
        network_sca.arp_scan()

    elif option == 0:
        return True

    else:
        menu()

    return False


while (exit != True):
    exit = menu()
