# Function to add a new student record
def add_record():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    cls = input("Enter class: ")
    marks = input("Enter marks: ")
    
    # Open file in append mode
    with open("student.txt", "a") as file:
        file.write(f"{roll},{name},{cls},{marks}\n")
    print("Record added successfully!")

# Function to display all student records
def display_records():
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return
            
            print("Roll Number\tName\t\tClass\tMarks")
            print("-" * 40)
            for line in lines:
                roll, name, cls, marks = line.strip().split(",")
                print(f"{roll}\t\t{name}\t\t{cls}\t{marks}")
    except FileNotFoundError:
        print("No records found.")

# Function to search for a student by roll number
def search_record():
    roll_search = input("Enter roll number to search: ")
    
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                roll, name, cls, marks = line.strip().split(",")
                if roll == roll_search:
                    print("Record found:")
                    print(f"Roll Number: {roll}")
                    print(f"Name: {name}")
                    print(f"Class: {cls}")
                    print(f"Marks: {marks}")
                    return
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Function to delete a student record by roll number
def delete_record():
    roll_delete = input("Enter roll number to delete: ")
    
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()
        
        # Filter out the record to delete
        updated_lines = []
        found = False
        for line in lines:
            roll, name, cls, marks = line.strip().split(",")
            if roll != roll_delete:
                updated_lines.append(line)
            else:
                found = True
        
        if found:
            with open("student.txt", "w") as file:
                file.writelines(updated_lines)
            print("Record deleted successfully!")
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Main menu-driven interface
def main():
    while True:
        print("\nMenu:")
        print("1. Add a new student record")
        print("2. Display all student records")
        print("3. Search for a student by roll number")
        print("4. Delete a student record by roll number")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_record()
        elif choice == "2":
            display_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
