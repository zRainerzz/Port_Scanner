import sys
import socket
import re
from datetime import datetime

# Define regex for strict IPv4 matching
strict_ipv4_regex = r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'

# Check the number of arguments
if len(sys.argv) == 2:
    input_address = sys.argv[1]

    # Validate the input as either an IPv4 or a hostname
    if re.match(strict_ipv4_regex, input_address):
        target = input_address  # It's a valid IPv4 address
    else:
        try:
            target = socket.gethostbyname(input_address)  # Translate hostname to IPv4
        except socket.gaierror:
            print("Invalid hostname or IP address.")
            sys.exit()

    print(f"Target IP: {target}")

else:
    print("Invalid number of arguments.")
    print("Syntax: python3 scanner.py <ip address or hostname>")


#ADD A PRETTY BANNER
