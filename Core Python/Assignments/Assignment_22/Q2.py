#WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

FILENAME = "emp.txt"

def add_record():
    with open(FILENAME, "a") as f:
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = input("Enter Basic Salary: ")
        f.write(f"{eid},{name},{basic}\n")
    print("Record added successfully")


def search_record():
    eid = input("Enter ID to search: ")
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == eid:
                print("Record Found:")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Basic:", data[2])
                found = True
                break

    if not found:
        print("Record not found")


def delete_record():
    eid = input("Enter ID to delete: ")
    found = False
    lines = []

    with open(FILENAME, "r") as f:
        lines = f.readlines()

    with open(FILENAME, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] != eid:
                f.write(line)
            else:
                found = True

    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")


def edit_record():
    eid = input("Enter ID to edit: ")
    found = False
    lines = []

    with open(FILENAME, "r") as f:
        lines = f.readlines()

    with open(FILENAME, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == eid:
                name = input("Enter new name: ")
                basic = input("Enter new basic salary: ")
                f.write(f"{eid},{name},{basic}\n")
                found = True
            else:
                f.write(line)

    if found:
        print("Record updated successfully")
    else:
        print("Record not found")


def display_records():
    print("\nAll Records:")
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                print("ID:", data[0], "Name:", data[1], "Basic:", data[2])
    except FileNotFoundError:
        print("No records found")


# -------- MAIN MENU --------
while True:
    print("\nMENU")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        edit_record()
    elif choice == "5":
        display_records()
    elif choice == "6":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
