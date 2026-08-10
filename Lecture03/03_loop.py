# print('12 *1=',12*1)
# print('12 *2=',12*2)
# print('12 *3=',12*3)
# print('12 *4=',12*4)
# print('12 *5=',12*5)
# print('12 *6=',12*6)


number=int(input('Enter number: '))

i=2
while i<11:
    print(number,'*',i,'=',number*i)
    i+=2
print("Loop ended")

# print all even number between 1 to 100

i=2
while i<=100:
    print(i)
    i+=2

# Factorial

n=int(input('Enter factorial: '))

ans=1

while n>0:
    ans*=n
    n-=1
print(ans)

ans=1
a=int(input())
b=int(input())
while b>0:
    ans*=a
    b-=1
print("Power is ",ans)