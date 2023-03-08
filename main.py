import pyfiglet
from colorama import init
import port_sca
import socket

exit = False

def menu():
    init()
    ascii_banner = pyfiglet.figlet_format("SCRIPT HUB")
    print(ascii_banner)
    print("[1] Port Scanner (auto 1-1024)")
    print("[2] Single Port Scanner ")
    print("[3] Custom Range Port Scanner ")
    print("[0] Exit ")

    option = int(input("Enter Your Option >> "))

    if option == 1:
        target = input("please enter an ip address >>> ")
        port_sca.portscan((target))


    elif option == 2:
        target = input("please enter an ip address >>> ")
        portNumber = input("please enter an port number >>> ")
        port_sca.portscan((target),(portNumber))

    elif option == 3:
        target = input("please enter an ip address >>> ")
        MIN = input("please enter beginning of port scan range >>> ")
        MAX = input("please enter end of port scan range >>> ")

        port_sca.portscan((target),(MIN),(MAX))


    elif option == 0:
        return True

    return False



while (exit != True):
    exit = menu()