total=0
n=int(input("Enter N: "))
i=1
while total!=300:
    if i%5==0:
        continue
    if i>n:
        break
    total+=i