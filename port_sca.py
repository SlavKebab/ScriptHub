from socket import *
import time


def portscan(target,PortStart = None,PortEnd = None):

    if PortStart is None:
        print('Starting scan on host: ', target)

        count = 0
        startTime = time.time()

        for port in range(1, 1024):
            sock = socket(AF_INET, SOCK_STREAM)

            con = sock.connect_ex((target, port))
            if (con == 0):
                print('Port %d: OPEN' % (port,))
                count += 1
            else:
                print('port %d: closed' % (port,))
            sock.close()

        print('Port scan complete')
        print('Port scan found %d open ports' % (count,))
        print('Time taken:', time.time() - startTime)

################################################################################

    elif PortEnd is None:
        print('Starting scan on host: ', target)

        startTime = time.time()


        sock = socket(AF_INET, SOCK_STREAM)

        con = sock.connect_ex((target, PortStart))
        if (con == 0):
             print('Port %d: is OPEN' % (PortStart,))

        else:
            print('port %d: is closed' % (PortStart,))
        sock.close()

        print('Port scan complete')
        print('Time taken:', time.time() - startTime)

###############################################################################

    else:
        print('Starting scan on host: ', target)

        count = 0
        startTime = time.time()

        for port in range(PortStart, PortEnd):
            sock = socket(AF_INET, SOCK_STREAM)

            con = sock.connect_ex((target, port))
            if (con == 0):
                print('Port %d: OPEN' % (port,))
                count += 1
            else:
                print('port %d: closed' % (port,))
            sock.close()

        print('Port scan complete')
        print('Port scan found %d open ports' % (count,))
        print('Time taken:', time.time() - startTime)
