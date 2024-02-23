# Write your code here :-)

#grab each list and have those print out individually
# put a \n at the end of each new list.
# I will have to find the longest string in each of
#the inner lists of that the whole column can be wide enough
# to fit all of the strings. You can store the maximum
# width of each column as a list integer
# The printTable() function can begin with colWidth[0] * len(tableData)
#    colWidth[0] * len(tableData)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    colWidth = 0
    for x in tableData:
        x = ", ".join(x).title()
        current_length = len(x)
        if current_length > colWidth:
            colWidth = current_length
        print(x.rjust(colWidth, '_'))



printTable()
