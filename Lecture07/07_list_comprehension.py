L=[]
for i in range(1,11):
    L.append(i)
print(L)
L.clear()
L=[i for i in range(1,11)]
print(L)
# result=[]
# for i in range(1,51):
#     if i%5==0:
#         result.append(i)
# print(result)
result=[]

result=[i for i in range(1,51) if i%5==0]
print(result)

#scalar multiplication of vector
v=[2,3,4]
s=-3
vs=[s*i for i in v]
print(vs)
L=[1,2,3,4,5]
L=[i*i for i in L]
print(L)

languages=['java','python','php','c','javascript']

print([i for i in languages if i.startswith('p')])

L=[[i] for i in range(1,6)]
print(L)

L3=[[i*j for i in range(1,4)] for j in range(1,4)]
print(L3)