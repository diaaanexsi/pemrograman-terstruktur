def sum(*semuaAngka):
    hasil=0
    for angka in semuaAngka:
        hasil+=angka
    return hasil
def average(*semuaAngka):
    x=0
    for angka in semuaAngka:
        x+=1
    return sum(*semuaAngka)/x
def maks(*semuaAngka):
    max=semuaAngka[0]
    for angka in semuaAngka:
        if (angka>max):
            max=angka
    return max
def min(*semuaAngka):
    min=semuaAngka[0]
    for angka in semuaAngka:
        if (angka<min):
            min=angka
    return min
