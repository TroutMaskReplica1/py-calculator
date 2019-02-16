while True:
    num1 = input('enter an expression ')
    if num1 != 'done':
        print(eval(num1))
    elif num1 == 'done':
        break