lst, lst2, lst3 = [], [], []
var1, var2 = 0, 0
value_classes = int(input("Enter the number of classes: "))
for i in range(0, value_classes):
    students = int(input("Enter the number of students in the classroom № {}: ".format(i+1)))
    lst.append(students)
for j in range(0, value_classes):
    lst2.append(lst[j] // 2)
    lst3.append(lst[j] % 2)
    if lst3[j] < 1:
        print("The number of desks in the classroom № {} - {}".format(j+1, lst2[j]))
        var1 = var1 + int(lst2[j])
    else:
        print("The number of desks in the classroom № {} - {}".format(j + 1, lst2[j]+1))
        var2 = var2 + int(lst2[j]) + 1
print("The total number of desks in the school - ", var1 + var2)
