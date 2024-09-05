## print("Hey World")



length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
area = length * width

print("Area is: ", area)



num = int(input("Number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")



num1 = float(input("Enter first number: "))

num2 = float(input("Enter first number: "))

num3 = float(input("Enter first number: "))


#Max Value

maxvalue = max(num1,num2,num3)
minvalue = min(num1,num2,num3)

print("Max Value", maxvalue)
print("Min Value", minvalue)




entNum = int(input("Enter a number: "))

factorial = 1

for i in range(1, entNum + 1):
    factorial *- i
    print("Factorial of", entNum, "is", factorial)



string = input("Enter a string value: ")

reverseString = string[::-1]

print("Reverse String:", reverseString)