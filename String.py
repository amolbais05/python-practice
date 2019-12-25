message='Hello World'

print(message.find('Hello'))

new_message = message.replace('World', 'Amol')

print(new_message)


greeting='Hello'
name = 'Krishna'

#msg=greeting+', '+name+' Jai!!'

#msg='{}, {} Jai!!'.format(greeting,name)

msg=f'{greeting}, {name.upper()} Jai!!'
print(msg)


#for checking all possible attribute

print(dir(name))

print(help(str))

print(help(str.lower))