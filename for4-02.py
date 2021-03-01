# python2 for4-02

for outer in range(0,5):
    for inner in range(5,10):
        if outer in [3,5] or inner in [3,5]:
            print('***')
        else:
            print(outer,inner)