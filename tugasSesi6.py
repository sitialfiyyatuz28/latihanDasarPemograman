while(True):
    print ('=== Program Grade Nilai ===')
    nama = (input('Masukan Nama         : '))
    jurusan = (input('Jurusan              : '))
    nilai = (input('Masukan Nilai Akhir  : '))

    if (nilai.isnumeric() == True) :
        nilai_int = int(nilai)
        if nilai_int >= 90 :
            grade = 'A'
            predikat = 'Dengan Pujian'
        elif nilai_int >= 80 :
            grade = 'B'
            predikat = 'Sangat Memuaskan'
        elif nilai_int >= 70 :
            grade = 'C'
            predikat = 'Memuaskan'
        elif nilai_int >= 60 :
            grade = 'D'
            predikat = 'Tidak Memuaskan'
        elif nilai_int >= 0 :
            grade = 'E'
            predikat = 'Tidak LULUS'
        print('======================')
        print('======================')
        print('Grade Anda : %s' %grade)
        print('Predikat   : %s ' %predikat)
    else :
        print('Maaf Input Anda Salah')
    print('======================')
    print('======================')
    apakahLanjut = input('Apakah ingin lanjut barang lain? Y Lanjut N tidak : ')
    if(apakahLanjut != 'Y'):
        break