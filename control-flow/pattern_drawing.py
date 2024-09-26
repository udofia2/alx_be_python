size = int(input("Enter the size of the pattern: "))

x = 0
while x < size:
    for _ in range(size):
        print("*", end="")
    print()
    x += 1