# using dictionery
person={'name':'Amol', 'age' : 26}

#statement = 'My name is '+person['name']+' and I am '+str(person['age'])+' years old.'

#statement = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])

statement = 'My name is {0} and I am {1} years old.'.format(person['name'],person['age'])


print(statement)

# un pacing dictionary
statementd = 'Dictionary Unpacking : My name is {name} and I am {age} years old.'.format(**person)
print(statementd)

tag = 'h1'
text = 'This is a headline'

sentance='<{0}>{1}<{0}>'.format(tag,text);
print(sentance)

statement2 = 'My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(statement2)


statement4 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(statement4)

#using list

l = ['Anju',23]

sentance2 = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentance2)


# using class

class Person():
	"""docstring for Person"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
p1 = Person('Apoorv', 26)


sentance3 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentance3)

sentance4 = 'My name is {name} and I am {age} years old.'.format(name='Achyut',age=25)
print(sentance4)
