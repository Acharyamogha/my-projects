class Employee:
 def __init__(self, name, emp_id, department, salary):
  self.name = name
  self.emp_id = emp_id
  self.department = department
  self.salary = salary
 def update_salary(self, new_salary):
  self.salary = new_salary
 def display_details(self):
  print("Name:", self.name)
  print("Employee ID:", self.emp_id)
  print("Department:", self.department)
  print("Salary:", self.salary)
  print()
# Create employee instances
employee1 = Employee("John Doe", 101, "HR", 50000)
employee2 = Employee("Jane Smith", 102, "Engineering", 60000)
# Display initial details
print("Initial details:")
employee1.display_details()
employee2.display_details()
print()
# Manually update salary for a specific employee
def update_employee_salary_manually(employee):
 new_salary = float(input(f"Enter new salary for {employee.name}: "))
 employee.update_salary(new_salary)
# Allow the user to change the salary of any employee
employee_to_update = input("Enter the name of the employee whose salary you want to update: ")
if employee_to_update == employee1.name:
 update_employee_salary_manually(employee1)
elif employee_to_update == employee2.name:
 update_employee_salary_manually(employee2)
else:
 print("Employee not found.")
# Display updated details
print("Details after salary update:")
employee1.display_details()
employee2.display_details()