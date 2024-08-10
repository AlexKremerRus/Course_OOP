class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class BonusCalculator:
    def calculate_bonus(self, employee):
        if employee.position == "manager":
            return employee.salary * 0.1
        elif employee.position == "developer":
            return employee.salary * 0.05
        else:
            return 0

class Database:
    def save_employee(self, employee, bonus, tax):
        print(f"{employee.name} - Name employee")
        print(f"{employee.position} - Position")
        print(f"{employee.salary} - salary ")
        print(f"{bonus} - bonus")
        print(f"{employee.salary + bonus} with bonus")
        print(f"{employee.salary  + bonus - tax} with tax")
        # здесь реализуем логику сохранения сотрудника в базу данных
        print("Employee saved to database")

class EmailSender:
    def send_email(self, email):
        # здесь реализуем логику отправки email
        print(f"Email sent to {email}")

class TaxCalculator:
    def calculate_tax(self, employee, bonus):
        if employee.salary < 3000:
            return employee.salary  *  0.1
        if employee.salary <  10000:
            return employee.salary  *  0.2
        else:
            return employee.salary  *  0.3



# Usage
employee = Employee("Test Test", "developer", 5000)
bonus = BonusCalculator().calculate_bonus(employee)
tax = TaxCalculator().calculate_tax(employee, bonus)
Database().save_employee(employee, bonus, tax)
EmailSender().send_email("test@example.com")
