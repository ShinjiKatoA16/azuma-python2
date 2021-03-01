# python-2 for3-05

num = int(input('input negative number =>'))

if num < 0:
    for i in range(-1,num-1,-1):
        if i%6 == 0:
            print(i,'◆◇')
        elif i%2 == 0:
            print(i,'◆')
        elif i%3 == 0:
            print(i,'◇')
        else:
            print(i)
else:
    print('invalid!')