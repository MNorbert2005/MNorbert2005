line = 1
indx = 0
index = 7
while line <= 7:
    column = 1
    while column <= 7:
        if indx < column:
            if not indx + 2 <= column:
                print('O ', end='')
            else:
                if index == column:
                    print('O ', end='')
                else:
                    print('. ', end='')
        else:
            if index == column:
                print('O ', end='')
            else:
                print('. ', end='')
        column += 1
    index -= 1
    indx += 1
    print('')
    line += 1