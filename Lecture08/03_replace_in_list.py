L=[10,21,13,4,15]

number_search=int(input("Enter number you want to search: "))
replace_value=int(input("Enter the replace value: "))
# i=L.index(number_search)
# print(i)
# L[i]=replace_value
# print(L)
index=-1
for i in range(len(L)):
    if L[i]==number_search:
        index=i
if index !=-1:
    L[i]=replace_value
    print(L)
else:
    print("Not found!")