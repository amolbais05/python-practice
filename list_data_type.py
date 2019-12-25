courses = ['python','data science','machine learning','artifical intelligence']

print(courses)
print(len(courses))
print(courses[0])
print(courses[-3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(courses[:-1])

# add item to end of list

courses.append('R')
print(courses)

# insert at specific location

courses.insert(0, 'Maths')
print(courses)

# extend method to add complete list in list at specified position 

courses = ['python','data science','machine learning','artifical intelligence']
courses_2 = ['Maths','R']

#courses.insert(0, courses_2) # list in list, 
#courses.append(courses_2)
#print(courses)
#print(courses[0])

courses.extend(courses_2)
print(courses)

### Remove value from list

courses.remove('R')
print(courses)

popped_value = courses.pop() # removes last item
print("popped_value "+popped_value)
print(courses)


###### Reverse list

courses_3 = ['English','Science', 'Maths', 'Stat']
courses_3.reverse()
print(courses_3)

### Sort list
courses_4 = ['D','B', 'A', 'C']
courses_4.sort()
print(courses_4)
courses_4.sort(reverse=True)
print(courses_4)

num_list = [1,5,3,4]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)



# Without altering original list, how to sort... use sorted function, not sort method
courses_5 = ['History','Maths', 'Physics', 'CompSci']

#sorted(courses_4)
#print(courses_4)

sorted_list = sorted(courses_5)
print(sorted_list)

# Min, max, sum 
num_list = [1,5,3,4]
print(sum(num_list))
print(min(num_list))
print(max(num_list))


# find index and check value is present or not
print(courses_5.index('Maths'))
print('Java' in courses_5)
print('Maths' in courses_5)

for courses in courses_5:
	print(courses)

for index, courses in enumerate(courses_5):
	print(index, courses)

for index, courses in enumerate(courses_5, start=1):
	print(index, courses)


# List to String Conversion
courses = ['History','Maths', 'Physics', 'CompSci']

courses_str = ' - '.join(courses)
print(courses_str)

#courses_str = ' , '.join(courses)
#print(courses_str)

# String to List

new_list = courses_str.split(' - ')
print(new_list)
