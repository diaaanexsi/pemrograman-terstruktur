#cari data peminjaman
from datetime import*


def getTerlambat(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return int((now - x).days)

cari=input('masukkan kode member yang dicari:')

data=open('data2.txt','r')

hasil= False

for file in data:
    databaru=file.split('|').copy()
    kode=file.split('|')[0]
    if(kode==cari):
        hasil=databaru
        break

if(hasil):
    maksPinjam = hasil[4].rstrip('\n')
    terlambat = getTerlambat(maksPinjam)

    if(terlambat <= 0):
        textTerlambat = "Tidak Terlambat"
        denda         = "Tidak Ada Denda"
    elif(terlambat > 0):
        textTerlambat = str(terlambat) + " hari"
        denda         = "Rp " + str(terlambat*2000)
        
    print('Data Peminjaman Buku')
    print('Kode Member               :',hasil[0])
    print('Nama Member               :',hasil[1])
    print('judul buku                :',hasil[2])
    print('Tanggal mulai meminjam    :',hasil[3])
    print('Tanggal maks pengembalian :',maksPinjam)
    print('Terlambat                 :',datetime.date(datetime.now()))
    print('Denda                     :',denda)
    
else:
    print('Data Mahasiswa tidak ditemukan')
    
data.close()
