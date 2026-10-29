import pandas as pd
import numpy as np
import os

# ================== Task1 =====================
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create dataframe from dictionary
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# -------- Add new salary column
task1_with_salary = task1_data_frame.copy(deep=True)
print("task1_data_frame-before, \n", task1_data_frame)
Salary = [70000, 80000, 90000]
task1_with_salary["Salary"] = Salary
print(task1_with_salary)

# ----------- Modify an existing column -------
task1_older = task1_with_salary.copy(deep=True)
task1_older['Age']+=1
print(task1_older)

# ------------- Save the DataFrame as a CSV file ----------
task1_older.to_csv("employees.csv", index=False)


# ============== Task 2 ===========================
# reading data from CSV file
task2_employees = pd.read_csv("employees.csv")
print("Reading_data: \n", task2_employees)

# additional_employees.json
data = { "Name": ["Eve", "Frank"],
  "Age": [28, 40],
  "City": ["Miami", "Seattle"],
  "Salary": [60000, 95000]
}
df = pd.DataFrame(data)
print(df)
df.to_json("additional_employees.json", index=False)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# more_employees => json data + csv data
more_employees = pd.concat((task2_employees, json_employees), ignore_index=True)
print(more_employees)

# ====================== Task 3 =============================
# head
first_three = more_employees.head(3)
print("head:, \n", first_three)

# tail
last_two = more_employees.tail(2)
print("tail: \n", last_two)

# shape
employee_shape = more_employees.shape
print(employee_shape)

# info
print(more_employees.info())


# ===================== Task 4 =====================

HERE = os.path.dirname(os.path.abspath(__file__))
dirty_data = pd.read_csv(os.path.join(HERE, "dirty_data.csv"))

# dirty_data = pd.read_csv("assignment4/dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy(deep=True)

# Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("before: \n", clean_data)

# Convert age
clean_data["Age"] = clean_data["Age"].replace("NaN", pd.NA)
clean_data['Age'] =  pd.to_numeric(clean_data['Age'], errors='coerce')
print("after_age: \n", clean_data)

# Convert Salary
clean_data["Salary"] = clean_data["Salary"].replace("NaN", pd.NA)
clean_data['Salary'] =  pd.to_numeric(clean_data['Salary'], errors='coerce')
print("after_age: \n", clean_data)

# Fill the missing values of salary
mean_score = clean_data['Age'].mean()  # ignoring NaNs
clean_data['Age'] = clean_data['Age'].fillna(mean_score)

median_score = clean_data['Salary'].median()  # ignoring NaNs
clean_data['Salary'] = clean_data['Salary'].fillna(median_score)
print("After_mean: \n", clean_data)

# Converting all dates to date time
clean_data['Hire Date'] =  pd.to_datetime(clean_data['Hire Date'], format='mixed', errors="coerce")
print("After date_conversion: \n", clean_data)

# Stripping white spaces
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()

clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Department'] = clean_data['Department'].str.upper()
print("After standardising: \n", clean_data)
