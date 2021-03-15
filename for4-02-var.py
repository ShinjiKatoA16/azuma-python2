# python2 for4-02 variation to check string

for outer in range(0,5):
    for inner in range(5,10):
        out_s = '{} {}'.format(outer,inner)
        if '3' in out_s or '5' in out_s:
            print('***')
        else:
            print(out_s)