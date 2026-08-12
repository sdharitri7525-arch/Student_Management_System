import json
import os
# Color codes for a beautiful terminal
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

FILE_NAME = "students.json"

# Load data if the file exists, otherwise start with an empty list
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        students = json.load(f)
else:
    students = []

while True:
    print("\n=========================")
    print(CYAN + "Student Management System" + RESET)
    print("=========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        
        # Save as a dictionary and append to list
        student_data = {"name": name, "roll": roll}
        students.append(student_data)
        
        # Save permanently to the file
        with open(FILE_NAME, "w") as f:
            json.dump(students, f, indent=4)
        print(GREEN + "Student Added successfully!" + RESET)
        
    elif choice == "2":
        print(YELLOW + "\n--- View Students ---" + RESET)
        if not students:
            print(RED + "No students added yet." + RESET)
        else:
            for s in students:
                print(f"Name: {s['name']}, Roll: {s['roll']}")
                
    elif choice == "3":
        print("\n--- Search Student ---")
        search_roll = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s['roll'] == search_roll:
                print(f"Found! Name: {s['name']}, Roll: {s['roll']}")
                found = True
                break
        if not found:
            print("Student not found.")
            
    elif choice == "4":
        print("\n--- Delete Student ---")
        delete_roll = input("Enter roll number to delete: ")
        found = False
        for s in students:
            if s['roll'] == delete_roll:
                students.remove(s)
                with open(FILE_NAME, "w") as f:
                    json.dump(students, f, indent=4)
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Student not found.")
            
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
        