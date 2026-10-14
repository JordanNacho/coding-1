def mainCalculator():
    print("please type in a number")
    selection = int(input())
    
    if selection == 1:
       
        calculate_add()
    elif selection == 2:
        calculate_subtract()
    elif selection == 3:
        calculate_multiply()
    elif selection == 4:
        calculate_devide()
    else:
        print("sorry something went wrong")
        
    
mainCalculator()