students = []
print("Student Result Management System:\n\n1. Add Student Record\n2. Display All Records\n3. Search Student (by Name/Roll no.)\n4. Edit Record\n5. Delete Record\n6. Sort by Total marks\n7. Exit\n\nChoose an option number(1-7):-")
def add_student():
    roll = input("Enter your Roll No.-\n").strip()
    name = input("Enter your name-\n").strip()
    math = int(input("Enter your Math marks-\n"))
    science = int(input("Enter your Science marks-\n"))
    english = int(input("Enter your English marks-\n"))
    total = math+science+english
    percentage = total/3
    student = {
        "roll": roll,
        "name": name,
        "marks": {
            "Maths": math,
            "Science": science,
            "English": english
        },
        "Total": total,
        "Percentage": round(percentage, 2)
    }
    students.append(student)
    print(f"Student record for {name} added, Successfully!\n")

def display_all():
    if not students:
        print("There is no student record.\n")
        return
    

    print("Student Record")
    for idx, student in enumerate(students, start=1):
        print(f"""
              Student no- {idx}:
              Roll no.- {student['roll']}
              Name- {student['name']}
              marks- 
              Maths- {student['marks']['math']}
              Science- {student['marks']['science']}
              English- {student['marks']['english']}
              Total- {student['total']}
              Percentage- {student['percentage']}%
              """)
def search_student():
    search_term = input("Search by name or Roll no.: ").strip()
    found = False
    for idx, student in students:
        if search_term.lower() in student["name"].lower() or search_term == student["roll"]:
            print("\nStudent Found.\n")
            print(f"""
              Student no- {idx}:
              Roll no.- {student['roll']}
              Name- {student['name']}
              marks- 
              Maths- {student['marks']['math']}
              Science- {student['marks']['science']}
              English- {student['marks']['english']}
              Total- {student['total']}
              Percentage- {student['percentage']}%
              """)
            found = True
            break
    if not found:
        print("Sorry, Student not found.") 

def edit_student_record():
    search_term = input("Search by name or Roll no.: ").strip()
    for idx, student in students:
        if search_term.lower() in student["name"].lower() or search_term == student["roll"]:
            print("\nStudent Found.\n")
            print(f"""
              Student no- {idx}:
              Roll no.- {student['roll']}
              Name- {student['name']}
              marks- 
              Maths- {student['marks']['math']}
              Science- {student['marks']['science']}
              English- {student['marks']['english']}
              Total- {student['total']}
              Percentage- {student['percentage']}%
              """)
            print("Enter new details (leave blank to keep unchanged):")
            new_name = input("New Name ").strip()
            new_roll = input("New roll ").strip()
            new_math = input("New math ").strip()
            new_science = input("New science ").strip()
            new_english = input("New english ").strip()
            if new_name:
                student["name"] = new_name
            if new_roll:  
                student["roll"] = new_roll
            if new_math:
                student["marks"]["math"] = int(new_math)
            if new_science:
                student["marks"]["science"] = int(new_science)
            if new_english:
                student["marks"]["english"] = int(new_english)
                marks = student["marks"]
                student["total"] = marks["Math"] + marks["Science"] + marks["English"]
                student["percentage"] = round(student["total"] / 3, 2)
                print("Student record updated successfully!\n")
                return
            
print("Student not found.\n")
def delete_student():
    search_term = input("Enter name or Roll no. to delete student:\n").strip()
    found = False

    for idx, student in students:
        if search_term.lower() in student["name"].lower() or search_term == student["roll"]:
            print("student Found:")
            print(f"""
              Student no- {idx}:
              Roll no.- {student['roll']}
              Name- {student['name']}
              marks- 
              Maths- {student['marks']['Math']}
              Science- {student['marks']['Science']}
              English- {student['marks']['English']}
              Total- {student['total']}
              Percentage- {student['percentage']}%
              """)
            surity = input("Are you sure you want to delete this student details? (yes/no):\n").strip().lower()
            if surity == "yes":
                students.remove(student)  
                print("student is deleted successfully!")
                found = True
                break
            else:
                print("Deletion cancelled.")
                found = True
                break
def sort_students_by_total():
    if students:
        students.sort(key=lambda student: student["total"], reverse = True)
        print("students sorted by total marks!")
    else:
        print("No students to sort.")
            