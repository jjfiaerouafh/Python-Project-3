#EMPLOYEE SALARY SYSTEM
class Employee:
    
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print("Salary increased successfully.")
        else:
            print("Invalid increment amount.")

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Current Salary:", self.salary)


# Creating object
emp1 = Employee("Anantha Krishnan", 101, 30000)

# Testing methods
emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()