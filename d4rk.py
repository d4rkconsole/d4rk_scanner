#!/bin/python3
import socket
import pyfiglet
from datetime import datetime
import termcolor


banner = pyfiglet.figlet_format(" D4RK  SCANNER ")
print(banner)
print('-' * 80)
print("Time started at : " , datetime.now())
print("Scanning tool with banner grabbing it will  do :")
print(" [+]  Tool Created by D4rk sh4d0w : Hacker and programmer ")
print(" [*] Follow my friend name - yourAnonS0u1  and Lorian synaro ")
print(""" [+] yourAnonS0u1 Github profile : https://github.com/HLoTW 
 [+]  Lorian synaro twitter : https://twitter.com/loriansynaro """ )
print('-' * 80)

target = input(" [+] Enter the target ip to Scan : ")
ports = int(input(" [*] Enter how many ports you want to scan : "))

for ports in range(1,ports):

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,ports))
		s.settimeout(1)
		print(" [+] port number: " ,str(ports) ,' is opened')
		print( " [*] Banner of port no : " , str(ports) , ' is : ',s.recv(1024))
		s.close()
		

		
		
	except:
		pass


		
