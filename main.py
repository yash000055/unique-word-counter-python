# inputs=input("Enter the Paragraph : ")
p="hello you are very good and also you are smart"
newP=p.split()
uniquewords=[]
occurencesOfUniquewords=[]
count=0
for item in newP:
    if(newP.count(item)==1):
        uniquewords.append(item)
        count+=1

for items in newP:
    occurencesOfUniquewords.append(newP.count(items))

print((uniquewords))
print(count)
print(occurencesOfUniquewords)
