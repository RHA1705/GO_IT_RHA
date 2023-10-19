# print("Hello world!")
# print("Hello Git!")

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)
    
# print(factorial(5))

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
    print('You have 0 package to send')
else:
    print(f'You have {chunk} package to send')
finally:
    print("Have a nice day!")
