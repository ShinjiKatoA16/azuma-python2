# Python-2 P34 for4-03 variation
# I/O (print) is slow function, it is not good to call it many times

column = int(input('column number => '))
row = int(input('row number => '))

if column <= 0 or row <= 0:
    print('invalid!')
else:
    for r in range(row):
        for c in range(column):
            print('◇', end = '')
        print()