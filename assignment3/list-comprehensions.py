# ------------------ TASK 3 ------------------------
import csv

with open("../csv/employees.csv", newline="") as f:
    employee_list = list(csv.reader(f))

# print(employee_list)

emploee_names = [employee_list[i][1] + " " + employee_list[i][2] for i in range(1, len(employee_list))]

final_list = [name.split(" ")[0] for name in emploee_names]
print(final_list)


'''
employee_names = []
for i in range(1, len(employee_list)):
    employee_names.append(employee_list[i][1] + " " + employee_list[i][2])
print(employee_names)


[['employee_id', 'first_name', 'last_name', 'phone'],
  ['1', 'Cindy', 'Wade', '+222 656-486-3727']]
'''