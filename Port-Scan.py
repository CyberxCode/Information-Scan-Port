#!usr/bin/python
"""by:Abdallah"""
import socket
 
url = input('Enter url site: ')
 
print('\n+'+'-'*78+'+')
print('Scan Ports'.center(75))
print('+'+'-'*78+'+')
print('\nPlease wait.!\n')
 
for Port in range(0,100):
    Scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Search = Scan.connect_ex((url,Port))
    if Search == 0:
        print('Open Port: %s -> %s '.center(30) %(Port,socket.getservbyport(Port)))
    Scan.close()
         
print('\nFinish Scan\n'.center(30))