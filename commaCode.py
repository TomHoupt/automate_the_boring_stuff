## commaCode.py


#misc_list = ['cat', 'dog', 'bat', 'turtle', 'snake', 'lizard']
misc_list = ['cat', 'dog', 'lizard']
#misc_list = []
length_of_list = len(misc_list)


if misc_list == []:
    print('There is nothing in the list')
else:
    last_value = misc_list[-1]
    add_and = misc_list.insert(-1, 'and ')
    list_as_a_string = ', '.join(misc_list[0:length_of_list])
    print(list_as_a_string + last_value)


