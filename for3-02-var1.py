# P26 for3-02 variation of list

length = int(input('input number => '))
out_s = ''
symbol = ['●','▲','■']   # list, tuple or string

for i in range(length):
    out_s += symbol[i%3]

print(out_s)