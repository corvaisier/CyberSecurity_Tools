#!usr/bin/env python3

# used to practice fuzzing and vulnerability researches/exploits in vulnserver
# usefull to found vulnerabilities and what type of characters create crash but not to determinate how many characters will create the crash 
# basic_fuzzer.py could determinate lenght of input

from boofuzz import *

# need to specifie good ip address
host = "127.0.0.1"
# default port of vulnserver
port = 9999

# boilerplate boofuzz
session = Session(
    target = Target(
        connection = SocketConnection(
            host, port, proto = "tcp"
        )
    )
)

# target program : HTER
s_initialize("HTER")

# fuzz syntax define
s_string("HTER", fuzzable = False)
s_delim("", fuzzable = False)
s_string("FUZZ", fuzzable = True) # fuzz point

# connection tu the server
session.connect(s_get("HTER"))
session.fuzz
