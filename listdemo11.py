list1=["apple","banana","cherry"]
print(list1)
x=type(list1)
print(x)
print(list1[0])
print(list1[2])
list1[0]="grapes"
print(list1)
for x in list1:
    print(x)
list1.insert(2,"orange")
print(list1)
list1.remove("orange")
print(list1)
list1.pop()
print(list1)
list1.clear()
print(list1)
