# P26 for3-02

out_s = ''
length = int(input('input number => '))
for i in range(length):
    if i%3 == 0:
        out_s = out_s + '●'
    elif i%3==1:
        out_s += '▲'
    else:
        out_s += '■'

print(out_s)