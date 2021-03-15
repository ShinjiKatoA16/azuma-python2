# P26 for3-02 variation of slicing

num = int(input('input number => '))
rept = (num+2) // 3

long_str = '●▲■' * rept
print(long_str[:num])