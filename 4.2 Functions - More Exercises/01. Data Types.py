arg, el = input(), input()

if arg == 'int':
    print(int(el) * 2)
elif arg == 'real':    
    print(f'{(float(el) * 1.5):.2f}'  )
elif arg == 'string':    
    print('$' + el + '$')





