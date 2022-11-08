n=int(input("enter number of elements"))
print("enter the elements")
list=[]
for i in range(0,n):
    ele=int(input())
    if ele>100:
        list.append('Over')
    else:
        list.append(ele)

print(list)