# python2 P23 for2-08

num = int(input('input number=>'))
out_s = ''

for n in range(num):
    out_s += str(n%5+1)
print(out_s)