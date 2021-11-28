mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("="*70)
print("NIM          NAMA MHS          TGL LAHIR          TEMPAT LAHIR")
print("-"*70)

for a in mhs:
    List=a.split(':')
    tgl=List[2]
    tglLahir=tgl[2]+'/'+tgl[1]+'/'+tgl[0]

    print(List[0].ljust(10), end='')
    print(List[1].ljust(20), end='')
    print(List[2].ljust(20), end='')
    print(List[3].ljust(10))

print('-'*70)
