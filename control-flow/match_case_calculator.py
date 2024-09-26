num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))  
operation = input("Choose the operation (+, -, *, /):")

match operation:
  case "+":
    result = num2 + num2
    print(result)
  case "-":
    result = num2 - num2
    print(f"The result is {result}")
  case "*":
    result = num2 * num2
    print(f"The result is {result}")
  case "/":
    result = num2 / num2
    print(f"The result is {result}")