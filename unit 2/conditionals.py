# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions.

# conditional syntax(how it is written)
bill_amount = int(input("please type in a bill tender(1,5,10): "))

# if usually indicate that something is a possible option
if bill_amount == 1:
    print("here are 4 quarters")

elif bill_amount == 5:
    print("here are 20 quarters")

elif bill_amount == 10:
    print("here are 40 quarters")

elif bill_amount is 20:
    print("sorry we do not accept 20s. please enter an accepted amount")


#else is ALWAYS your last option.
else:
    print("sorry that type of bill is not accepted. ")

    # elif allows us to indecate that there are more possible options
    # you can have as many elif as you want


# create a calculator function that uses if/else logic to allow the user
# to change or select different arithmentic operations.
# example: an input where if the user enter 1, it will do
# addition, 3 will do subtaction
# 3 will do multiplication and 4 division

Calc = int(input("please enter the sign(+,-,*,/): "))

if Calc ==



