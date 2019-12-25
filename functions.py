
def hello_func():
	pass # keeps function as blank

print(hello_func)
print(hello_func())	

def hello_func2():
	print('Hello function')


print(hello_func2())

def hello_func3():
	return 'Return Hello function'

hello_func3()
print(hello_func3())


def hello_parameter(greeting):
	return '{} function'.format(greeting)

def hello_parameter2(greeting , name ='You'):
	return '{} , {}'.format(greeting, name)


print(hello_parameter('amol'))

print(hello_parameter2('Good Morning'))
print(hello_parameter2('Good Morning', name ='Krishna'))
print(hello_parameter2('Good Morning', 'Krishna'))