# first we will store data

employee={
    101:{"name":"Raghav", "age":21, "department":"HR", "salary":50000},
    102:{"name":"Madhav", "age":20, "department":"IT", "salary":30000}
}

def main_menu():
    while True:
        print("Employee Management System")
        print("1-ADD EMPLOYEE")
        print("2-VIEW ALL EMPLOYEE")
        print("3-SEARCH FOR EMPLOYEE")
        print("4-EXIT")


        choice=input("ENTER YOUR CHOICE(1-4):")
        if choice=='1':  # we are using '1' this because string can not be compare with integer that is why we are using '1'
            add_employee()
        elif choice=='2':
            view_employee()
        elif choice=='3':
            search_employee()
        elif choice=='4':
            print("thank you for using EMS!!")
            break
        else :
            print("Invalid Choice")  

              


def add_employee():
    try:
        emp_id = int(input("Enter Employee Id: "))
        if emp_id in employee:
            print("Employee ID already exists.")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee {name} added successfully!")

    except ValueError:
        print("Invalid Input")



def view_employees():
    if not employee:
        print("No employees available.")
        return

    print("\nID\tName\t\tAge\tDepartment\tSalary")
    print("-" * 50)
    for emp_id, data in employee.items():
        print(f"{emp_id}\t{data['name']}\t{data['age']}\t{data['department']}\t{data['salary']}")


def search_employee():
    try:
        emp_id=int(input("Enter employee id to Search- "))
        if emp_id in employee:
            details=employee[emp_id]
            print(f"Employee found:\nName: {details['name']}\nAge: {details['age']}\nDepartment: {details['department']}\nSalary: {details['salary']}")
        else:
         print('Employee not found')    
    except ValueError:
        print('please enter valid id')      


main_menu()