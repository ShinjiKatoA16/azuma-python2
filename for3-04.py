# python-2 for3-04

num = int(input('input positive number=>'))

if num < 0:
    print('invalid!')
else:
    for n in range(0, num+1):
        if n%2 == 0:
            print(n, 'even')
        else:
            print(n, 'odd')