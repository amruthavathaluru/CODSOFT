def calculator():
    a=int(input("Enter number1:"))
    b=int(input("Enter number2:"))
    print("1.Addition   2.Substraction   3.multiplication   4.Division")
    ch=int(input("Enter your choice:"))
    match ch:
        case 1:
            print(a,"+",b,"=",a+b)
        case 2:
            print(a,"-",b,"=",a-b)
        case 3:
            print(a,"*",b,"=",a*b)
        case 4:
            print(a,"/",b,"=",a/b)
        case _:
            print("Invalid Operation")
calculator()
while(1):
    Y=input(("Do you want to continue(y/n):"))
    if(Y=='y'):
        calculator()
    else:
        break

            
    
