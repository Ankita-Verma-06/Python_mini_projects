import array

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, emp_id: int, name: str, base_salary: float):
        if base_salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_allowances(self):
        return self.base_salary * 0.15 

    def calculate_deductions(self):
        return self.base_salary * 0.22  

    def calculate_net_salary(self):
        return self.base_salary + self.calculate_allowances() - self.calculate_deductions()

employee_ids = array.array('i', [])
employee_registry = {}

while True:
    print("\n=== PAYROLL MANAGEMENT SYSTEM ===")
    print("1. Add Employee")
    print("2. Display Salary Report")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        try:
            emp_id = int(input("\nEnter Employee ID: "))
          
            if emp_id in employee_ids:
                print(" Error: Employee ID already exists.")
                continue
                
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Base Salary: "))

           
            emp = Employee(emp_id, name, salary)

            employee_ids.append(emp_id)
            employee_registry[emp_id] = emp
            print("Employee added successfully!")

        except ValueError:
            print(" Error: ID and Salary must be numeric values.")
        except InvalidSalaryError as e:
            print(f"Error: {e}")

    elif choice == '2':
        if not employee_ids:
            print("\n No employee records found. Please add an employee first.")
            continue

        print("\n" + "="*60)
        print(f"{'FINAL PAYROLL REPORT':^60}")
        print("="*60)
        print(f"{'ID':<10} {'Name':<15} {'Base':<12} {'Net Salary':<12}")
        print("-"*60)

        for pid in employee_ids:
            e = employee_registry[pid]
            print(f"{e.emp_id:<10} {e.name:<15} {e.base_salary:<12.2f} {e.calculate_net_salary():<12.2f}")
        print("="*60)

    elif choice == '3':
        print("\nThank you for using the Payroll System. Goodbye!")
        break
        
    else:
        print(" Invalid option! Please select 1, 2, or 3.")
