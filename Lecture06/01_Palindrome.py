s=input("Enter the word: ")

# Name
flag=True
for i in range(len(s)//2):
    j=len(s)-i-1
    if s[i]!=s[j]:
        flag=False
        print("Not palindrome")
        break

if flag==True:
    print("Palindrome")