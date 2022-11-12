line=input("Enter the line:")
counts={}
sentence=line.split()
print(sentence)
for word in sentence:
    if word in counts:
        counts[word] += 1

    else:
        counts[word]=1

for k,v in counts.items():
    print(k,v)
n=int(input("enter number of strings"))
print("enter the stings")
stringlist=[]
count=0

for i in range(0,n):
    ele=input()
    stringlist.append(ele)
print(stringlist)
for i in stringlist:
    for j in i:
        if j=='a':
            count=count+1
print(count)

dict={}
str1= input("Enter a string:")
for n in str1:
    if n in dict:
        dict[n]+=1
        print(dict)
    else:
        dict[n]=1
        print(dict)

print("Character frequency")
for k,v in dict.items():
    print(k,v)