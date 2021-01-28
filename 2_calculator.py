x = float(input('Enter first number:'))
y = float(input('Enter second number:'))
operation = input("Enter the sign of the arithmetic operation:")
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '^':
    result = x ** y
elif operation == '/':
    if y == 0:
        print('Unsupported operation')
    else:
        result = x / y

if result is not None:
    print(result)
