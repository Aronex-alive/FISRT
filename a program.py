#WAP to find the area or the perimeter of A square according to the choice of the user
s=float(input("Enter the side of square in metres: "))
d=input("Press 1 for finding area and \n 2 for perimeter and \n 3 for digonal of it \n press 4 for an astonishment:  ")
if d=="1":
    print("Area of the square is: ",s*s)
    a=input("Do you want to find the perimeter of the square also? \n press Y for yes and N for no: ")
    if a.lower()== "y":
        print("perimeter of the square is:",4*s)
    else:
        print("OK, Have a good day")
elif d=="2":
    print("Perimeter of the square is: ",s*4)
    w=input("Do you want to find the area of the square also? \n press Y for yes and N for no: ")
    if w.lower()=="y":
        print("Area of square is: ",s*s)
    else:
        print("OK, Have a good day")
elif d=="3":
    from math import sqrt,pow
    print("Diagonal of square is: ",sqrt(pow(s,2)+ pow(s,2)))
elif d=="4":
    from random import randint
    i=randint(1,2)
    for i in (1,11):
        print("Random vlaues are: ",i)
        i+1
else:
    print("Please enter valid input")
    
            
    
