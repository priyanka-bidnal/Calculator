def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
