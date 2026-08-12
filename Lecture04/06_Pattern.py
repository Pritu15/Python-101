"""
Pattern-01
*
**
***
****
*****
"""

n=int(input("Enter n: "))

for i in range(1,n+1):
    print("*"*i)
"""
Pattern-02
row=4
col=2
**
**
**
**
"""
row=int(input("Enter row: "))
col=int(input("Enter col: "))
for r in range(row):
    for c in range(col):
        print("*",end="")
    print()


"""
Pattern-03
n=4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

"""
n=int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()


"""
Pattern-04
n=4
A B C D
A B C D
A B C D
A B C D


"""

n=int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64),end=" ")
    print()


"""
Pattern-08
n=4
1
1 2 
1 2 3
1 2 3 4

"""
n=int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()