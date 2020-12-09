import sys
import os
import urllib
import urllib.request

sys.ps1 = '\033[92m'

print(sys.ps1)



print('''
 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
            url source code reader by V1 MoDzZz
                       
''')


url = input("Enter your url you want to read : ")

req = urllib.request.urlopen(url)

b10 = req.read()

fb100 = b10.decode('utf-8')

print(fb100)
