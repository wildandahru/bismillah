import socket, os, sys

ip = input('Masukkan Alamat IP yg dituju: ')
port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	client.connect((ip, port))
except:
	print('Ip tidak bisa terhubung')
	sys.exit(0)


#Fungsi pada klien ---------------------------------------------------------
def buat_file(dir, client):
	nama = client.recv(1024)
	while nama:
		print((nama).decode())
		if "stop" in nama:
			break

#Akhir Fungsi ----------------------------------------------------------		
	
acc = client.recv(1024)
print((acc).decode())

dir = input("Masukkan direktory penyimapanan : ")
buat_file(dir, client)


