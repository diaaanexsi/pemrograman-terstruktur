a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print('data a awal',a)
print('data b awal',b)
a.insert(3, 10)
b.insert(2,15)
print('\nlalu pada list a disisipkan angka 10 pada indeks ke 3',a)
print('dan pada list b disisipkan angka 15 pada indeks ke 2',b)
a.append(4)
b.append(8)
print('\npada list a indeks terakhir ditambahkan angka 4',a)
print('dan pada list b indeks terakhir ditambahkan angka 8',b)
a.sort()
b.sort()
print('\nsorting ascending pada list a',a)
print('sorting ascending pada list b',b)
c=list(a[:8])
d=list(b[2:10])
print('\nyang merupakan sublist dari a (indeks 0 s/d 7) adalah c =',c)
print('yang merupakan sublist dari b (indeks 2 s/d 9) adalah d =',d)
e=[]
for p in range (len(c)):
    e+=[c[p]+d[p]]
print('\nhasil dari penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya adalah',e)
e=tuple(e)
print('\nmengubah bentuk list e menjadi tuple',e)

print ('nilai minimal dari e adalah',min(e))
print ('nilai maksimal dari e adalah',max(e))
print ('jumlahan seluruhnya dari e adalah',sum(e))

myString="python adalah bahasa pemrograman yang menyenangkan"
setmyString=set(myString)
print('\nsebuah string adalah',myString)
print('karakter huruf yang menyusun string adalah',setmyString)

setStringList=list(setmyString)
print('\nbentuk list dari myString\n',setStringList)
setStringList.sort()
print('sorting ascending alfabet himpunan karakter huruf dari myString\n',setStringList)
