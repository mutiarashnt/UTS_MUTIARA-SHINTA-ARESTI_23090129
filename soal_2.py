tahun = int(input('Masukkan Tahun : '))

def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 4 == 0 and tahun % 100 != 0:
        return False
    else:
        print('Bukan Tahun Kabisat')


print('Tahun ', tahun, 'merupakan TAHUN KABISAT')