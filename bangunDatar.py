print("Selamat datang!\n")

kerjakan = True
while(kerjakan):
    print("\n\n==========================================================")
    print("Aplikasi Penghitung Luas dan Keliling Bangun datar")
    print("==========================================================")
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Jajar Genjang")
    print("4. Trapesium")
    print("5. Belah Ketupat")
    print("6. Layang-layang")
    print("7. Segitiga")
    print("8. Lingkaran")
    
    indeks = int(input("Bangun apa yang ingin anda pilih? :     "))
    #JIKA YANG DIINPUT BUKAN ANGKA (1-8)
    if (indeks > 8 or indeks < 1):
        print("\n\nInput yang anda masukkan Salah!  (Masukkan angka dari 1-8)!,\nUlangi!")
        continue
    
    pil = input("LUAS / KELILING? (Dalam huruf Kapital) :    ")


    #LUAS
    if (pil == "LUAS"):
        if   (indeks == 1): #PERSEGI
            print("Luas Persegi")
            s = int(input("Masukkan panjang sisinya :   "))
            L = s*s
            print("L = sisi * sisi")
        elif (indeks == 2): #PERSEGI PANJANG
            print("Luas Persegi panjang")
            p = int(input("Masukkan panjangnya :    "))
            l = int(input("Masukkan lebarnya :   "))
            L = p*l
            print("L = panjang * lebar")    
        elif (indeks == 3):
            print("Luas Jajar genjang")
            sBawah = int(input("Masukkan panjang alasnya :   "))
            t = int(input("Masukkan tingginya :  "))
            L = sBawah*t
            print("L = alas * tinggi")
        elif (indeks == 4):
            print("Luas Trapesium")
            sBawah = int(input("Masukkan panjang alasnya :   "))
            sAtas = int(input("Masukkan panjang sisi atasnya :   "))
            t = int(input("Masukkan tingginya :  "))
            L = .5*(sBawah+sAtas)*t
            print("L = 1/2 * (alas + sisiAtas) * tinggi")
        elif (indeks == 5):
            print("Luas Belah Ketupat")
            d1 = int(input("Masukkan panjang diagonal1 :     "))
            d2 = int(input("Masukkan panjang diagonal2 :     "))
            L = d1*d2*.5
            print("L = 1/2 * diagonal1 * diagonal2")
        elif (indeks == 6):
            print("Luas Layang-layang")
            d1 = int(input("Masukkan panjang diagonal1 :     "))
            d2 = int(input("Masukkan panjang diagonal2 :     "))
            L = d1*d2*.5
            print("L = 1/2 * diagonal1 * diagonal2")
        elif (indeks == 7):
            print("Luas Segitiga")
            sBawah = int(input("Masukkan panjang alasnya :   "))
            t = int(input("Masukkan tingginya :  "))
            L = .5*sBawah*t
            print("L = 1/2 * alas * tinggi")
        elif (indeks == 8):
            print("Luas Lingkaran")
            pi = 3.14593
            r = int(input("Masukkan panjang jari-jarinya :   "))
            L = pi*r*r
            print("L = pi * jari-jari^2")
        print("Luas = ", L, "cm^2")    

    #KELILING
    elif (pil == "KELILING"):
        if   (indeks == 1):
            print("Keliling Persegi")
            s = int(input("Masukkan panjang sisinya :   "))
            K = 4*s
            print("K = sisi + sisi + sisi + sisi")
        elif (indeks == 2):
            print("Keliling Persegi panjang")
            p = int(input("Masukkan panjangnya :    "))
            l = int(input("Masukkan lebarnya :   "))
            K = 2*(p+l)
            print("K = 2 * (panjang + lebar)")    
        elif (indeks == 3):
            print("Keliling Jajar genjang")
            sBawah = int(input("Masukkan panjang alasnya :   "))
            sMiring = int(input("Masukkan panjang sisi miringnya :  "))
            K = 2*(sBawah+sMiring)
            print("K = 2 * (sisiBawah + sisiMiring)")
        elif (indeks == 4):
            print("Keliling Trapesium")
            sBawah = int(input("Masukkan panjang alasnya :   "))
            sAtas = int(input("Masukkan panjang sisi atasnya :   "))
            sKanan = int(input("Masukkan panjang sisi kanannya :    "))
            sKiri = int(input("Masukkan panjang sisi Kirinya :    ")) 
            K = sAtas+sKiri+sKanan+sBawah
            print("K = sAtas+sKiri+sKanan+sBawah")
        elif (indeks == 5):
            print("Keliling Belah Ketupat")
            s = int(input("Masukkan panjang sisinya :   "))
            K = 4*s
            print("K = sisi + sisi + sisi + sisi")
        elif (indeks == 6):
            print("Keliling Layang-layang")
            s1 = int(input("Masukkan panjang sisi1 :     "))
            s2 = int(input("Masukkan panjang sisi2 :     "))
            K = 2*(s1+s2)
            print("K = 2 * sisi1 * sisi2")
        elif (indeks == 7):
            print("Keliling Segitiga")
            s1 = int(input("Masukkan panjang sisi1 :     "))
            s2 = int(input("Masukkan panjang sisi2 :     "))
            s3 = int(input("Masukkan panjang sisi3 :     "))
            K = s1+s2+s3
            print("K = s1 + s2 + s3")
        elif (indeks == 8):
            print("Keliling Lingkaran")
            pi = 3.14593
            r = int(input("Masukkan panjang jari-jarinya :   "))
            K = 2*pi*r
            print("K = 2 * pi * jari-jari")
        print("Keliling = ", K, "cm")

    #JIKA YANG DIINPUT BUKAN (LUAS dan KELILING)
    else:
        print("\n\nInput Anda Salah!,\nUlangi!!!")
        continue

    #===Ulangi===
    ulangi = input("\n\nUlangi?  (YA / TIDAK) (Dalam huruf Kapital)! :   ")
    #YA
    if (ulangi == "YA"):
        pass    
    #TIDAK
    elif (ulangi == "TIDAK"):
            print("\nTerima Kasih!\n\n")
            kerjakan = False
    #JIKA YANG DIMASUKKAN BUKAN(YA/TIDAK)
    else:
            print("\n\nInput yang anda Masukkan salah!")
            kerjakan = False
    