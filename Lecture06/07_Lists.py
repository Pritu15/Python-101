L=[1,2,3,1]
L2=[1,3,2,1]
L4=L
L5=L.copy()
print(id(L))
print(id(L4))
print(id(L5))

L3=[1,2,3,1]
print(L==L2)
print(L==L3)

# Empty
print([])
# 1D
print(L)
# 2D
List_2D_demo=[1,2,3,[4,5]]
print(List_2D_demo[3])
print(List_2D_demo[3][1])
# 3D
list_3D_demo=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(list_3D_demo[0])
print(list_3D_demo[0][1])
# print("*"*20)
print(list_3D_demo[1][1][0])

print(list('hello'))