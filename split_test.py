def split_and_join(line):
    line = line.split(' ')
    line = '-'.join(line)
    print(line)


a = 'This is simple string'

split_and_join(a)    

print('-'.join(input().split()))
return("-".join(line.split()))