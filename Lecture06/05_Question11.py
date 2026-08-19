L=[]
for number in range(1000,3001):
    flag=True
    temp=number
    while temp!=0:
        digit=temp%10
        temp//=10
        if digit%2==1:
            flag=False
            break
    if flag:
        L.append(number)
print(L)

