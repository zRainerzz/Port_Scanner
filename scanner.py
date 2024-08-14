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
    



#Define our target

if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
    
else:
    print(bcolors.RED + "Invalid amount of arguments.")
    print(bcolors.RED + "Syntax: python3 scanner.py <ip address>")


print(bcolors.GREEN + "-" * 50)
print(bcolors.GREEN + "Scanning target... (˵ •̀ᴗ•́˵)و")
print(bcolors.GREEN + "Time started " + str(datetime.now()))
print(bcolors.GREEN + "-"*50)


try: 

    for port in range(50,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Gather the IPv4 addr / Gather the port we are trying to connect to
        socket.setdefaulttimeout(1)#if it doesn't respond back in a second then it will move on.
        result= s.connect_ex((target , port))#i wanna connect on target and port
        if result == 0:#if the port is open, it will return 0, if it is close it returns a 1
            print(bcolors.RED + f"Port {port} is open 𓆩😈𓆪")
                
        s.close()
                
except KeyboardInterrupt: #that means it will be stopped if we press CTRL + C
    print(bcolors.YELLOW + "\n Exiting program. ˙◠˙")
    sys.exit()

except socket.gaierror:
    print(bcolors.YELLOW + "Hostname could not be resolved. ˙◠˙")
    sys.exit()

except socket.error:
    print(bcolors.YELLOW + "We could not connect to server. ˙◠˙")
    sys.exit()