# Creating Strings
s='hello'
s2="hello"

# Multiline
s3='''Hello,My name is Pritu,
I am from Chittagong'''
s4="""Hello,My name is Pritu,
I am from Chittagong"""

s5=str("Hello")

print(s,s2,s3,s4)


#Accessing substrings from a string

# Positive Indexing
s='hello world'
print(s[4])
# print(s[41])

# Negative Indexing

print(s[-4])

# Slicing

print(s[6:0:-2])
print(s[::-1])
print(s[-1:-6:-1])

# Editing in a String

s='hello world'
# s[0]='H'  'str' object does not support item assignment

# del s
# print(s)

# Arithmatic Operation
print("Dhaka"+" "+"Metro")

print("Dhaka"*5)
print('dhaka'!='Chittagong')
print('dhaka'>'dhaka')

# Loops in String

for i in 'hello':
    print(i)

for i in 'hello':
    print("Dhaka")

print('D' in 'Dhaka')

# Common Functions

print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
print(sorted(s,reverse=True))

# Capitalize/Upper/Lower/
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s)

#Count /Find/Index
s='My name is Pritu'
print(s.count('i'))
print(s.find('q'))
print(s.index('i'))

# format
name='Satyam'
gender='Male'
# print('Hi my name is {1} and I am a {0}'.format(gender,name))
# f string // formatted string
print(f"Hi my name is {name} and I am a {gender}")
