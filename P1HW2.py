 # Jerico Branch
 # 2/11/25
 # P1HW2
 # Travel Budgeting


#Calculating travel expense
#print("This program calculates and displays travel expenses")

first_num = int(input("Enter Budget:"))
travel_dest = str(input("Enter the travel destination:"))
gas_price = int(input("How much do you think you will spend on gas?:"))
accomdation_price = int(input("How much do you think you will spend on accomodation/hotel?:"))
food_price = int(input("Last, how much do you think you will spend on food?:"))

print("-"*9 + " Travel Expenses " + "-"*9)

print("Location: " + travel_dest)
print("Initial Budget: $" + str(first_num))
print("Fuel: $" + str(gas_price))
print("Accomodation: $" + str(accomdation_price))
print("Food: $" + str(food_price))
print("Remaining Balance: $" + str(first_num - gas_price - accomdation_price - food_price))