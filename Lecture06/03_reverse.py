s=[1,2,3,4]

# Name

for i in range(len(s)//2):
    j=len(s)-i-1
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
# 
print(s)