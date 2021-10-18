BahasaIndonesia= int(input("Masukkan nilai BahasaIndonesia:"))
IPA= int(input("Masukkan nilai IPA;"))
Matematika=int(input("Masukkan nilai Matematika:"))
if (BahasaIndonesia >= 0) and (BahasaIndonesia<=100) and (IPA >= 0) and (IPA<=100) and (Matematika>=0) and (Matematika<=100):
    if(BahasaIndonesia >= 60) and (IPA >= 60) and (Matematika>70):
        print("LULUS")
    elif(BahasaIndonesia <= 60) and (IPA <= 60) and (Matematika<70):
        print("TIDAK LULUS")
else:
    print("Maaf input tidak valid")
