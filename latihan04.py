# Deskriptif
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen  / 100
# print harga barang

while(True):
    nama_barang = input('Masukan nama barang :')
    harga_barang1 = int(input('Masukan harga barang :'))
    persen = 10
    harga_keuntungan = int(harga_barang1)*persen/100
    harga_jual = int(harga_barang1) + harga_keuntungan
    print(nama_barang, 'dijual dengan  :', harga_jual)

    apakahLanjut = input('Apakah ingin lanjut barang lain? Y Lanjut N tidak : ')
    if(apakahLanjut != 'Y'):
        break