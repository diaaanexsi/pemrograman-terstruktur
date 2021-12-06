#membaca file

p=open("text lat1.txt","r")

ganjil=0
genap=0
for q in p:
    try:
        if (int (q)%2==0):
            ganjil+=1
        else:
            genap+=1
    except:
        print(q.rstrip("/n"),"bukan data")

              
print ('banyaknya bilangan genap:',genap)
print('banyaknya bilangan ganjil:',ganjil)

p.close()
