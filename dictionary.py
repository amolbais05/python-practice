student = {'name' : 'Krishna','age' : 16,'courses' : ['dev','love','frndshp']}

print(student['name'])
print(student['courses'])
print(student.get('age'))
print(student.get('phone'))
print(student.get('phone','Value not presnt'))

student['phone'] = 98765
print(student.get('phone','Value not presnt'))

# Update method cab be used to add/update deatils

student.update({'name' : 'Achyut', 'age':26, 'desg' : 'dasa'})
print(student)

# delete 

del student['age']
print(student)

popped = student.pop('name')
print(student)
print(popped)


print(len(student))
print(student.keys())
print(student.values())
print(student.items())


for key in student:
	print(key)

for key, value in student.items():
	print(key, value)	