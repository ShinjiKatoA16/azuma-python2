# python2 P36 for4-05 variation

column = int(input('input column => '))
row = int(input('input row => '))
BLACK = '■'
WHITE = '□'

if row < 2 or column < 2:
    print('invalid!')
else:
    for r in range(row):
        out_s = ''
        for c in range(column):
            # if (r,c) in [(0,0), (0,column-1) ....]:
            if (r,c) == (0,0) or \
            (r,c) == (0,column-1) or \
            (r,c) == (row-1,0) or \
            (r,c) == (row-1,column-1):
                out_s += BLACK # black
            else:
                out_s += WHITE # white
        print(out_s)
