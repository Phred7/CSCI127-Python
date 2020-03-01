
total = int(input("How many pennies do you have? "))

nickles = int(total/5)

pennies = total%5

pennies = total - (nickles*5)

print (nickles, "nickles and", pennies, "pennies" )


