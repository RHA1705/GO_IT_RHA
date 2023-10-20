result = None
operand = None
operator = None
wait_for_number = True

while wait_for_number:
    
    try:
        operand = int(input('Enter a number: '))
    except ValueError:
        print(f'{operand} is not a number. Try again.')
    else:
        result += operand
        