import random
import os
import datetime
import os
import time
global titik2,bantuan
#disetiap fungsi harus menyertakan fungsi (kumpulan variabel).
#karena di fungsi (kumpulan variabel ) itu terdapat semua varibale penting
#jika ingin menambahkan sebuah variabel yang dipake bersama
#maka kamu harus menmabahkan sintaks global (nama variabel) supaya bisa dipake bersama
# CARI PASSWORD YAAAAAAA......

titik2 = ":"
def catatan():
	print('''haiaiaiaiaiai''')




def waktu():
	global waktu_sekarang
	waktu_sekarang = datetime.datetime.now()
	

def kumpulan_varibel():
	global bantuan1
	global ayung,simson
	bantuan1 =  '''
	berikut beberapa peintah yang dapat diapakai

	1.konsol                  untuk masuk ke konsol sitem (jika didukung)
	2.hai semuanya            menyampaikan hai 
	3.apa kabar               menanyaka kabar

	perintah 4-7 masih dalam tahap pengerjaan

	4.aku ada kabar buruk     menyampaikan kabar buruk kepada ai
	5.jam berapa sekarang?    menanya waktu
	6.tanggal berapa sekaang  menanya tanggal
	7.kabar kamu gimana?      menanyai kabar

	'''
	ayung = 'darul'
	simson = 'simson'


def menu():
	os.system("clear")
	waktu()
	print("Waktu Sekarang (TAHUN-BULAN-TANGGAL : JAM) : ",waktu_sekarang.strftime("%y-%m-%d %H:%M:%S"))
	time.sleep(2)
	print(70*"=")
	nama = input("Passwordnya? : ")
	if nama == "konsol":
		konsol()
	if nama == "qwer":
		menu2()
	else:
		print("maaf,",nama,"bukanlah password yang tepat")
		#perencanaan disini akan saya buat sebuah algoritma curiga
		exit()
	
def menu2():
	kumpulan_varibel()
	global wktu
	os.system("clear")
	print(70*"=")
	print("")
	wktu = datetime.datetime.now()
	wktu.hour
	if wktu.hour < 12:
		print("  selamat pagi",simson)
	elif 12 <= wktu.hour < 18:
		print('  selamat siang',simson)
	else:
		print('  selamat  malam',simson)
	print("")
	print(70*"=")
	
	time.sleep(2)
	menu3()


def menu3():

	kumpulan_varibel()
	print(70*"=")

	input_menu2 = input("kamu > ")
	if input_menu2 == "hai semuanya":
		bot_sapa()
	if input_menu2 == "apa kabar":
		bot_sapa_kabar()
	else:
		print(bantuan1)

#kalo mau nambahin data.......................................
def rizky():
	kumpulan_varibel()
	global rizkynama,rizkysapa1,rizkykabar
	rizkynama = "rizky"
	rizkysapa1 = "hai"
	rizkykabar = "alhamdulillah baik"

def putri():
	kumpulan_varibel()
	global putrinama,putrisapa1,putrikabar
	putrinama = "putri"
	putrisapa1 = "haii"
	putrikabar = "baik, son :)"

def doni():
	kumpulan_varibel()
	global doninama,donisapa,donikabar
	doninama = "doni"
	donisapa = "halo"
	donikabar = "masih sehat kok, son ;)"

def rani():
	kumpulan_varibel()
	global raninama,ranisapa1,ranikabar
	raninama = "rani"
	ranisapa1 = "hi..."
	ranikabar = "hmm .. baik,  son :)"
#tutup............................................................


def bot_sapa():
	kumpulan_varibel()
	rizky()
	putri()
	doni()
	rani()

	print(rizkynama,titik2,rizkysapa1)
	print(putrinama,titik2,putrisapa1)
	print(doninama,titik2,donisapa)
	print(raninama,titik2,ranisapa1)
	print("")
	print(70*"=")
	print("")
	menu3()

def bot_sapa_kabar():
	waktu()
	rizky()
	putri()
	doni()
	rani()

	print(rizkynama,titik2,rizkykabar)
	print(putrinama,titik2,putrikabar)
	print(doninama,titik2,donikabar)
	print(raninama,titik2,ranikabar)

	menu3()


def pesan_konsol():

	print("gunakan konsol lagi?")
	pskon = input("(y/n)")
	if pskon == "Y":
		konsol()
	if pskon == "y":
		konsol()
	else:
		klr = ("keluar dari konsol? (y/n)")
		if klr == "y":
			exit()
		if klr == "Y":
			exit()
		else:
			print("sedang keluar dari konsol....")
			time.sleep(2)
			menu()

def konsol():
	print("selamat datang di konsol")
	kon = input("> ")
	os.system(kon)
	pesan_konsol()


menu()
	