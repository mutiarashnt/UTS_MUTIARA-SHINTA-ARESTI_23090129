def total_1(a):
    return a
def total_2(a,b):
    return a + b
def total_3(a,b,c):
    return a + b + c
def total_4(a,b,c,d):
    return a + b + c + d
def total_5(a,b,c,d,e):
    return a + b + c + d + e
def total_6(a,b,c,d,e,f):
    return a + b + c + d + e + f


jumlah = int(input('Masukkan Jumlah Barang : '))
print('\n')
# harga1 = int(input('Masukkan Harga Barang ke-1 : '))
# harga2 = int(input('Masukkan Harga Barang ke-2 : '))
# harga3 = int(input('Masukkan Harga Barang ke-3 : '))
# harga4 = int(input('Masukkan Harga Barang ke-3 : '))
# harga5 = int(input('Masukkan Harga Barang ke-4 : '))
# harga6 = int(input('Masukkan Harga Barang ke-5 : '))


if jumlah == 1:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    print('Total Belanjaan Anda : Rp.', total_1(harga1))
elif jumlah == 2:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    harga2 = int(input('Masukkan Harga Barang ke-2 : '))
    print('Total Belanjaan Anda : Rp.', total_2(harga1,harga2))
elif jumlah == 3:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    harga2 = int(input('Masukkan Harga Barang ke-2 : '))
    harga3 = int(input('Masukkan Harga Barang ke-3 : '))
    print('Total Belanjaan Anda : Rp.', total_3(harga1,harga2,harga3))
elif jumlah == 4:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    harga2 = int(input('Masukkan Harga Barang ke-2 : '))
    harga3 = int(input('Masukkan Harga Barang ke-3 : '))
    harga4 = int(input('Masukkan Harga Barang ke-4 : '))
    print('Total Belanjaan Anda : Rp.', total_4(harga1,harga2,harga3,harga4))
elif jumlah == 5:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    harga2 = int(input('Masukkan Harga Barang ke-2 : '))
    harga3 = int(input('Masukkan Harga Barang ke-3 : '))
    harga4 = int(input('Masukkan Harga Barang ke-4 : '))
    harga5 = int(input('Masukkan Harga Barang ke-5 : '))
    print('Total Belanjaan Anda : Rp.', total_5(harga1,harga2,harga3,harga4,harga5))
elif jumlah == 6:
    harga1 = int(input('Masukkan Harga Barang ke-1 : '))
    harga2 = int(input('Masukkan Harga Barang ke-2 : '))
    harga3 = int(input('Masukkan Harga Barang ke-3 : '))
    harga4 = int(input('Masukkan Harga Barang ke-4 : '))
    harga5 = int(input('Masukkan Harga Barang ke-5 : '))
    harga6 = int(input('Masukkan Harga Barang ke-6 : '))
    print('Total Belanjaan Anda : Rp.', total_6(harga1,harga2,harga3,harga4,harga5,harga6))
else:
    print('Anda Telah Mencapai Batas Maksimum Pembelian Barang')




