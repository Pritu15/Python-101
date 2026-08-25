# create a tuple
t1=()
print(t1)
t2=('hello',)
print(t2)
print(type(t2))
t3=tuple('hello')
print(t3)

#Access a tuple
t3=(1,2,3,4,5)

print(t3)
print(t3[-1])
print(t3[0:3:+2])

# Edit Add Delete Not possible

#Operations
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
print(t1*2)

print(4 in t2)
print(4 not in t2)

for i in  t1:
    print(i)

# Tuple functions len,max,min,sorted,index,sum,count
print(len(t1))
print(max(t1))
print(min(t1))
print(sorted(t1))
print(sorted(t1,reverse=True))
print(t1.index(2))
print(sum(t1))
print(t1.count(2))


