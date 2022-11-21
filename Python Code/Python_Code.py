k='abcdefghijklmnopqrstuvwxyz1'
m=''
while m!="abcdefghijklmnopqrstuvwxyz":
    n=input()
    m=n
    if len(n)<len(k):
        k=n 
    
print(k)
