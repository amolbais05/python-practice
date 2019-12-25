language = 'Python'

if language == 'Python':
	print('Its Py')
elif language == 'Java':
	print('Its Java')	
else:
	print('Nooo...')

#and
#or
#not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('User logged in!')
else:
	print('User Not logged')

a=[1,2,3]
b=[1,2,3]	

print(a == b)

print(id(a))
print(id(b))

print(a is b)
b=a
print(a is b)
