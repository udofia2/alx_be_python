number = int(input("Enter a number to see its multiplication table:"))

for x in range(1, 10):
  result = number * x
  print(f"{number} * {x} = {result}")