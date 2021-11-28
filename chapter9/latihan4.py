#shuflleString
def shuffleString(x,n):
    import random
    hasil=[]
    for p in range(n):
        acak=[]
#karena tidak boleh ada yang sama maka
        if acak not in hasil:
            acak=''.join(random.sample(x,len(x)))
            hasil+=[acak]
            p+=1
    print(hasil)

#diberikan
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)

    
