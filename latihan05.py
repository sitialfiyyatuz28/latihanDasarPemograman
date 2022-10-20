# deskriptif
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen barang
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input('Masukan Nama Barang : ')
    harga_barang = int(input('Masukan Harga Barang : '))
    persen = int(input('Masukan Persen Barang : '))
    barang_terjual = int(input('Masukan Jumlah Barang Terjual : '))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    # menghitung modal
    modal = harga_barang * barang_terjual
    # menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    # menghitung laba
    laba = keuntungan_persen * barang_terjual
    # menghitung laba keseluruhan
    laba_keseluruhan = laba_keseluruhan + laba

    print('Barang                   :', nama_barang)
    print('Harga Barang             :', harga_barang)
    print('keuntungan per barang    :', keuntungan_persen)
    print('dijual dengan harga      :', harga_jual)
    print('terjual                  :', barang_terjual)
    print('modal                    :', modal)
    print('laba                     :', laba)

    apakahLanjut = input('Apakah ingin lanjut barang lain? Y Lanjut N tidak : ')
    if(apakahLanjut != 'Y'):
        break

print('---------')
print('modal keseluruhan    :', modal_keseluruhan)
print('laba keseluruhan     :', laba_keseluruhan)