employees = {}


def add_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists!\n")
        return

    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    employees[emp_id] = {
        "name": name,
        "salary": basic_salary
    }

    print("Employee Added Successfully!\n")


def view_employees():
    if not employees:
        print("No Employees Found!\n")
        return

    print("\nEmployee Details")
    print("-" * 50)
    print("ID\tName\tSalary")

    for emp_id, emp in employees.items():
        print(emp_id, "\t", emp["name"], "\t", emp["salary"])

    print()


def search_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Found")
        print("Name :", emp["name"])
        print("Salary :", emp["salary"])
    else:
        print("Employee Not Found!")

    print()


def update_salary():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        new_salary = float(input("Enter New Salary: "))
        employees[emp_id]["salary"] = new_salary
        print("Salary Updated Successfully!")
    else:
        print("Employee Not Found!")

    print()


def delete_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee Deleted Successfully!")
    else:
        print("Employee Not Found!")

    print()


def generate_salary_slip():
    emp_id = input("Enter Employee ID: ")

    if emp_id not in employees:
        print("Employee Not Found!\n")
        return

    emp = employees[emp_id]

    basic = emp["salary"]
    hra = basic * 0.20
    da = basic * 0.10
    tax = basic * 0.05

    net_salary = basic + hra + da - tax

    print("\n========== Salary Slip ==========")
    print("Employee ID :", emp_id)
    print("Employee Name :", emp["name"])
    print("Basic Salary :", basic)
    print("HRA (20%) :", hra)
    print("DA (10%) :", da)
    print("Tax (5%) :", tax)
    print("-------------------------------")
    print("Net Salary :", net_salary)
    print("================================\n")


while True:
    print("===== Employee Payroll System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Generate Salary Slip")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        generate_salary_slip()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")