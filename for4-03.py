# Python-2 P34 for4-03

column = int(input('column number =>'))
row = int(input('row number =>'))

if column <= 0 or row <= 0:
    print('invalid!')
else:
    for r in range(row):
        out_s = ''
        for c in range(column):
            out_s = out_s + '◇'
        print(out_s)