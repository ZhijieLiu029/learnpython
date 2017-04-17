age = input('Please input your age:')
age = int(age)
if age >= 18:
    print('Your age is',age )
    print('adult') 
elif age>=6:
    print('Your age is',age )
    print('teenage')
else:
    print('Kid')