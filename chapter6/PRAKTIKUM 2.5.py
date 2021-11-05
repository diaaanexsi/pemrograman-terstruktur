def luasSegitiga(alas,tinggi):
    luas=alas*tinggi/2
    return luas

alas=10
tinggi=20
print("Luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah",luasSegitiga(alas,tinggi))

def luasSegitiga2(alas,tinggi):
    luas=alas*tinggi/2
    return luas

alas=15
tinggi=45
print("Luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah",luasSegitiga2(alas,tinggi))

def jumlah(luasSegitiga,luasSegitiga2):
    total= luasSegitiga + luasSegitiga2
    print( luasSegitiga, '+',luasSegitiga2,'=',total)

jumlah(100,337.5)
