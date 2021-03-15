# python2 P23 for2-08 variation of slicing

num = int(input('input number => '))

# required repeat count is (num+4)//5)
long_str = '12345' * ((num+4)//5)
print(long_str[:num])