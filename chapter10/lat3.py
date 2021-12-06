#baca file datamhs

data=open('datamhs.txt','r')

myList=[]

myData=data.readlines()

for i in range (len(myData)):
    pisah=myData[i].split('|')
    Dict={'nim':pisah[0],'nama':pisah[1],'alamat':pisah[2]}
    myList.append(Dict)

print(myList)


data.close()
