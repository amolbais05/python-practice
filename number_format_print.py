for i in range(1,11):
	sentence = 'The value is {:02} '.format(i)
	print(sentence)


pi = 3.14159265
sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence)	

sentence1 = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence1)

sentence2 = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence2)