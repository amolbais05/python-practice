
def student_info(*arg, **kwarg):
	print(arg)
	print(kwarg)

student_info('Art','Eng',name='Krsna',age=16)


courses=['Art','Eng','Math']
dictn = {'name':'amol','age':26}

print('-----------------')
student_info(courses,dictn) 
print('-----------------')

student_info(*courses,**dictn) # for unpacking the values 
print('-----------------')
