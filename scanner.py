#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#define our target
if len(sys.argv) ==  2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("Invalid amount of arguments")
	print("Synatx : Python3 scanner.py <ip>")

#add a banner
print("*" * 50)
print("Scanning Target: "+target)
print("Time Started: "+str(dt.now()))
print("*" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Checking ports")
			print(f"port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting Programme.")
	sys.exit()
except socket.gaierror:
	print("Hostname Could Not Be Resolved")
	sys.exit()
except socket.error:
	print("Could Not Connect To Server.")
	sys.exit()
