email=input('Enter Email: ')
password=input("Enter Password")

if email=='pritu.dhar81@gmail.com' and password=='1234':
    print("Welcome")
elif email=='pritu.dhar81@gmail.com':
    print("Incorrect password")
    password=input('Enter password')
    if password=='1234':
        print('Welcome')
    else:
        print('You are not the user')
else:
    print('Not correct')
