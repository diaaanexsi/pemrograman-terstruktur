data=[{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
      {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
      {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
      {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
      {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print("="*47)
print("NIM          NAMA MHS          MID          UAS")
print("-"*47)

for i in range(len(data)):
    print(data[i]['nim'].ljust(13), end='')
    print(data[i]['nama'].ljust(17), end='')
    print(str(data[i]['mid']).rjust(3), end='')
    print(str(data[i]['uas']).rjust(13))
print('='*47)
