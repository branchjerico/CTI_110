# -*- coding: utf-8 -*-
"""P3HW2


#Jerico Branch
#3/13/2025
#P3HW2
#Determine OT pay, regular pay, and gross pay

'''
Pseudocode:

Get employee_name from user (create a variable, use input())
Get employee_name from user (create a variable, use input())
Get pay_rate from user (create a variable, use input())

Determine if employee worked any overtime

if hours_worked > 40:
    Calculate OT_hours_worked (hours_worked -40) - create variable
    Calculate OT_pay_rate (pay_rate * 1.5) - create variable
    Calculate OT_pay (OT_hours_worked* OT_pay_rate) - create variable
    Calculate reg_pay (40 * pay_rate) create variable
    Calculate gross_pay (OT_pay + reg_pay) create variable

# hours_worked < = 40
else:
    Calculate OT_hours_worked = 0
    Calculate OT_pay_pay = 0
    Calculate reg_pay (hours_worked * pay_rate) create variable
    Calculate gross_pay (OT_pay + reg_pay)

Output the values
Display employee name separately
Display all heading (formatted)
display dotted line
display the corresponding values (formatted)

Display the values in columns
print(f"{'Hours Worked' :<20}{'Pay Rate'}")
print(f"-----" * 7)
print(f"{hours_worked :<20}${pay_rate :<20.2f}")

'''

# Get input values
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
pay_rate = float(input("Enter hourly pay rate: "))

# Determine if employee worked overtime
if hours_worked > 40:
    OT_hours_worked = hours_worked - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT_hours_worked * OT_pay_rate
    reg_pay = 40 * pay_rate
    gross_pay = OT_pay + reg_pay
else:
    OT_hours_worked = 0
    OT_pay = 0
    reg_pay = hours_worked * pay_rate
    gross_pay = reg_pay

# Display output

print("-" * 60)
print(f"Employee Name: {employee_name}")
print("")
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OT Hours':<15}{'OT Pay':<15}{'Reg Pay':<15}{'Gross Pay':<15}")
print("-" * 90)
print(f"{hours_worked:<15.2f}${pay_rate:<14.2f}{OT_hours_worked:<15.2f}${OT_pay:<14.2f}${reg_pay:<14.2f}${gross_pay:<14.2f}")