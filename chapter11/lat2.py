#INPUT file peminjam buku

from datetime import*

data=open('data2.txt','w')
List=[]

while True:
    kode=input('masukan kode member:')
    nama=input('masukan nama member:')
    judul=input('masukan judul buku:')
    now=datetime.date(datetime.now())
    due=now+timedelta(days=7)
    myString=kode+'|'+nama+'|'+judul+'|'+str(now)+'|'+str(due)+'\n'

    data.write(myString)

    ans=input('apakah masih terdapat data yang harus diinput (y/n)?')
    if ans in ("N","n"):
        break


data.close()
