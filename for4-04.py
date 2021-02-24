# Python-2 P35 for4-04

num = int(input('input number =>'))

if 1 <= num and num <= 9:
    for row in range(1,num+1):
        out_s = ''
        for col in range(num, num-row, -1):
            out_s = out_s + str(col)
        print(out_s)
else:
    print('input numbe 1-9')