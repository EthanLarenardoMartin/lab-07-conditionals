num1 = float(input("Please enter a number. "))
num2 = float(input("Please enter another number. "))
operator = input("Finally, please enter an operator. (mul/div/mod) ")

if operator == "mul":
    print(num1 * num2)
elif operator == "div":
    print(num1 / num2)
### or you can do "print(num1 // num2)"" for a rounded number. ###
elif operator == "mod":
    print(num1 % num2)
else:
    print("***invalid operation***")