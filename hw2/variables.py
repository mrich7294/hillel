print("Введіть перше ціле число!")
var1 = int(input("var1 = "))
print("Введіть друге ціле число!")
var2 = int(input("var2 = "))
var3 = var1
print("Це базові значення змінних: var1 = {}, var2 = {}".format(var1, var2))
var1 = var2
var2 = var3
print("Це використання буферної змінної: var1 = {}, var2 = {}".format(var1, var2))

var1, var2 = var2, var1
print("Це використання множинного присвоєння: var1 = {}, var2 = {}".format(var1, var2))

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print("Це використання арифметичних операцій: var1 = {}, var2 = {}".format(var1, var2))
