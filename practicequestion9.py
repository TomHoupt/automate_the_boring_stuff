# write code that prints hello if 1 is stored in spam, prints howdy if 2 is
# stored in spam and prints greetings!  if anything else is stored in spam

print('Type 1, 2 or something else:\n')
spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
