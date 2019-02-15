while True:
    num1 = input('number ')
    num2 = input('second number ')
    operation = input('operation ')
    if operation == '+':
        x = (int(num1) + int(num2))
        print(x)
        y = input('again? ')
        if y == 'no':
            print('Thank you, come again!')
            break
    elif operation == '-':
        x = (int(num1) - int(num2))
        print(x)
        y = input('again? ')
        if y == 'no':
            print('Thank you, come again!')
            break
    elif operation == '/':
        x = (int(num1) // int(num2))
        print(x)
        y = input('again? ')
        if y == 'no':
            print('Thank you, come again!')
            break
    elif operation == '*':
        x = (int(num1) * int(num2))
        print(x)
        y = input('again? ')
        if y == 'no':
            print('Thank you, come again!')
            break
