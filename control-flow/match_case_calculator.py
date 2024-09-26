num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))  
operator = input("Choose the operation (+, -, *, /):")

match operator:
  case "+":
    result = num2 + num2
    print(result)
  case "-":
    result = num2 - num2
    print(result)
  case "*":
    result = num2 * num2
    print(result)
  case "/":
    result = num2 / num2
    print(result)