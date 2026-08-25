
n=int(input("Enter N: "))

L=[]

for i in range(n):
    temp=int(input())
    L.append(temp)

L_even=[]
L_odd=[]
for i in range(len(L)):
    if L[i]%2==0:
        L_even.append(L[i])
    else:
        L_odd.append(L[i])

print(L)
print(L_even)
print(L_odd)