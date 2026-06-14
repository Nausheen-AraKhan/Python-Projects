import art
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operators={"+":add,
           "-":subtract,
           "*":multiply,
          "/":divide}
def calculator():
    yes_no="y"
    while yes_no=="y":
       print(art.logo)
       num1=int(input("Enter the first number: "))
       for op in operators:
           print(op)
       opt=input("Enter the operator: ")
       num2=int(input("Enter the second number: "))
       if opt in operators:
           print("The answer is: ", operators[opt](num1,num2))
       yes_no=input("Do you want to continue? (y/n): ").lower()
       print("\n"*20)


calculator()




