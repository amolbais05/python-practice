'''
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print(string)
'''


def mutate_string(string, position, character):
	l = list(string)
	l[position] = character
	string = ''.join(l)
	return string

def mutate_string2(string, position, character):
	l = list(string)
	l[5] = 'k'
	string = ''.join(l)
	return string	

print(mutate_string('abracadabra',5,'k'))    