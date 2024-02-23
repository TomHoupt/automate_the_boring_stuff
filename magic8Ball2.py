## magic8Ball2.py

import random

print('Welcome to the magic 8 ball. Please type in your question: ')
user_input = input()

message = [
'It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful',
]

newMessage = random.choice(message)
print(newMessage)

while newMessage == 'Concentrate and ask again' or newMessage == 'Reply hazy try again':
    print('Please type your question here: ')
    user_input = input()
    newMessage = random.choice(message)
    print(newMessage)

print('youre done')

