# Import the necessary modules
from socket import *
import time


# Define a class for scanning ports
class Scanner:
    # Define a method for scanning a range of ports
    def portscan(self, target=None, PortStart=None, PortEnd=None):

        # If no specific port range is given, scan the first 1024 ports
        if PortStart is None:
            # Print a message indicating that the scan is starting
            print('Starting scan on host: ', target)
            # Initialize a counter for the number of open ports found
            count = 0

            # Get the start time of the scan
            startTime = time.time()

            # Iterate over ports 1-1024 and attempt to connect to each
            for port in range(1, 1024):
                # Create a new socket object
                sock = socket(AF_INET, SOCK_STREAM)
                # Attempt to connect to the target on the current port
                con = sock.connect_ex((target, port))

                # If the connection was successful (i.e. no error occurred),
                # print a message indicating that the port is open and increment the counter
                if (con == 0):
                    print('Port %d: OPEN' % (port,))
                    count += 1
                # If the connection was not successful, print a message indicating that the port is closed
                else:
                    print('port %d: closed' % (port,))

                # Close the connection
                sock.close()

            # Print a message indicating that the scan is complete and report the results
            print('Port scan complete')
            print('Port scan found %d open ports' % (count,))
            print('Time taken:', time.time() - startTime)

        ################################################################################

        # If only one port is specified, scan only that port
        elif PortEnd is None:

            # Print a message indicating that the scan is starting
            print('Starting scan on host: ', target)
            # Get the start time of the scan
            startTime = time.time()

            # Create a new socket object
            sock = socket(AF_INET, SOCK_STREAM)

            # Attempt to connect to the target on the specified port
            con = sock.connect_ex((target, int(PortStart)))
            # If the connection was successful, print a message indicating that the port is open
            if (con == 0):
                print('Port %s: is OPEN' % (PortStart,))

            # If the connection was not successful, print a message indicating that the port is closed
            else:
                print('port %s: is closed' % (PortStart,))

            # Close the connection
            sock.close()

            # Print a message indicating that the scan is complete and report the results
            print('Port scan complete')
            print('Time taken:', time.time() - startTime)

        # If a range of ports is specified, scan that range
        else:
            # Print a message indicating that the scan is starting
            print('Starting scan on host: ', target)

            # Initialize a counter for the number of open ports found
            count = 0
            # Get the start time of the scan
            startTime = time.time()

            # Iterate over the specified range of ports and attempt to connect to each
            for port in range(int(PortStart), int(PortEnd)):
                # Create a new socket object
                sock = socket(AF_INET, SOCK_STREAM)
                # Attempt to connect to the target on the current port
                con = sock.connect_ex((target, port))
                # If the connection was successful, print a message indicating that the port is open
                if (con == 0):
                    print('Port %d: OPEN' % (port,))
                    count += 1
                # If the connection was not successful, print a message indicating that the port is open
                else:
                    print('port %d: closed' % (port,))
                sock.close()
            # Print a message indicating that the scan is complete and report the results
            print('Port scan complete')
            print('Port scan found %d open ports' % (count,))
            print('Time taken:', time.time() - startTime)
