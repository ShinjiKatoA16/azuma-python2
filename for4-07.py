# python2 P38 for4-07

num = int(input('input number =>'))
row = (num+4) // 5
count = 0

for r in range(row):
    out_s = ''
    for c in range(5):
        if count == num:
            break
        if count%2 == 0:
            out_s = out_s + '○'
        else:
            out_s = out_s + '●'
        count = count + 1
    print(out_s)