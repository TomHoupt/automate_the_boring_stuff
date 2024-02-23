tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    for x in tableData:
        colWidth = 0
        current_length = len(x)
        if current_length > colWidth:
            colWidth = current_length
        x = ", ".join(x).title()
        print(x.rjust(colWidth, ' '))



printTable()