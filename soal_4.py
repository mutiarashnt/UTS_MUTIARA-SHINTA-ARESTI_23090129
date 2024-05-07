def BMI(a,b):
    return a / b**2

berat = int(input('Masukkan Berat Badan (kg) : '))
tinggi = int(input('Masukkan Tinggi Badan (m) : '))

if BMI < 18.5:
    print('Berat Badan Kurang')
elif BMI <= 18.5 and < 24.9:
    print('Berat Badan Normal')
elif BMI <= 18.5 and < 24.9:
    print('Berat Badan Normal')
else:
    print('Obesitas')

