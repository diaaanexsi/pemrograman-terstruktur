data=[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
      {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
      {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
      {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
      {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print("="*80)
print("NIM          NAMA MHS          MID          UAS          N.AKHIR          STATUS")
print("-"*80)


for i in data:
    Akhir=(i['mid']+2*i['uas'])/3
    akhir=round(Akhir)
    if akhir >=60:
        Status='LULUS'
    else:
        Status='TIDAK LULUS'


    print(i['nim'].ljust(13), end='')
    print(i['nama'].ljust(17), end='')
    print(str(i['mid']).rjust(3), end='')
    print(str(i['uas']).rjust(13), end='')
    print(str(akhir).rjust(15), end='')
    print(str(Status).rjust(18))
print('='*80)
