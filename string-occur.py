# Get a string from an input string where all occurrences of first character replaced with '$' except first character [eg: onion->oni$n]
n=input("enter the string")
a=n[0]
for i in n:
    if i==a:
        n=n.replace(i,'$')
        n=a+n[1:]
print(n)