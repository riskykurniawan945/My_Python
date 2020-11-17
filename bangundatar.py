import math
import os

user = input("\n\n\nMasukkan Nama anda :    ")
print("\nSelamat datang!,  {}".format(user))

def persegi():
    if (pil == "LUAS"):
        print("Luas Persegi")
        s = int(input("Masukkan panjang sisinya (cm):   "))
        L = s * s 
        print("L = sisi * sisi")
        print("Luas = {} cm^2".format(L))
        return L

    elif (pil == "KELILING"):
        print("Keliling Persegi")
        s = int(input("Masukkan panjang sisinya (cm):   "))
        K = 4 * s
        print("K = sisi + sisi + sisi + sisi")
        print("Keliling = {} cm".format(K))    
        return K


def persegiPanjang():
    if (pil == "LUAS"):
        print("Luas Persegi panjang")
        p = int(input("Masukkan panjangnya (cm):\t"))
        l = int(input("Masukkan lebarnya (cm):\t"))
        L = p * l
        print("L = panjang * lebar")
        print("Luas = {} cm^2".format(L)) 
        return L

    elif (pil == "KELILING"):
        print("Keliling Persegi panjang")
        p = int(input("Masukkan panjangnya (cm):\t"))
        l = int(input("Masukkan lebarnya (cm):\t"))
        K = 2 * (p + l)
        print("K = 2 * (panjang + lebar)")  
        print("Keliling = {} cm".format(K))    
        return K



def jajarGenjang():
    if (pil == "LUAS"):
        print("Luas Jajar genjang")
        sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
        t = int(input("Masukkan tingginya (cm):\t"))
        L = sBawah * t
        print("L = alas * tinggi")
        print("Luas = {} cm^2".format(L))
        return L  

    elif (pil == "KELILING"):
        print("Keliling Jajar genjang")
        sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
        sMiring = int(input("Masukkan panjang sisi miringnya (cm):\t"))
        K = 2 * (sBawah + sMiring)
        print("K = 2 * (sisiBawah + sisiMiring)")
        print("Keliling = {} cm".format(K)) 
        return K



def trapesium():
    if (pil == "LUAS"):
        print("Luas Trapesium")
        sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
        sAtas = int(input("Masukkan panjang sisi atasnya (cm):\t"))
        t = int(input("Masukkan tingginya (cm):\t"))
        L = .5 * (sBawah + sAtas) * t
        print("L = 1/2 * (alas + sisiAtas) * tinggi")
        print("Luas = {} cm^2".format(L))  
        return L

    elif (pil == "KELILING"):
        print("Keliling Trapesium")
        sBawah = int(input("Masukkan panjang sisi alasnya (cm):\t"))
        sAtas = int(input("Masukkan panjang sisi atasnya (cm):\t"))
        sKanan = int(input("Masukkan panjang sisi kanannya (cm):\t"))
        sKiri = int(input("Masukkan panjang sisi Kirinya (cm):\t")) 
        K = sAtas + sKiri + sKanan + sBawah
        print("K = sAtas+sKiri+sKanan+sBawah")
        print("Keliling = {} cm".format(K))
        return K


def belahKetupat():
    if (pil == "LUAS"):
        print("Luas Belah Ketupat")
        d1 = int(input("Masukkan panjang diagonal1 (cm):     "))
        d2 = int(input("Masukkan panjang diagonal2 (cm):     "))
        L = d1 * d2 * .5
        print("L = 1/2 * diagonal1 * diagonal2")
        print("Luas = {} cm^2".format(L))  
        return L

    elif (pil == "KELILING"):
        print("Keliling Belah Ketupat")
        s = int(input("Masukkan panjang sisinya (cm):   "))
        K = 4 * s
        print("K = sisi + sisi + sisi + sisi")
        print("Keliling = {} cm".format(K))
        return K


def layangLayang():
    if (pil == "LUAS"):
        print("Luas Layang-layang")
        d1 = int(input("Masukkan panjang diagonal1 (cm):     "))
        d2 = int(input("Masukkan panjang diagonal2 (cm):     "))
        L = d1 * d2 * .5
        print("L = 1/2 * diagonal1 * diagonal2")
        print("Luas = {} cm^2".format(L))  
        return L

    elif (pil == "KELILING"):
        print("Keliling Layang-layang")
        s1 = int(input("Masukkan panjang sisi1 (cm):     "))
        s2 = int(input("Masukkan panjang sisi2 (cm):     "))
        K = 2 * (s1 + s2)
        print("K = 2 * sisi1 * sisi2")
        print("Keliling = {} cm".format(K))
        return K


