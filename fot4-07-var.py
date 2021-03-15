# python2 P38 for4-07 variation

number = int(input('input number => '))

sym_even = '○●○●○'
sym_odd = '●○●○●'
quotient = number // 5
remain = number % 5

for q in range(quotient):
    if q % 2 == 0:
        print(sym_even)
    else:
        print(sym_odd)

if remain > 0:
    if quotient % 2 == 0:
        print(sym_even[:remain])
    else:
        print(sym_odd[:remain])