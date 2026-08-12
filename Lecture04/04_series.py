n=int(input("Enter n: "))

fact=1
result=0
for i in range(1,n+1):
    fact*=i
    result+=i/fact
print(result)
