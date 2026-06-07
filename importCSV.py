import csv
import os

CSV_FILE = "StudentRecord1.csv"
FIELDNAMES = ["roll", "name", "age", "marks"]

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        create_clean_csv()
    else:
        try:
            with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames != FIELDNAMES:
                    print("Corrupt CSV File detected. Recreating..")
                    create_clean_csv()
        except Exception:
            print("CSV Error. Recreating new file.")
            create_clean_csv()

def create_clean_csv():
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = FIELDNAMES)
        writer.writeheader()
    print("Fresh CSV created successfully.")

def find_student_by_roll(roll):
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader  = csv.DictReader(f)
            for row in reader:
                if row.get("roll", "").strip() == roll.strip():
                    return row
    except Exception:
        return None
    return None

def add_student():
    roll = input("Enter roll number").strip()
    if not roll:
        print("Roll number cannot be empty ")
        return
    if find_student_by_roll(roll):
        print(f"Roll {roll} already exists!")

    name = input("Enter names : ").strip()
    age = input("Enter age: ").strip()
    marks = input("Enter marks: ").strip()


    if not name or not age or not marks:
        print("All fields are required!")
        return
    
    if not age.isdigit() or not marks.replace('.', '', 1).isdigit():
        print("Age and Marks must be numeric!")
        return
    
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames= FIELDNAMES)
        writer.writerow({"roll": roll, "name":name, "age":age, "marks":marks})

    print("Student added successfully!")


def read_all_students():
    students = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    except:
        pass
    return students

def view_students():
    students= read_all_students()
    if not students:
        print("No reacords found.")
        return
    print("\n =====Student Records====")
    print(f"{'Roll':<10} {'Name': <25} {'Age': <8} {'marks':<8}")
    print("-" * 60)
    for s in students:
        print(f"{s['roll']:<10} {s['name']:<25} {s['age']:<8} {s['marks']:<8}  ")

def menu():
    initialize_csv()
    while True:
        print("\n ==== Student CSV System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter Option(1-3)").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    menu()
        
