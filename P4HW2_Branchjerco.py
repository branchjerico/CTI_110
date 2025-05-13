#Jerico Branch
#3-30-2025
#P4HW2

'''
 Initialize variables for totals and employee data.
Print table header.
Loop until user enters 'Done':
Get and validate employee name.
Get and validate hourly rate and hours worked.
Calculate regular and overtime pay.
Store employee data.
Update totals.
Print employee details.
Print final totals.
'''
#Initialize totals
total_regular = 0
total_overtime = 0
total_gross = 0
employee_count = 0
all_employees = []  # To store each employee's data


print("-" * 90)
print(f"{'Employee Name':<20}{'Hours':<10}{'Rate':<10}{'OT Hours':<10}{'OT Pay':<12}{'Reg Pay':<12}{'Gross Pay':<12}")
print("-" * 90)

while True:
    # Get employee name
    name = input("Enter employee name (or 'Done' to Terminate): ")
    if name.lower() == "done":
        break

    # Get pay rate and hours
    while True:
        try:
            rate = float(input("Enter hourly pay rate: $"))
            hours = float(input("Enter hours worked: "))
            if rate >= 0 and hours >= 0:
                break
            print("Please enter positive numbers")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


    # Calculate pay
    if hours > 40:
        overtime = hours - 40
        regular = 40
    else:
        overtime = 0
        regular = hours

    regular_pay = regular * rate
    overtime_pay = overtime * rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Store employee data
    employee_data = {
        'name': name,
        'hours': hours,
        'rate': rate,
        'overtime': overtime,
        'overtime_pay': overtime_pay,
        'regular_pay': regular_pay,
        'gross_pay': gross_pay
    }
    all_employees.append(employee_data)

    # Update totals
    total_regular += regular_pay
    total_overtime += overtime_pay
    total_gross += gross_pay
    employee_count += 1

    # Display current employee's data in table format
    print("-" * 90)
    print(f"{name:<20}{hours:<10.1f}${rate:<9.2f}{overtime:<10.1f}${overtime_pay:<11.2f}${regular_pay:<11.2f}${gross_pay:<11.2f}")

# Display final totals
print("-" * 90)
print(f"{'Total employees entered:':<30}{employee_count}")
print(f"{'Total regular pay:':<30}${total_regular:.2f}")
print(f"{'Total overtime pay:':<30}${total_overtime:.2f}")
print(f"{'Total gross pay:':<30}${total_gross:.2f}")
