#Sets
# Unordered and no duplicate

courses = {'History','Maths','Computer','Science'}

new_courses = {'History','Statics','Laptop','Art','Maths'}

print(courses)

print('Maths' in courses) # can do with list and tuples, but sets are optimized for this

print(courses.intersection(new_courses))
print(new_courses.intersection(courses))
#
print(courses.difference(new_courses))
print(new_courses.difference(courses))


print(courses.union(new_courses))