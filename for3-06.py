# python-2 for3-06

column = int(input('column number =>'))
row = int(input('row number =>'))

if column < 2 or row < 2:
    print('invalid!')
else:
    for r in range(row):
        if r == 0 or r == row-1:
            print('■'+'□'*(column-2)+'■')
        else:
            print('□'*column)