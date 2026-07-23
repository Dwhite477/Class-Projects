name = input("What is your name? ")
hourly_wage = float(input("What is your hourly wage? "))
number_of_hours = float(input("How many hours do you work in a week? "))
weekly_wage = hourly_wage * number_of_hours
print(f"{name}, your weekly wage is: ${weekly_wage:.2f}")
print(f"{name}, your net salary is: ${weekly_wage * 0.9:.2f}")