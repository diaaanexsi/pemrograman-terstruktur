#INPUT file datamhs

data=open('datamhs.txt','a')

while True:
    nim=input('masukan nim:')
    nama=input('masukan nama:')
    alamat=input('masukan alamat:')

    myString=nim+'|'+nama+'|'+alamat+'\n'

    data.write(myString)

    ans=input('apakah masih terdapat data yang harus diinput (y/n)?')
    if ans in ("N","n"):
        break


data.close()
