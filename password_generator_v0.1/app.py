import string
import random
import os

def author():
    print(f"{'Password Generator':^40}")
    print(f"{'Creator by agungwin22':^40}")
    print("="*40)

def showMenu():
    print("-"*40)
    print(" Pilih Untuk Kombinasi Password")
    print(" lalu terakhir pilih No4 untuk melihat Hasil")
    print("-"*40)
    print(" [1] Angka\n")
    print(" [2] Huruf\n")
    print(" [3] Karakter\n")
    print(" [4] Hasil")
    print("="*40)

while True:

    os.system("cls") # untuk windows
    # os.system("clear") # untuk linux & macos

    author()
    # mengambil panjang input password
    panjang = int(input(" Masukkan Panjang Password : "))

    showMenu()

    karakter = ""

    while True:
        pilihan = input(" Pilih Kombinasi : ")

        if pilihan == '1':
            karakter += string.digits
        elif pilihan == '2':
            karakter += string.ascii_letters
        elif pilihan == '3':
            karakter += string.punctuation
        elif pilihan == '4':
            break
        else:
            print(" Input salah!")

    password = []

    for i in range(panjang):

        randomchar = random.choice(karakter)

        password.append(randomchar)

    print("-"*40)
    print(" Password Generate : " + "".join(password))
    print("-"*40)

    isdone = input("\n Lanjut Generate ? (y/n) : ")

    if isdone == 'n':
        print("\n Keluar Aplikasi!\n")
        break