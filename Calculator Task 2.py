while True:
    print("""
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Remender
6: Exit """)
    c=input("Enter any choice : ")
    if c=="6":
        break
    elif c=="1" or  c=="2" or c=="3" or c=="4" or c=="5":
        num1=int(input("Enter a number : "))
        num2=int(input("Enter second number :"))
        if c=="1":
            print("Adidition = ",num1+num2)
        elif c=="2":
             print("Subtraction = ",num1-num2)
        elif c=="3":
             print("Multiplication = ",num1*num2)
        elif c=="4":
             print("Division = ",num1/num2)
        elif c=="5":
             print("Remender = ",num1%num2)
    else:
        print("Enter a valid choice") 
    
        
