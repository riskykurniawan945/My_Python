import time
import os
# data_nama = "barakatak"
# data_pw = "apd14"
b = 3
pesanan = []
total = 0

menu_makanan = ["NASI GORENG", "MIE GORENG", "AYAM GORENG"]
menu_minuman = ["TEH DINGIN", "ES JERUK ", "KOPI PANAS"]
harga_menu_makanan = [12000, 12000, 15000]
harga_menu_minuman = [4000, 5000, 5000]




def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def kasir():
    global total
    print("=== Kasir Warung Barakatak ===")
    nama = ''
    namakosong = True
    while (namakosong):
        nama = input("Masukkan nama Konsumen: ")
        if (nama == ''):
            print("Nama tidak boleh kosong!")
        else:
            namakosong = False
    print ("Nama Konsumen :", nama)
    print("")
    print('___________________MAKANAN_____________________\n')
    for i in range(len(menu_makanan)):
        print ("[" , (i+1) , "]", menu_makanan[i], "\t:\tRp.", harga_menu_makanan[i])
    print('_______________________________________________\n')
    print('___________________MINUMAN_____________________')
    for i in range(len(menu_minuman)):
        print ("[" , (i+1) , "]", menu_minuman[i], "\t:\tRp.", harga_menu_minuman[i])
    print('_______________________________________________\n')

    EROR = True
    while(EROR):
        try:   
            for i in range(len(menu_makanan)):
                pesan = int(input("Pesan berapa " + menu_makanan[i] + "\t:\t"))
                pesanan.append(pesan)
                print("Total: ", harga_menu_makanan[i], " x ", (pesan), " = Rp. ", (pesan) * harga_menu_makanan[i])
                total += harga_menu_makanan[i] * pesan
                print("Tagihan: Rp.", total)
            for i in range(len(menu_minuman)):
                pesan = int(input("Pesan berapa " + menu_minuman[i] + "\t:\t"))
                pesanan.append(pesan)
                print("Total: ", harga_menu_minuman[i], " x ", (pesan), " = Rp. ", (pesan) * harga_menu_minuman[i])
                total += harga_menu_minuman[i] * pesan
                print("Tagihan: Rp.", total)
            EROR = False
        except ValueError:
            print("Input anda salah, Masukkan Angka!")
            total = 0

    uangTidakCukup = True
    while(uangTidakCukup):
        try:    
            uang = int(input("Uang Tunai: Rp."))
            if uang > total:
                print("Kembalian: Rp.", uang - total)
                uangTidakCukup = False
            elif uang == total:
                print("Uang Anda Pas")
                uangTidakCukup = False
            else:
                print("UANG ANDA TIDAK CUKUP")
        except ValueError:
            print("Input anda salah, Masukkan Angka") 


    EROR = True
    while(EROR):
        cetak = str(input("\nCetak Struk? (y/n): "))
        if(cetak == "y"):
            print("\n=========================")
            print("======= S T R U K =======")
            print("=========================")
            print ("=== Nama      :",nama)
            for i in range(len(menu_makanan)):
                print ("=== Beli      :",pesanan[i],menu_makanan[i])
            for i in range(len(menu_minuman)):
                print ("=== Beli      :",pesanan[i],menu_minuman[i])
            print ("=== Tagihan\t:Rp.",total)
            print ("=== Uang\t:Rp.",uang)
            akhir=int(uang - total)
            if uang > total:
                print ("=== Kembalian\t:Rp.",akhir)
            elif uang == total:
                print("Uang Anda Pas")
            else:
                print("=== Anda Utang :Rp.",akhir)
            print("=========================")
            print("=========================")
            print("Terima Kasih Telah Makan di Warung Barakatak")
            print("Langganan Permanen ya Kak")
            EROR = False
            back_to_menu()
        elif(cetak == "n"):
            EROR = False
            back_to_menu()
        else:
            print("Pilihan kamu tidak tersedia!")


def tambah_menu():
    EROR = True
    while (EROR):
        try:
            new = input("Anda ingin menambahkan Makanan atau Minuman?:    ")
            tambah = input("Silahkan Masukkan nama menu yang ingin anda tambahkan!:    ")
            price = int(input("Berapa Harganya?:   "))
            if(str.upper(new) == "MAKANAN"):
                menu_makanan.append(str.upper(tambah))
                harga_menu_makanan.append(price)
                break
            elif(str.upper(new) == "MINUMAN"):
                menu_minuman.append(str.upper(tambah))
                harga_menu_minuman.append(price)
                break
            else:
                print("Input anda salah!")
        except ValueError:
            print("Input anda salah!")        
    show_menu()




