#paint calculation for a room
#input the length, width and height of the room
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
height = float(input("Enter the height of the room in feet: "))

#calculate the area of the walls
wall_area = 2 * (length * height) + 2 * (width * height)
conditional_statement = length < 1 or width < 1 or height < 1 
if conditional_statement:
    print("Error: invalid values for length, width, and height.")
    quit()

total_area = wall_area
#calculate the amount of paint needed (1 gallon covers 350 square feet)

paint_needed = total_area / 350
#print the results

number_of_coats = int(input("Enter the number of coats of paint: "))
Conditional_statement2 = number_of_coats <= 0 
if Conditional_statement2:
    print("Error: invalid values for number of coats.")  
    quit()

cost_per_gallon = float(input("Enter the cost of paint per gallon: "))


total_cost = paint_needed * cost_per_gallon
conditional_statement3 = cost_per_gallon <= 0
if conditional_statement3:
    print("Error: invalid value for the cost per gallon.")
    quit()

print(f"The total area to be painted is {total_area:.2f} square feet.")
print(f"The amount of paint needed is {paint_needed:.2f} gallons.")
print(f"The total cost of the paint is ${total_cost:.2f}.")
