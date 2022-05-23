#calculator_program

def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Pick operator (+, - , *, or /): ")

if operator == "+":
    print("Result is "+str(addition(num1, num2)))  #Convert to string to concatenate 
    
elif operator == "-":
    print("Result is "+str(subtraction(num1, num2)))
    
elif operator == "*":
    print("Result is "+str(multiplication(num1, num2)))
    
elif operator == "/":
    print("Result is "+str(division(num1, num2)))

else: print("Operator is not valid !")
    

    

    

    