#Making calculator

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def rem(x,y):
    return x%y

print("1. ADD\n2. SUB\n3. MUL\n4. DIV\n5. REM")
choice = int(input("Enter your choice:"))
x= int(input("Enter Your Number1:"))
y= int(input("Enter Your Number2:"))

if choice == 1:
    print(add(x,y))
elif choice == 2:
    print(sub(x,y))
elif choice == 3:
    print(mul(x,y))
elif choice == 4:
    print(div(x,y))
elif choice == 5:
    print("remainder:",rem(x,y))
else:
    print("Not Valid,This is a simple calculator for adding, subtraction, multiply,division and taking remainder")

    
