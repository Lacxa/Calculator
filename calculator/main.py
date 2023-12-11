def add(x, y):
   return x + y


def sub(x, y):
   return x - y


def mult(x, y):
   return x * y


def division(x, y):
   return x / y


print("calculator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

while True:
   choice = input("Enter your choice >> ")

   if choice in "1, 2, 3, 4":
       if choice == "1":
           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
               print(num1, "+", num2, "=", add(num1, num2))
           except ValueError:
               print("Enter valid input")

       elif choice == "2":
           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
               print(num1, "-", num2, "=", sub(num1, num2))
           except ValueError:
               print("Enter valid input")

       elif choice == "3":
           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
               print(num1, "*", num2, "=", mult(num1, num2))
           except ValueError:
               print("Enter valid input")

       elif choice == "4":
           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
               print(num1, "/", num2, "=", division(num1, num2))
           except ValueError:
               print("Enter valid input")

   else:
       print("Enter valid choice")


