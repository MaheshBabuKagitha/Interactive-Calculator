#Interactive Calcualtor
import math
def calc():
    if c==1:
        add=(nn1 + nn2)
        print("Sum of your numbers are (x+y)",add)
    elif c==2:
        add=(nn1 - nn2)
        print("Subtraction of your numbers are (x-y)",add)
    elif c==3:
        add=nn1 * nn2
        print("Multiplication of your numbers are (x*y)",add)
    elif c==4:
        add=nn1 / nn2
        print("Division of your numbers are (x/y)",add)
    elif c==5:
        print("CALCULATOR CLOSED")
while True:
    try:
        print("___CALCULATOR___\nPLEASE CHOOSE A METHOD\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
        c=float(input("enter your choise: "))
        if c not in [1,2,3,4,5]:
            print("choose in range(1-5): ")
        elif c in [1,2,3,4]:
            try:
                nn1=float(input("enter your First number x:"))
                nn2=float(input("enter your Second number y:"))
                calc()
            except:
                print("you are trying to enter other than numbers..! \nCALCULATOR RESTARTED\n\n")
        
        elif c==5:
            print("CALCULATOR CLOSED")
            break
    except:
        print("enter number only..choose in range(1-5): ")
