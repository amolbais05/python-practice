nums = [1,2,3,4,5]

for numbers in nums:
	if numbers == 3:
		print('Found!!')
		break
	print(numbers)

print('-------------')

for numbers in nums:
	if numbers == 3:
		print('Found!!')
		continue
	print(numbers)	

print('-------------')

for numbers in nums:
	for letters in 'abcde':
		print(numbers , letters)
				