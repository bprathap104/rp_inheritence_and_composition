import hr

salary_employee = hr.SalaryEmployee(1, 'John', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Smith',30, 40)
commision_employee = hr.CommisionEmployee(3, 'William', 1500, 300)

payroll = hr.PayrollSystem()

payroll.calculate_payroll([salary_employee, hourly_employee, commision_employee])