def hapus_menu():
    print("")
    print('___________________MAKANAN_____________________\n')
    for i in range(len(menu_makanan)):
        print ("[" , (i+1) , "]", menu_makanan[i], "\t:\tRp.", harga_menu_makanan[i])
    print('_______________________________________________\n')
    print('___________________MINUMAN_____________________')
    for i in range(len(menu_minuman)):
        print ("[" , (i+1) , "]", menu_minuman[i], "\t:\tRp.", harga_menu_minuman[i])
    print('_______________________________________________\n')

    belum_hapus = True
    while(belum_hapus):
        hapus = input("\nAnda Ingin Menghapus Menu apa?:\t ")
        if (str.upper(hapus) in menu_makanan):
            menu_makanan.remove(str.upper(hapus))
            print(str.upper(hapus), "Telah dihapus!")
            time.sleep(1)
            belum_hapus = False
        elif (str.upper(hapus) in menu_minuman):
            menu_minuman.remove(str.upper(hapus))
            print(str.upper(hapus), "Telah dihapus!")
            time.sleep(1)
            belum_hapus = False
        else:
            print("Menu yang anda hapus tidak ada didalam daftar menu!")
    show_menu()


def ubah_harga():
    print("")
    print('___________________MAKANAN_____________________\n')
    for i in range(len(menu_makanan)):
        print ("[" , (i+1) , "]", menu_makanan[i], "\t:\tRp.", harga_menu_makanan[i])
    print('_______________________________________________\n')
    print('___________________MINUMAN_____________________')
    for i in range(len(menu_minuman)):
        print ("[" , (i+1) , "]", menu_minuman[i], "\t:\tRp.", harga_menu_minuman[i])
    print('_______________________________________________\n')

    harga_lama = True
    while(harga_lama):
        try:
            ubahmenu = input("\nAnda Ingin Mengubah Harga Makanan atau Minuman?:\t ")
            ubah = int(input("\nTulis Indeks Makanan yang ingin anda ubah!:\t "))
            if (str.upper(ubahmenu) == "MAKANAN"):
                print("Harga Awal\t=\t", harga_menu_makanan[ubah-1], "\n")
                ubah_harga = int(input("Harga Baru\t=\t"))
                harga_menu_makanan[ubah-1] = ubah_harga
                harga_lama = False
            elif (str.upper(ubahmenu) == "MINUMAN"):
                print("Harga Awal\t=\t", harga_menu_minuman[ubah-1], "\n")
                ubah_harga = int(input("Harga Baru\t=\t"))
                harga_menu_minuman[ubah-1] = ubah_harga
                harga_lama = False
        except ValueError:
            print("Input anda salah, masukkan angka!")
    show_menu()












def show_menu():
    print(100*"\n")
    print(' _____________________________________________')
    print('/                                             \ ')
    print('_______________________________________________')
    print("              MENU WARUNG BARAKATAK               ")
    print('_______________________________________________')
    print('___________________MAKANAN_____________________')
    for i in range(len(menu_makanan)):
        print ("[" , (i+1) , "]", menu_makanan[i])
    print('_______________________________________________')
    print('___________________MINUMAN_____________________')
    for i in range(len(menu_minuman)):
        print ("[" , (i+1) , "]", menu_minuman[i])
    print("\n-----------------------------------------------")
    print("\tAplikasi Kasir Warung Barakatak")
    print("-----------------------------------------------")
    print("[1] Kasir")
    print("[2] Ubah Harga")
    print("[3] Tambah Menu")
    print("[4] Hapus Menu")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu >>> "))

    if(selected_menu == "1"):
        kasir()
    if(selected_menu == "2"):
        ubah_harga()
    if(selected_menu == "3"):
        tambah_menu()
    if(selected_menu == "4"):
        hapus_menu()
    elif (selected_menu == "0"):
        print("-------------------------------------------------------------")
        print("\tTerima kasih telah menggunakan Aplikasi Kasir")
        print("-------------------------------------------------------------")
        time.sleep(3)
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        

show_menu()

