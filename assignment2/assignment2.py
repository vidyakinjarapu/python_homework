# ------------------ TASK 2 --------------------------------
import csv
def read_employees():
    data = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
        return data
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}: {e}")
        exit()
        
employees = read_employees()
# print(employees)

# --------------------------- TASK 3 -------------------------------
def column_index(col_name):
    idx = employees["fields"].index(col_name)
    return idx
# print(column_index("first_name"))


# --------------------------- Task 4 -------------------------------
def first_name(row_num):
    col_num = column_index("first_name")
    row = employees["rows"][row_num][col_num]
    # print(row)
    return row

# first_name(3)

# -------------------------- Task 5 ------------------------------
employee_id_column = column_index("employee_id")
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# -------------------------- Task 6 ------------------------------
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# --------------------------- Task 7 ------------------------------
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

# print(sort_by_last_name())

# ----------------------------- Task 8 -------------------------------
def employee_dict(row):
    res_dict = {}
    for i in range(len(employees["fields"])):
        if i == employee_id_column:
            continue
        res_dict[employees["fields"][i]] = row[i]
    return res_dict
# print(employee_dict(['10', 'Kelli', 'Bowman', '+379 (843)240-1818x77648'])) 

print("Emp_id_col: ", employee_id_column)


# -------------------------------- Task 9 ---------------------------------
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        key = row[employee_id_column]
        result[key] = employee_dict(row)
    return result
    
# print(all_employees_dict())

# ------------------------------------ Task 10 -------------------------------
import os
def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())

#-------------------------------------- Task 11 ---------------------------------
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("batman")
print(custom_module.secret)

# ------------------------------------- Task 12 ---------------------------------
from pprint import pprint
def read_minutes():
    minutes1 = {}
    minutes2 = {}
    rows1 = []
    rows2 = []
    try:
        with open('../csv/minutes1.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes1["fields"] = row
                else:
                    rows1.append(tuple(row))
            minutes1["rows"] = rows1
        with open('../csv/minutes2.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes2["fields"] = row
                else:
                    rows2.append(tuple(row))
            minutes2["rows"] = rows2
        return minutes1, minutes2
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}: {e}")
        exit()
minutes1, minutes2 = read_minutes()
# print("minutes1: ", minutes1)
# print("minutes2: ", minutes2)

# ------------------------------ Task 13 -----------------------------
def create_minutes_set():
    set1= set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    final_set = set1.union(set2)
    return final_set
minutes_set = create_minutes_set()
# pprint(minutes_set)

# ------------------------------- Task 14 ------------------------------
from datetime import datetime
def create_minutes_list():
    time_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    # print(time_list)
    return time_list
minutes_list = create_minutes_list()

# ---------------------------------- Task 15 ----------------------------
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    sorted_time_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"]) # header first row
        writer.writerows(sorted_time_list) # then we write all the data rows
    return sorted_time_list   


pprint(write_sorted_list())