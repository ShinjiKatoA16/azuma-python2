# python2 P37 for4-06 variation to use quotient and remain

number = int(input('input number => '))

nums = '12345'
# quotient, remain = divmod(number, 5)
quotient = number // 5
remain = number % 5

for q in range(quotient):
    print(nums)

if remain > 0:
    print(nums[:remain])