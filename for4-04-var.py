# Python-2 P35 for4-04 variation of slicing

number = int(input('input number => '))
NUMS = '987654321'

if 1 <= number and number <= 9:
    start = 9-number
    for row in range(1, number+1):
        print(NUMS[start:start+row])
else:
    print('invalid! 1-9')
