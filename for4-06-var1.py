# python2 P37 for4-06 variation, change outer loop to while, it is easier to understand to use 2-d for loop

number = int(input('input number => '))
# row = (number+4)//5

while number > 0:
    out_s = ''
    for col in range(1,6):
        if number > 0:  # need to process more?
            out_s += str(col)
            number -= 1
        else:
            break
    print(out_s)