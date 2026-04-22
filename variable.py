n=input("enter a string   :")
a=""
c=len(n)
for i in range (c , 0 , -1):
    a=a+n[i-1]
print(a)
if n==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    
