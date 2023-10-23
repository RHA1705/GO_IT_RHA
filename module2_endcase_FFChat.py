result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            operand = int(input('Enter a number: '))
            if result is None:
                result = operand
            wait_for_number = False
        else:
            operator = input('Enter +, -, *, or /: ')
            if operator == '=':
                break
            elif operator not in ['+', '-', '*', '/']:
                raise ValueError(f"{operator} is not a valid operator. Try again.")
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    result /= operand
                wait_for_number = True
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)

print(f"Result: {result}")