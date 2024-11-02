#ini adalah game angka random
import os
import random

def clear():
    os.system('cls')

def garis ():
    print ('='*45)

def cover():
    garis ()
    print ('\n\n             Game Angka Random\n\n')
    garis()

def maingame ():
    global pengulangan
    clear()
    cover()
    bil = random.randint(1,100)
    pengulangan = 7
    while pengulangan > 0 :
        tebakan = int(input('masukkan angka tebakan : '))
        if tebakan > bil :
            pengulangan -= 1
            print ('angka tebakan terlalu besar')
            print (f'tersisa {pengulangan} pengulangan lagi')
            if pengulangan == 0 :
                a = input ('mau main lagi ? ya[y] tidak[t]')
                if  a == 'y':
                    maingame()
                if a == 't':
                    print ('terima kasih telah bermain')                   
        elif tebakan < bil :
            pengulangan -=1
            print ('angka tebakan terlalu kecil')
            print (f'tersisa {pengulangan} kesempatan lagi')
            if pengulangan == 0 :
                a = input ('mau main lagi ? ya[y] tidak[t]')
                if  a == 'y':
                    maingame()
                if a == 't':
                    print ('terima kasih telah bermain')                   
        elif tebakan == bil :
            pengulangan -= 1
            print ('selamat tebakan anda benar')
            menang = input('mau main lagi : ya [y] tidak [t]')
            while True :
                if menang == 'y':
                    clear()
                    maingame()
                    break
                elif menang == 't' :
                    clear ()
                    break
            break
            

if __name__ =="__main__":
    maingame ()



