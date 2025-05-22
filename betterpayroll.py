#Chandler Chaffin 3.3.21 Better_Payroll.py
employee_one_name = input("Please enter an employee name: ")
#while loops to validate each input seems bad because of repeating the same code over and over
#my attempts to condense into a single while loop were unsuccessful.
while True:
  try:
    hours_worked_one = float(input("Please enter this employee's hours worked: "))
    break
  except: 
    print("invalid data type -- enter a float value")
while True:
  try:
    pay_rate_one = float(input("Please enter this employee's hourly pay rate: "))
    break
  except: 
    print("invalid data type -- enter a float value")
employee_two_name = input("Please enter another employee name: ") 
while True:
  try:
    hours_worked_two = float(input("Please enter this employee's hours worked: "))
    break
  except: 
    print("invalid data type -- enter a float value")
while True:
  try:
    pay_rate_two = float(input("Please enter this employee's hourly pay rate: "))
    break
  except: 
    print("invalid data type -- enter a float value")

if hours_worked_one > 40:
  overtime_hours_one_normalized = (hours_worked_one - 40) * 1.5
  hours_worked_one = 40
if hours_worked_two > 40:
  overtime_hours_two_normalized = (hours_worked_two - 40) * 1.5
  hours_worked_two = 40
#collected and stored the data in my variables
print("%s's gross pay is %.2f " % (employee_one_name, (hours_worked_one * pay_rate_one) + (overtime_hours_one_normalized * pay_rate_one)))
print("%s's gross pay is %.2f " % (employee_two_name, (hours_worked_two * pay_rate_two) + (overtime_hours_two_normalized * pay_rate_two)))
print("You need $%.2f to pay your employees" % ((hours_worked_one * pay_rate_one) + (hours_worked_two * pay_rate_two) + (overtime_hours_two_normalized * pay_rate_two) + (overtime_hours_one_normalized * pay_rate_one)))