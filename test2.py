import math
print("simple calculator")
print("1.Add")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice=float(input("choose operation "))

num1=float(input("enter num 1: "))
num2=float(input("enter num2: "))

match choice:
    case 1:
        print("results= ",num1+num2)
    case 2:
        print("results= ",num1-num2)
    case 3:
      print("results= ",num1*num2) 
    case 4:
        if num2!=0:
            print("results= ",num1/num2)
        else:
            print("division by zero is not allowed")        
    case _:
        print("invalid choice") 
    



