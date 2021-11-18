n=int(input("jumlah data:"))
print
data=[]
p=0
while p<n:
    try:
        
        e=int(input('Masukkan data ke-%d: \n' % (p+1)))
        data.append(e)
        p+=1
        data.sort()
        print('\nUrutan bilangan dari kecil ke besar:',data)
    except ValueError:
        print('\nData salah')


    
