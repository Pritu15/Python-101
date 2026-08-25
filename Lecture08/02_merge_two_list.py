L1=[1,2,3]
L2=[4,5,6,7,8]

L=[]
# L=L1+L2
# print(L)
for i in range(len(L1)):
    L.append(L1[i])

for i in range(len(L2)):
    L.append(L2[i])

print(L)