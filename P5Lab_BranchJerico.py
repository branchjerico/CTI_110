#Jerico Branch
#4/3/2025
#P5Lab




import random
def disperse_change(change):
                   
 #Convert the float value into an integer
    change = int(change * 100)

    print(change)

        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")






def main():
    random_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${random_owed:.2f}")
    user_amt_paid = float(input("Enter cash into self checkout: $"))
    change_owned = user_amt_paid - random_owed
    print(f"Change owned: ${change_owned:.2f}")
    disperse_change(change_owned)

# Call the function to show 

# Call the main
if __name__== "__main__":
    main()