a=int(input("Enter number: "))
b=int(input("Enter number: "))
print(f"Before swapping a:{a},b:{b}")
# using extra variable
temp=a
a=b
b=temp
# using python syntax
a,b=b,a
# No extra variable
a=a+b
b=a-b
a=a-b
print(f"After swapping a:{a},b:{b}")

