# python2 P36 for4-05

column = int(input('column number=>'))
row = int(input('row number=>'))

if column < 2 or row < 2:
    print('invalid!')
else:
    for r in range(row):
        out_s = ''
        for c in range(column):
            if r in [0, row-1] and c in [0, column-1]:
                out_s = out_s + '■'
            else:
                out_s = out_s + '□'
        print(out_s)