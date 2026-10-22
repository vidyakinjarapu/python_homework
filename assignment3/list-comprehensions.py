# ------------------ TASK 3 ------------------------
import csv

with open("../csv/employees.csv", newline="") as f:
    employee_list = list(csv.reader(f))

print(employee_list)

emploee_names = [employee_list[i][1] + " " + employee_list[i][2] for i in range(1, len(employee_list))]
print(emploee_names)

fullname_list = [name.split(" ")[0] for name in emploee_names]

final_list = [name for name in emploee_names if "e" in name]

print(final_list)