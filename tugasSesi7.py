#
#
#

print('----------------------------------------------')
print('----------------- Latihan 7 ------------------')
print('----------------------------------------------')

print('----------------------------------------------')
print('-------- Program Kalkulator Sederhana --------')
print('----------------------------------------------')

while(True):
    print('=== Program Kalkulator ===')
    print('Menu')
    print(' 1. Hitung Luas Segitiga')
    print(' 2. Hitung Luas Persegi Panjang')
    print(' 3. Tentukan number Ganjil Genap')
    print(' 4. Quit')

    print('-----------------------------------------')

    listMenu = input('Masukan Pilihan : ')
    
    if listMenu == '1':
        print('Menu -- Hitung Luas Segitiga')
        alas = int(input('Masukan Panjang Alas : '))
        tinggi = int(input('Masukan Tinggi : '))

        rumus1 = 1/2 * alas * tinggi
        print('Luas Segitiga : ', rumus1)
        print('------------------------')

    elif listMenu == '2':
        print('Menu -- Hitung Luas Persegi Panjang')
        panjang = int(input('Masukan Panjang : '))
        lebar = int(input('Masukan Lebar : '))

        rumus2 = panjang * lebar
        print('Luas Persegi Panjang : ', rumus2)
        print('------------------------')

    elif listMenu == '3':
        print('Menu -- Tentukan number Ganjil Genap')
        angka = int(input('Masukan Angka : '))

        if (angka % 2 == 0) :
            print('Angka', angka, 'merupakan angka Genap')
        else:
            print('Angka', angka, 'merupakan angka Ganjil')
        print('------------------------')

    else:
        menu = input('Terimakasih')
        print('------------------')
        break
