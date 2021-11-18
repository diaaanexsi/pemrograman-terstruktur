try:
    n=int(input("jumlah data:"))
    print
    data=[]
    p=0
    while p<n:
        e=input('Masukkan data ke-:%s\n' %(p+1))
        data.append(e)
        p+=1
    data.sort()
    print('\nUrutan bilangan dari kecil ke besar:',data)
    for e in data:
        print("{0} ({1}karakter)".format(e,len(tuple(e))))

except ValueError:
    print('\nData salah')


