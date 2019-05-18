import socket, os, sys

ip = input("Masukkan Alamat IP : ")
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	server.bind((ip, port))
except:
	print('IP gagal di bindingkan ...')
	sys.exit(0)

server.listen(1)

#Fungsi pada Server -------------------------------

def kirim_nama(dir, conn):	
	i=0
	num = len(dir)
	dft = os.listdir(dir)
	while i < num:
		print(dft[i])
		nm = os.path.basename((dft[i]))
		conn.send((nm).encode())
		i += 1
	conn.send(("stop").encode())
#Akkhir Fungsi -------------------------------------

conn, client_addr = server.accept()
acc = 'Koneksi sudah diterima'
conn.send((acc).encode())
dir = input('Masukkan path direktori yg akan direplikasi : ')
kirim_nama(dir, conn)


