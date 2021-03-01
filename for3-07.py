# python-2 for3-07

row = int(input('row number =>'))

if row <= 0:
    print('invalid!')
else:
    for r in range(1,row+1):
        if r%2 == 1:
            print('▲'*r)
        else:
            print('△'*r)