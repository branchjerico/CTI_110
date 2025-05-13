# Jerico Branch
# 3/20/2025
# P4LAB2
#Working with nested loops


# Create a variable to control the loop
run_again = "yes"

#While loop to control the main logic
while run_again != "no":
    integer = int(input("Enter an integer:"))
    if integer >= 0:
        for i in range(1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
        print("This program does not handle negative numbers")

    run_again = input("Would like to run the program again?")

#While loop ends here

print("Program is ending.....BYE!")

