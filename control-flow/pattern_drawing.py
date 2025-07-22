size = int(input("Enter the size of the pattern: "))

row_count = 0
while row_count < size:
    for _ in range(size):
        print("*", end="")
    print()
    row_count +=1