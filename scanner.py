import sys
import socket
import re
from datetime import datetime



#ADD A PRETTY BANNER
class bcolors:
    BRIGHTGREEN='\033[1;32;40m'
    BRIGHTMAGENTA='\033[1;34;40m'
    DARKGRAY='\033[1;30;40m'
    GREEN='\033[92m'
    YELLOW='\033[93m'
    RED='\033[91m'


print(bcolors.RED + '~~> PORT SCANNER v1.0 <~~')
print(bcolors.DARKGRAY + '>> MADE WITH CODES <<')
print(bcolors.RED + "~~> AUTHOR: zRainerzz <~~")
print(bcolors.BRIGHTMAGENTA + '''
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀⠀⠀⠀⢀⣀⣤⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣤⣀⠀⠀⠀⠀⠀⠐⣤⡀
⠀⠀⠀⠀⠀⢀⣴⡿⠁⠀⠀⣀⣴⣾⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣤⣀⠀⠀⠘⣿⣆
⠀⠀⠀⠀⣠⣾⡿⠁⢀⣴⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠘⣿⣷⡀
⠀⠀⠀⣰⣿⡿⠁⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⠀⠀⠸⣿⣿⡄
⠀⠀⣸⣿⣿⠃⠀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀                    ⠀⠀ ⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢹⣿⣿⡄
⠀⢰⣿⣿⡏⠀⠀⠀⠀⠘⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⣿⣿⣷
⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⢹⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠀⠠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠇⠀⠀⠀⠀⠀⢸⣿⣿⣇
⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣤⣄⢠⣾⣿⣿⠃⠀⠀⠹⣿⣿⣷⠀⢀⣴⣿⣿⣿⣶⣶⣶⣦⣴⣿⣿⡏⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿
⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇
⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣠⣤⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣄⡀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣤⣤⣤⣄⣀⠀⠀⠀⣀⣴⣿⣿⣿⡿⠿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡿⢿⣿⣿⣷⣄⡀⠀⠀⠀⣀⣠⣤⣤⣼⣿⣿⣿⡏
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠉⠉⠙⠛⠻⠿⢿⣿⣿⡿⠟⢁⣠⣾⣿⣿⣿⠿⣫⣿⣿⣿⣿⣿zRainerzz⣿⣿⣿⣿⣻⢿⣿⣿⣿⣦⣄⠙⠻⣿⣿⣿⡿⠿⠛⠛⠉⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢀⣴⣿⣿⣿⠿⢋⣵⣾⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣷⣭⡛⢿⣿⣿⣷⣄⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠟⢁⣶⣿⣿⡿⠋⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⠻⣿⣿⣿⣦⠉⠻⣿⣿⣷⣄
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⡿⠋⠀⠀⢸⣿⣿⣿⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣿⣿⣿⡄⠀⠈⠛⢿⣿⣿⣦⡀
⠀⠀⠀⠀⢀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣿⣶⣄⣀
⠀⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡇
⠀⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡇
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇
⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇
⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿
⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿
⠀⠀⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇
⠀⠀⠸⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿
⠀⠀⠀⢻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠇
⠀⠀⠀⠀⢻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣴⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠂⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠚⠋⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡄⠀⠀⠀⠀⠀⠀⣰⠿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠚⠁''')
    






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
        except socket.gaierror:#That's what happens when the hostname is not resolved
            print(bcolors.YELLOW + "Hostname could not be resolved. ˙◠˙")
            sys.exit()

    print(f"Target IP: {target}")

else:
    print(bcolors.RED + "Invalid number of arguments.")
    print(bcolors.RED + "Syntax: python3 scanner.py <ip address or hostname>")


print(bcolors.GREEN + "-" * 50)
print(bcolors.GREEN + "Scanning target... (˵ •̀ᴗ•́˵)و")
print(bcolors.GREEN + "Time started " + str(datetime.now()))
print(bcolors.GREEN + "-"*50)
print(bcolors.GREEN + "Full scan takes a while btw.")
range_scan=input(bcolors.GREEN + "f full_scan (65535 ports) - n normal_scan (50,85 ports)").title()

try: 
    if range_scan=="N":
        for port in range(50,85):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)#if it doesn't respond back in a second then it will move on.
            result= s.connect_ex((target , port))
            if result == 0:
                print(f"Port {port} is open")
                
            s.close()
                
    elif range_scan=="F":
        for port in range(1,65535):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Gather the IPv4 addr / Gather the port we are trying to connect to
            socket.setdefaulttimeout(1)#if it doesn't respond back in a second then it will move on.
            result= s.connect_ex((target , port))#i wanna connect on target and port
            if result == 0:#if the port is open, it will return 0, if it is close it returns a 1
                print(bcolors.RED + f"(˵ •̀ᴗ•́˵)و Port {port} is open")
                
            s.close()
            
    else:
        print(bcolors.YELLOW + "F or N is a must, you should start over ˙◠˙").title()
        sys.exit()
        
except KeyboardInterrupt: #that means it will be stopped if we press CTRL + C
    print(bcolors.YELLOW + "\n Exiting program. ˙◠˙")
    sys.exit()
    
except socket.error:
    print(bcolors.YELLOW + "We could not connect to server.")
    sys.exit()