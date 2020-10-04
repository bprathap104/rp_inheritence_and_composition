class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'-- Check amount: {employee.calculate_payroll()}')
            print('')
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id,name)
        self.hourly_rate = hourly_rate
        self.hours = hours
    def calculate_payroll(self):
        return self.hourly_rate * self.hours

class CommisionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commision):
        super().__init__(id,name,weekly_salary)
        self.commision = commision
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision
