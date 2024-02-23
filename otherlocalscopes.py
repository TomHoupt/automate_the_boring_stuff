def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
print('---')

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
