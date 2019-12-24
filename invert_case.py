my = 'amOL 2'
ret = ""
for a in my : 
	if a.isupper() :
		print(a.lower(), end ="")
		ret += a.lower()
	else:
		print(a.upper(), end ="")	
		a.upper()
	
print("------")


str.swapcase: print("".join(map(str.swapcase, input())))

