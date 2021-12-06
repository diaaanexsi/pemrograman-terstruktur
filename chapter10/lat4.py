#cari file datamhs

cari=input('masukkan nim yang dicari:')

data=open('datamhs.txt','r')

hasil= False

for file in data:
    databaru=file.split('|').copy()
    nim=file.split('|')[0]
    if(nim==cari):
        hasil=databaru
        break

if(hasil):
    print('Data Mahasiswa')
    print('NIM        :', hasil[0])
    print('Nama       :',hasil[1])
    print('alamat     :',hasil[2])
else:
    print('Data Mahasiswa tidak ditemukan')
data.close()
