jumlahKueKeju = 25
jumlahKueCoklat = 35
kueKeju = 6000
kueCoklat = 3500
kueKejuAda = True
kueCoklatAda = True


while (kueKejuAda or kueCoklatAda):

    if(kueKejuAda):
        beliKueKeju = int(input("Berapa Kue Keju yang Ingin anda Beli? (Jika tidak ada tulis 0):    "))
    if (kueCoklatAda):
        beliKueCoklat = int(input("Berapa Kue Coklat yang Ingin anda Beli? (Jika tidak ada tulis 0):    "))

    if (jumlahKueKeju >= beliKueKeju):
        if (beliKueKeju >= 4 and beliKueKeju <= 15):
            diskon = beliKueKeju * kueKeju * .1
            hargaKeju = beliKueKeju * kueKeju - diskon
            print("Total Harga Kue Keju = ", int(hargaKeju))
        elif (beliKueKeju >= 16 and beliKueKeju <= 25):
            diskon = beliKueKeju * kueKeju * .15
            hargaKeju = beliKueKeju * kueKeju - diskon
            print("Total Harga Kue Keju = ", int(hargaKeju))
        elif (beliKueKeju < 4):
            hargaKeju = beliKueKeju * kueKeju
            print("Total Harga Kue Keju = ", int(hargaKeju))

    elif (kueKejuAda and jumlahKueKeju < beliKueKeju):
        if (jumlahKueKeju >= 4 and jumlahKueKeju <= 15):
            diskon = beliKueKeju * kueKeju * .1
            hargaKeju = beliKueKeju * kueKeju - diskon
            print("Total Harga Kue Keju = ", int(hargaKeju))
        elif (jumlahKueKeju >= 16 and jumlahKueKeju <= 25):
            diskon = beliKueKeju * kueKeju * .15
            hargaKeju = beliKueKeju * kueKeju - diskon
            print("Total Harga Kue Keju = ", int(hargaKeju))
        elif (jumlahKueKeju < 4):
            hargaKeju = beliKueKeju * kueKeju
            print("Total Harga Kue Keju = ", int(hargaKeju))


    
    if (jumlahKueCoklat >= beliKueCoklat):
        if (beliKueCoklat >= 5 and beliKueCoklat <= 20):
            diskon = beliKueCoklat * kueCoklat * .07
            hargaCoklat = beliKueCoklat * kueCoklat - diskon
            print("Total Harga Kue Coklat = ", int(hargaCoklat))
        elif (beliKueCoklat >= 21 and beliKueCoklat <= 35):
            diskon = beliKueCoklat * kueCoklat * .12
            hargaCoklat = beliKueCoklat * kueCoklat - diskon
            print("Total Harga Kue Coklat = ", int(hargaCoklat))
        elif (beliKueCoklat < 5):
            hargaCoklat = beliKueCoklat * kueCoklat
            print("Total Harga Kue Coklat = ", int(hargaCoklat))

    elif(kueCoklatAda and jumlahKueCoklat < beliKueCoklat):
        if (jumlahKueCoklat >= 5 and jumlahKueCoklat <= 20):
            diskon = beliKueCoklat * kueCoklat * .07
            hargaCoklat = beliKueCoklat * kueCoklat - diskon
            print("Total Harga Kue Coklat = ", int(hargaCoklat))
        elif (jumlahKueCoklat >= 21 and jumlahKueCoklat <= 35):
            diskon = beliKueCoklat * kueCoklat * .12
            hargaCoklat = beliKueCoklat * kueCoklat - diskon
            print("Total Harga Kue Coklat = ", int(hargaCoklat))
        elif (jumlahKueCoklat < 5):
            hargaCoklat = beliKueCoklat * kueCoklat
            print("Total Harga Kue Coklat = ", int(hargaCoklat))


    jumlahYangHarusDibayar = hargaKeju + hargaCoklat
    print("Total yang Harus anda bayar adalah = ", int(jumlahYangHarusDibayar))
    hargaKeju = hargaCoklat = 0


    tempKueKeju = jumlahKueKeju
    jumlahKueKeju -= beliKueKeju
    if (jumlahKueKeju == 0):
        print("Kue Keju Habis!")
        kueKejuAda = False
    elif (jumlahKueKeju > 0):
        print("Kue Keju yang tersisa tinggal = ", jumlahKueKeju)
    elif (kueKejuAda and jumlahKueKeju < 0):
        print("Maaf, Kue Keju Kami tidak cukup, Kami kekurangan {} Kue Keju, kami hanya menjual sebanyak {} buah". format(-jumlahKueKeju, tempKueKeju))
        kueKejuAda = False
        
    tempKueCoklat = jumlahKueCoklat
    jumlahKueCoklat -= beliKueCoklat
    if (jumlahKueCoklat == 0):
        print("Kue Coklat Habis!")
        kueCoklatAda = False
    elif (jumlahKueCoklat > 0):
        print("Kue Coklat yang tersisa tinggal = ", jumlahKueCoklat)
    elif (kueCoklatAda and jumlahKueCoklat < 0):
        print("Maaf, Kue Coklat Kami tidak cukup, Kami kekurangan {} Kue Coklat, kami hanya menjual sebanyak {} buah" .format(-jumlahKueCoklat, tempKueCoklat))
        kueCoklatAda = False


    print("----------------------")
