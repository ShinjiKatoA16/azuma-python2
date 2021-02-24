# python2 P37 for4-06

num = int(input('input number =>'))
row = (num+4) // 5
count = 0

for r in range(row):
    out_s = ''
    for c in range(1,6):
        if count == num:
            break
        else:
            count = count + 1
        out_s = out_s + str(c)
    print(out_s)