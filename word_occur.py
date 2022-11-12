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
