
def Movie_tickets():
    print("hey buddy!, how old are you?")
    Age= int(input("enter age here:"))

  if Age < 7:
        print("your ticket is $8.00")
    elif Age > 8 and Age < 20:
        print("your ticket is $12.00")
    elif Age > 21 and Age < 60:
        print("your growing up buddy, your ticket price is $20.00")
    elif Age > 61:
        print("DAAAAMN your old, heres your free ticket!")
    else:
        print("get Better lil bro")


def Field_trip():
    print("Do you have a signed permission slip?")
    permslip= input()
    yes=True
    no=False
    if permslip == no:
        print("damn that sucks, well in that case, whats your GPA")
        gpa= int(input())
    elif permslip == yes:
        print("LESS GOOOOOO, welcome to the trip!")
    elif gpa <= 90:
        print("alright step on the bus and enjoy the ride!")
    elif gpa >= 90:
        print("get out of here bro your not going on the trip")
    else:
        print("This is usless info bro")


    Field_trip()







