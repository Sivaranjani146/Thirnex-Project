import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("employee_data.csv")

print("Original Dataset:")
print(data)

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicates
data = data.drop_duplicates()

# Fill missing department values
data['Department'] = data['Department'].fillna("Unknown")

# Fill missing names
data['Name'] = data['Name'].fillna("No Name")

# Convert salary column to numeric
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')

# Replace missing salary with average salary
average_salary = data['Salary'].mean()

data['Salary'] = data['Salary'].fillna(average_salary)

print("\nCleaned Dataset:")
print(data)

# -----------------------------
# REPORT GENERATION
# -----------------------------

# Department-wise average salary
report = data.groupby('Department')['Salary'].mean()

print("\nDepartment Wise Average Salary:")
print(report)

# Save cleaned data
data.to_csv("cleaned_employee_data.csv", index=False)

# Save report
report.to_csv("salary_report.csv")

# -----------------------------
# VISUALIZATION
# -----------------------------

report.plot(kind='bar')

plt.xlabel("Department")

plt.ylabel("Average Salary")

plt.title("Department Wise Salary Report")

plt.show()