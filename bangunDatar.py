import math
import os
from time import sleep
import turtle
from turtle import *



def gambarPersegi():
    # Persegi
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    begin_fill()    
    turtle.forward(100)
    turtle.left(90)
    end_fill() 
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(100)
    turtle.write('sisi', move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(100)
    turtle.write("\n\nsisi", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    end_fill()

    turtle.color("#222831")
    begin_fill()    
    turtle.forward(15)
    end_fill() 

    return turtle



def gambarPersegiPanjang():
    # Persegi Panjang
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    begin_fill()    
    turtle.forward(150)
    turtle.left(90)
    end_fill() 
    turtle.color("#ffd369", "#222831")
    begin_fill()    
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    end_fill()

    turtle.color("#222831")
    begin_fill()    
    turtle.forward(15)
    end_fill() 

    return turtle



def gambarJajarGenjang():
    # JAJAR GENJANG

    turtle.bgcolor("#393e46")

    turtle.color("#393e46")
    begin_fill()    
    turtle.goto(0, -50)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))        
    turtle.goto(105, -50)
    turtle.goto(-195, -50)
    turtle.goto(-150, 0)
    turtle.write("Sisi Miring  ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    turtle.goto(195, 50)
    turtle.goto(105, -50)
    turtle.goto(-105, -50)
    turtle.goto(-105, 0)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    end_fill()

    return turtle




def gambarTrapesium():
    # TRAPESIUM
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write(" Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.goto(120, 0)
    turtle.goto(120, 60)
    turtle.write("Tinggi ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(0, 150)
    turtle.write(" Sisi Atas", move=False, align = "center", font=("Arial", 13, "italic"))
    turtle.goto(-120, 150)
    turtle.goto(-120, 75)
    # turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-120, 0)
    turtle.goto(210, 0)
    turtle.goto(165, 75)
    turtle.write(" Sisi Miring", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(-120, 150)
    turtle.goto(-165, 75)
    turtle.write("Sisi Miring ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-210, 0)

    turtle.goto(120, 0)
    end_fill()

    return turtle



def gambarBelahKetupat():
    #BELAH KETUPAT
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("      Diagonal 1", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(150, 0)
    turtle.goto(-150, 0)
    turtle.goto(-75, 100)
    turtle.write("Sisi 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, 200)
    turtle.goto(0, -85)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, -200)
    turtle.goto(75, -100)
    turtle.write("     Sisi 2 ", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(150, 0)
    turtle.goto(75, 100)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 200)
    turtle.goto(0, -200)
    turtle.goto(-75, -100)
    turtle.write("Sisi 4    ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(-150, 0)
    end_fill()

    return turtle




def gambarLayangLayang():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46")
    begin_fill()
    turtle.goto(50, 0)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.goto(50, 120)
    turtle.goto(50, -120)
    turtle.goto(50, -50)
    turtle.write("Diagonal 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, 0)
    turtle.goto(155, 0)
    turtle.goto(0, 0)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-155, 0)
    turtle.goto(-52.5, -60)
    turtle.write("Sisi 1      ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, -120)
    turtle.goto(102.5, -60)
    turtle.write("      Sisi 2", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(155, 0)
    turtle.goto(50, 120)
    turtle.goto(-155, 0)
    end_fill()

    return turtle




def gambarSegitiga():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46", "white")
    begin_fill()
    turtle.goto(0, -50)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("Sisi 1 (Alas) ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(-120, -50)
    turtle.goto(-60, 55)
    turtle.write("Sisi 2 ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)
    turtle.goto(60, 55)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(0, -50)
    turtle.goto(0, 50)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)

    return turtle




def gambarLingkaran():
    #Lingkaran
    turtle.bgcolor("#393e46")

    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.circle(100)
    turtle.left(90)   
    turtle.goto(0, 50)
    turtle.write(" Jari-Jari", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 100)
    turtle.left(180)
    turtle.forward(100)
    end_fill()

    return turtle
    


    


def persegi():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi")
                salah = True
                while(salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    else:
                        L = s * s 
                        print("L = sisi * sisi")
                        print("L =", s, "*", s)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False                            
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarPersegi()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    # EROR = False
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegi()
                        done()
                        # EROR = False
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarPersegi()
                            done()
                            # EROR = False
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarPersegi()
                            done()
                            # EROR = False
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K =", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm\n".format(K))
                        salah = False    
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarPersegi()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    # EROR = False
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegi()
                        done()
                        # EROR = False
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarPersegi()
                            done()
                            # EROR = False    
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarPersegi()
                            done()
                            # EROR = False
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def persegiPanjang():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    else:
                        L = p * l
                        print("L = panjang * lebar")
                        print("L =", p, "*", l)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarPersegiPanjang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    # EROR = False
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegiPanjang()
                        done()
                        # EROR = False
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarPersegiPanjang()
                            done()
                            # EROR = False    
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarPersegiPanjang()
                            done()
                            # EROR = False
                return L   
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    else:
                        K = 2 * (p + l)
                        print("K = 2 * (panjang + lebar)")
                        print("K = 2 *", "(", p, "+", l, ")")  
                        print("Keliling = {} cm\n".format(K))    
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarPersegiPanjang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    # EROR = False
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegiPanjang()
                        done()
                        # EROR = False
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarPersegiPanjang()
                            done()
                            # EROR = False    
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarPersegiPanjang()
                            done()
                            # EROR = False
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def jajarGenjang():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):    "))
                    t = int(input("Masukkan tingginya       (cm):    "))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    else:                        
                        L = sBawah * t
                        print("L = alas * tinggi")
                        print("L =", sBawah, "*", t)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarJajarGenjang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    # EROR = False
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarJajarGenjang()
                        done()
                        # EROR = False
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarJajarGenjang()
                            done()
                            # EROR = False    
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarJajarGenjang()
                            done()
                            # EROR = False
                return L  
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya        (cm):    "))
                    sMiring = int(input("Masukkan panjang sisi miringnya (cm):    "))
                    if (sBawah == 0 and sMiring == 0):
                        print("Ups, Panjang alas dan Sisi miring tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sMiring == 0):
                        print("Ups, Sisi Miring tidak boleh 0!!")
                    else:
                        K = 2 * (sBawah + sMiring)
                        print("K = 2 * (sisiBawah + sisiMiring)")
                        print("K = 2 * (", sBawah, "+", sMiring, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False 
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarJajarGenjang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarJajarGenjang()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarJajarGenjang()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarJajarGenjang()
                            done()
        
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def trapesium():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang alasnya      (cm):    "))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):    "))
                    t = int(input("Masukkan tingginya            (cm):    "))
                    if (sBawah == 0 and sAtas == 0 and t == 0):
                        print("Ups, Panjang alas, Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif(sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang alas, Sisi atas, tidak boleh 0!!")
                    elif (sAtas == 0 and t == 0):
                        print("Ups, Panjang Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    else:
                        L = .5 * (sBawah + sAtas) * t
                        print("L = 1/2 * (alas + sisiAtas) * tinggi")
                        print("L = 1/2 * (", sBawah, "+", sAtas, ")", "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False 
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarTrapesium()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True
                    
                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarTrapesium()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarTrapesium()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarTrapesium()
                            done()
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang sisi alasnya (cm):\t"))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):\t"))
                    sKanan = int(input("Masukkan panjang sisi kanannya (cm):\t"))
                    sKiri = int(input("Masukkan panjang sisi Kirinya (cm):\t")) 
                    if (sBawah == 0 and sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang Alas, sisi Atas tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Kanan tidak boleh 0!!" )
                    elif (sBawah == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan):
                        print("Ups, Panjang sisi Atas, sisi Kanan tidak boleh 0!!" )
                    elif (sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (sKanan == 0):
                        print("Ups, Panjang Sisi Kanan tidak boleh 0!!")
                    elif (sKiri == 0):
                        print("Ups, Panjang Sisi Kiri tidak boleh 0!!")
                    K = sAtas + sKiri + sKanan + sBawah
                    print("K = sAtas+sKiri+sKanan+sBawah")
                    print("K =", sAtas, "+", sKiri, "+", sKanan, "+", sBawah)
                    print("Keliling = {} cm".format(K))
                    salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarTrapesium()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarTrapesium()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarTrapesium()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarTrapesium()
                            done()
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")




def belahKetupat():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Belah Ketupat")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):     "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):     "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    else:
                        L = .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False 
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarBelahKetupat()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarBelahKetupat()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarBelahKetupat()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarBelahKetupat()
                            done()
                  
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Belah Ketupat")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K = ", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm".format(K))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarBelahKetupat()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarBelahKetupat()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarBelahKetupat()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarBelahKetupat()
                            done()
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def layangLayang():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Layang-layang")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):    "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):    "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    else:     
                        L =  .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False  
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarLayangLayang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLayangLayang()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarLayangLayang()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarLayangLayang()
                            done()
                  
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Layang-layang")
                salah = True
                while(salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    if (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")    
                    else:
                        K = 2 * (s1 + s2)
                        print("K = 2 * (sisi1 + sisi2)")
                        print("K = 2 * (", s1, "+", s2, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarLayangLayang()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLayangLayang()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarLayangLayang()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarLayangLayang()
                            done()
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
   

    


def segitiga():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Segitiga")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
                    t = int(input("Masukkan tingginya (cm):\t"))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    else:
                        L = .5 * sBawah * t
                        print("L = 1/2 * alas * tinggi")
                        print("L = 1/2 *", sBawah, "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarSegitiga()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarSegitiga()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarSegitiga()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarSegitiga()
                            done()
                  
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Segitiga")
                salah = True
                while (salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    s3 = int(input("Masukkan panjang sisi3 (cm):     "))
                    if (s1 == 0 and s2 == 0 and s3 == 0):
                        print("Panjang Sisi 1, Sisi 2, dan Sisi 3 tidak boleh nol")
                    if (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    if (s1 == 0 and s3 == 0):
                        print("Panjang Sisi 1 & Sisi 3 tidak boleh nol")
                    if (s2 == 0 and s3 == 0):
                        print("Panjang Sisi 2 & Sisi 3 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")
                    elif (s3 == 0):
                        print("Panjang Sisi 3 tidak boleh nol")
                    else:
                        K = s1 + s2 +s3
                        print("K = s1 + s2 + s3")
                        print("K =", s1, "+", s2, "+", s3)
                        print("Keliling = {} cm".format(K))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarSegitiga()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarSegitiga()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarSegitiga()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarSegitiga()
                            done()
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

   


def lingkaran():
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if (r == 0):
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    else:
                        L = math.pi * r**2
                        print("L = π * jari-jari^2")
                        print("L = 3.141592 *", r**2)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarLingkaran()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLingkaran()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarLingkaran()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarLingkaran()
                            done()
                  
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if (r == 0):
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    else:
                        K = 2 * math.pi * r
                        print("K = 2 * π * jari-jari")
                        print("K = 2 * 3.141592 *", r)
                        print("Keliling = {} cm".format(K))
                        salah = False
                try:
                    turtle.TurtleScreen._RUNNING = True
                    gambarLingkaran()
                    done()
                    turtle.TurtleScreen._RUNNING = True
                    # turtle.bye()
                    # turtle.TurtleScreen._RUNNING = True

                except turtle.Terminator:
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLingkaran()
                        done()
    
                    except turtle.Terminator:
                        try:
                            turtle.TurtleScreen._RUNNING = True
                            gambarLingkaran()
                            done()
            
                        except turtle.Terminator:
                            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                            turtle.resetscreen()
                            gambarLingkaran()
                            done()
                  
                return K    
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    

kerjakan = True
while(kerjakan):
    user = ""
    while (user == ""):
        user = input("\n\nMasukkan Nama anda :    ")
    print("\n\t\t\tSelamat datang!,  {}".format(str.capitalize(user)))
    print("\t\t//====================================================\\\\")
    print("\t\t|| \t\t\t\t\t\t  === ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t|| Aplikasi Penghitung Luas dan Keliling Bangun datar ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t\\\\=========================||=========================//\n\n")
    print("[1] Persegi\t\t||")
    print("[2] Persegi panjang\t||")
    print("[3] Jajar Genjang\t||")
    print("[4] Trapesium\t\t||")
    print("[5] Belah Ketupat\t||")
    print("[6] Layang-Layang\t||")
    print("[7] Segitiga\t\t||")
    print("[8] Lingkaran\t\t||")

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
        pil = input("LUAS / KELILING? :    ")
        if (str.upper(pil) == "LUAS" or str.upper(pil) == "KELILING"):
            EROR = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[indeks-1]))
        else:
            print("Input anda salah!")
            


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


        #=====================File Handling=======================

    file_history = open("history.txt", "a")

    if (str.upper(pil) == "LUAS"):
        history = "\nNama :{}\n{}, {}, {}cm^2\n-------".format(str.capitalize(user), bangun[indeks-1], str.capitalize(pil), hasil)
    elif(str.upper(pil) == "KELILING"):
        history = "\nNama :{}\n{}, {}, {}cm\n-------".format(str.capitalize(user), bangun[indeks-1], str.capitalize(pil), hasil)

    file_history.write(history)
    file_history.close()

    EROR = True
    while(EROR):
        tampil = input("Apakah anda ingin Melihat History Penghitungan? (YA / TIDAK):    ")
        if (str.upper(tampil) == "YA"):
            # open
            file = open("history.txt", "r")
            file = file.read()
            print(file)        
            EROR = False

        elif (str.upper(tampil) == "TIDAK"):
            EROR = False
            
        else:
            print("Input anda salah")
            continue


    


        #=====================Ulangi=======================


    EROR = True
    while (EROR):
        ulangi = input("\n\nUlangi?  (YA / TIDAK)!:   ")

        if (str.upper(ulangi) == "YA"): #YA
            while(EROR):
                clr = input("Apakah Anda ingin Membersihkan layar? (BERSIHKAN / TIDAK):    ")
                if (str.upper(clr) == "BERSIHKAN"):
                    print("\nSedang Membersihkan Layar ...")
                    sleep(1)
                    os.system('cls')
                    EROR = False
                elif (str.upper(clr) == "TIDAK"):
                    EROR = False
                else:
                    print("Input Anda Salah!!!")

        elif (str.upper(ulangi) == "TIDAK"): #TIDAK
                print("\nTerima Kasih!\n\n")
                EROR = False
                kerjakan = False
                salah = True
                while (salah):
                    delete = input("Apakah anda ingin Menghapus History? (YA / TIDAK):    ")
                    if (str.upper(delete) == "YA"):
                        os.remove("history.txt")
                        print("History telah terhapus!")       
                        EROR = False
                        salah = False
                        print("\nTerima Kasih!\n\n")
                    elif (str.upper(delete) == "TIDAK"):
                        salah = False
                        print("\nTerima Kasih!\n\n")
                    else:
                        print("Input anda salah!")
                    
        else:
            print("Input anda salah!!!")
