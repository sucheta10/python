# Employee Management System:
# Design an employee management system where each employee is represented as an object. This system will manage employee details and their project assignments.
# Requirements:
# * Create a class Employee that stores information about each employee: name, ID, and department.
# * Create a class EmployeeManager that handles adding and removing employees, assigning them to projects, and tracking their current projects.
# * Each employee can be assigned to multiple projects. Implement methods to add and remove projects for each employee.
# * The EmployeeManager class should have the capability to list all employees under a specific project.
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.projects = []

    def __str__(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Department: {self.department}"

    def add_project(self, project):
        if project not in self.projects:
            self.projects.append(project)
            print(f"{self.name} has been assigned to the project: {project}.")
        else:
            print(f"{self.name} is already assigned to the project: {project}.")

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)
            print(f"{self.name} has been removed from the project: {project}.")
        else:
            print(f"{self.name} is not assigned to the project: {project}.")

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"{employee.name} has been removed from the system.")
                return
        print("Employee not found in the system.")

    def assign_project(self, emp_id, project):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.add_project(project)
                return
        print("Employee not found in the system.")

    def remove_project(self, emp_id, project):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.remove_project(project)
                return
        print("Employee not found in the system.")

    def list_employees_under_project(self, project):
        print(f"Employees assigned to the project '{project}':")
        for employee in self.employees:
            if project in employee.projects:
                print(employee)

# Function to prompt user for employee details
def input_employee_details():
    name = input("Enter the name of the employee: ")
    emp_id = input("Enter the ID of the employee: ")
    department = input("Enter the department of the employee: ")
    return name, emp_id, department


def main():
    emp_manager = EmployeeManager()

    while True:
        print("\n1. Add Employee")
        print("2. Remove Employee")
        print("3. Assign Project to Employee")
        print("4. Remove Project from Employee")
        print("5. List Employees under Project")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name, emp_id, department = input_employee_details()
            employee = Employee(name, emp_id, department)
            emp_manager.add_employee(employee)

        elif choice == '2':
            emp_id = input("Enter the ID of the employee to remove: ")
            emp_manager.remove_employee(emp_id)

        elif choice == '3':
            emp_id = input("Enter the ID of the employee: ")
            project = input("Enter the name of the project to assign: ")
            emp_manager.assign_project(emp_id, project)

        elif choice == '4':
            emp_id = input("Enter the ID of the employee: ")
            project = input("Enter the name of the project to remove: ")
            emp_manager.remove_project(emp_id, project)

        elif choice == '5':
            project = input("Enter the name of the project: ")
            emp_manager.list_employees_under_project(project)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()