def segitiga():
    if (pil == "LUAS"):
        print("Luas Segitiga")
        sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
        t = int(input("Masukkan tingginya (cm):\t"))
        L = .5 * sBawah * t
        print("L = 1/2 * alas * tinggi")
        print("Luas = {} cm^2".format(L)) 
        return L

    elif (pil == "KELILING"):
        print("Keliling Segitiga")
        s1 = int(input("Masukkan panjang sisi1 (cm):     "))
        s2 = int(input("Masukkan panjang sisi2 (cm):     "))
        s3 = int(input("Masukkan panjang sisi3 (cm):     "))
        K = s1 + s2 +s3
        print("K = s1 + s2 + s3")
        print("Keliling = {} cm".format(K))
        return K


def lingkaran():
    if (pil == "LUAS"):
        print("Luas Lingkaran")
        r = int(input("Masukkan panjang jari-jarinya (cm):   "))
        L = math.pi * r**2
        print("L = pi * jari-jari^2")
        print("Luas = {} cm^2".format(L)) 
        return L

    elif (pil == "KELILING"):
        print("Keliling Lingkaran")
        r = int(input("Masukkan panjang jari-jarinya (cm):   "))
        K = 2 * math.pi * r
        print("K = 2 * pi * jari-jari")
        print("Keliling = {} cm".format(K))
        return K    


kerjakan = True
while(kerjakan):
    print("\n\n==================================================")
    print("Aplikasi Penghitung Luas dan Keliling Bangun datar")
    print("==================================================")
    print("[1] Persegi")
    print("[2] Persegi panjang")
    print("[3] Jajar Genjang")
    print("[4] Trapesium")
    print("[5] Belah Ketupat")
    print("[6] Layang-Layang")
    print("[7] Segitiga")
    print("[8] Lingkaran")

    bangun = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang", "Segitiga", "Lingkaran"]
    
    EROR = True
    while (EROR): 
        try:
            indeks = int(input("\nBangun apa yang ingin anda pilih? (Angkanya saja):     "))
            if (indeks >= 1 and indeks <= 8):
                EROR = False
                print("Anda Memilih bangun {}\n".format(bangun[indeks-1]))   
            else:
                print("Masukkan angka diantara 1 - 8")
        except ValueError:
            print("Input anda salah, Masukkan angka diantara 1 - 8")

    EROR = True
    while (EROR): 
        pil = input("LUAS / KELILING? (Dalam huruf Kapital) :    ")
        if (pil != "LUAS" and pil != "KELILING"):
            print("Input anda salah!!!")   
        else:
            EROR = False
            print("Anda Memilih {} {}\n\n".format(pil, bangun[indeks-1]))

    if (indeks == 1):
        hasil = persegi()

    elif (indeks == 2):
        hasil = persegiPanjang()
    
    elif (indeks == 3):
        hasil = jajarGenjang()
    
    elif (indeks == 4):
        hasil = trapesium()
    
    elif (indeks == 5):
        hasil = belahKetupat()
    
    elif (indeks == 6):
        hasil = layangLayang()
    
    elif (indeks == 7):
        hasil = segitiga()
    
    elif (indeks == 8):
        hasil = lingkaran()


    # File Handling 
    file_history = open("history.txt", "a")

    if (pil == "LUAS"):
        history = "\nNama :{}\n{}, {}, {}cm^2\n-------".format(user, bangun[indeks-1], pil, hasil)
    elif(pil == "KELILING"):
        history = "\nNama :{}\n{}, {}, {}cm\n-------".format(user, bangun[indeks-1], pil, hasil)

    file_history.write(history)
    file_history.close()


    EROR = True
    while(EROR):
        tampil = input("Apakah anda ingin Melihat History Penghitungan? :    ")
        if (tampil == "YA"):
            # open
            file = open("history.txt", "r")
            file = file.read()
            print(file)        
            EROR = False

        elif (tampil == "TIDAK"):
            EROR = False
            
        else:
            print("Input anda salah")
            continue




    #=====================Ulangi=======================



    EROR = True
    while (EROR):
        ulangi = input("\n\nUlangi?  (YA / TIDAK) (Dalam huruf Kapital)! :   ")

        if (ulangi == "YA"): #YA
            EROR = False
            user = input("\n\n\nMasukkan Nama anda :    ")

        elif (ulangi == "TIDAK"): #TIDAK
                print("\nTerima Kasih!\n\n")
                EROR = False
                kerjakan = False
                delete = input("Apakah anda ingin Menghapus History? :    ")
                if (delete == "YA"):
                    os.remove("history.txt")
                    print("History telah terhapus!")       
                    EROR = False
                elif (delete == "TIDAK"):
                    pass
                else:
                    print("Input anda salah")
                    
        else:
            print("Input anda salah!!!")