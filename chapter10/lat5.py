#hasil jumlah file bilA

data=open('bilA.txt','r')
hasilData=open('hasilbilA.txt','w')

read=data.readlines()

for p in range(len(read)):
    hasil=read[p].replace('\n','')
    hasil2=hasil.split('|')
    hasilData.write (str(int(hasil2[0])+int(hasil2[1]))+'\n')


    
data.close()  
hasilData.close()
