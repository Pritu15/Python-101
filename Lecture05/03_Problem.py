# s=input("Enter the string: ")

# print(len(s))
# counter=0
# for i in s:
#     counter+=1
# print(f"The length of the string is {counter}")

# s=s.lower()
# temp=s[::-1]
# if s==temp:
#     print("palindrom")
# else:
#     print("Not palindrome")

# s=input("Enter you Email: ")
# pos=s.index('@')
# print(s[0:pos])

s=input("Enter a sentence: ")
L=[]

temp=''
for i in s:
    if i !=' ':
        temp+=i
    else:
        L.append(temp)
        temp=''

L.append(temp)
print(L)
