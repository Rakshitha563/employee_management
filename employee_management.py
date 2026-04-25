import csv

FILE_NAME = "employees.csv"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    salary = input("Enter Salary: ")
    department = input("Enter Department: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, role, salary, department])

    print("Employee added successfully!\n")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Employee List ---")
            for row in reader:
                print("ID:", row[0], "Name:", row[1], "Role:", row[2],
                      "Salary:", row[3], "Department:", row[4])
            print()
    except FileNotFoundError:
        print("No file found!\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == emp_id:
                    print("Employee Found:", row)
                    found = True
                    break

        if not found:
            print("Employee not found!\n")

    except FileNotFoundError:
        print("No file found!\n")


def update_salary():
    emp_id = input("Enter Employee ID to update salary: ")
    new_salary = input("Enter New Salary: ")

    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == emp_id:
                    row[3] = new_salary
                    found = True
                rows.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Salary updated successfully!\n")
        else:
            print("Employee not found!\n")

    except FileNotFoundError:
        print("No file found!\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != emp_id:
                    rows.append(row)
                else:
                    found = True

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Employee deleted successfully!\n")
        else:
            print("Employee not found!\n")

    except FileNotFoundError:
        print("No file found!\n")


def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

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
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")


main()