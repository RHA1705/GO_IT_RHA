result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            operand = int(input('Enter a number: '))
    except ValueError:
        print(f'{result} is not a number. Try again.')  
    else:
        if result == None:
            result = operand
    try:  
        operator = input('Enter an +, -, * or /: ')
        if operator == '=':
            break
        else:
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
    except:
        print(f"{operator} is not '+' or '-' or '/' or '*'. Try again.")                  
print(result)