text = "{number1} + {number2} = {result}"
number1 = int(input("enter the first number : "))
number2 = int(input("enter the second number : "))

result = number1 + number2 
print(text.format(number1 = number1, number2 = number2, result = result))