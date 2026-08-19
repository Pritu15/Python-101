n=int(input("Enter N: "))

is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
        print("Not Prime")
        break

if is_prime:
    print("Prime")
