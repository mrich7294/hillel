student = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))
value = apples // student
rest = apples % student
print("Every student receive {} apples! \nThere are {} apples left in the basket.".format(value, rest))