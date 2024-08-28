n = int((input("Enter a number. This will be the story point: ")))

a, b = 0, 1

print("Fibonacci Sequence Print Out: ")

for _ in range(n):
    print(a, end= " ")
    a, b = b, a + b

    