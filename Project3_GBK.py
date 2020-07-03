



    # import Libary Random 
from random import randint


    #membuat list
Glist = ["Batu","Gunting","Kertas"]

    #memanggil function randint agar value di "Glist" menjadi acak setiap dipanggil
acak = Glist[randint(0,2)]

    #buat variabel untuk melakukan while loop
user = True

    #membuat function Permaian yang memiliki parameter "acak" dan "user"
def Permaian(acak,user):

                #while Looping
            while user == True:
                user = input("Masukan Pilihanmu: ")
                if user == "Batu":
                    if acak == "Kertas":
                        print("Anda kalah,Kertas menutupi Batu")
                    elif acak == "Gunting":
                        print("Anda menang, Batu menghancurkan Gunting")
                    else:
                        print("Anda seri dengan komputer")

                elif user == "Gunting":
                    if acak == "Kertas":
                        print("Anda menang, Gunting memotong kertas ")
                    elif acak == "Batu":
                        print("Anda Kalah, gunting hancur dengan Batu")
                    else:
                        print("Anda seri dengan komputer")

                elif user == "Kertas":
                    if acak == "Gunting":
                        print("Anda kalah, Gunting memotong Kertas")
                    elif acak == "Batu":
                        print("Anda Menang, Kertas menutupi Batu")
                    else:
                        print("Anda Seri dengan Komputer")

                else:
                    print("Perintah tidak dikenal, Coba lagi!!")
                
                    # menambhakan  user dan acak agar terjadinya looping berulang
                user = True
                acak = Glist[randint(0,2)]

    #menampilkan function Permainan
Permaian(acak,user)