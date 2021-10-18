BahasaIndonesia= int(input("Masukkan nilai BahasaIndonesia:"))
IPA= int(input("Masukkan nilai IPA;"))
Matematika=int(input("Masukkan nilai Matematika:"))
if (BahasaIndonesia >= 0) and (BahasaIndonesia<=100) and (IPA >= 0) and (IPA<=100) and (Matematika>=0) and (Matematika<=100):
    if(BahasaIndonesia >= 60) and (IPA >= 60) and (Matematika>70):
        print("LULUS")
    else:
        sebab = " "
        if (BahasaIndonesia <60):
            sebab += " -Nilai Bahasa Indonesia kurang dari 60\n"
        if(IPA<60):
            sebab += "-Nilai IPA kurang dari 60\n"
        if(Matematika<=70):
            sebab+= "-Nilai Matematika kurang dari sama dengan70\n"
        print("\n TIDAK LULUS")
        print("sebab:")
        print(sebab)
else:
    print("Maaf input tidak valid")
