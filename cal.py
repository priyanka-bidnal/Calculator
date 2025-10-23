num1=float(input("Enter first number:"))
num2=float(input("Enter second number:))
operator=input("Enter operator:"))
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
        result=num1/num2  
    else:
        result="Error!"
else:
    result="Invalid operation"
print("Result:",result)    
    
