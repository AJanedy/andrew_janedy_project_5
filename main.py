def LoadData(file_name, deliminator):
    student_list = []
    student_file = open(file_name, "r")
    for line in student_file:
        split_line = line.split(deliminator)
        student_name = split_line[0]
        student_id = int(split_line[1])
        student_creds = int(split_line[2])
        student_gpa = float(split_line[3])

        student_data = {
            "name": student_name,
            "id": student_id,
            "credits": student_creds,
            "gpa": student_gpa
        }
        student_list.append(student_data)
    student_file.close()
    return student_list

def menu():
    print("===================================================")
    print("Please choose an option")
    print("[1] Add a student")
    print("[2] Find masters students")
    print("[3] Find probation students")
    print("[4] Find honors students")
    print("[5] Exit")
    print("===================================================")

def add(student_list):
    student_name = input("Please enter the name of the new student: ")
    student_ID = int(input(f"Enter the student ID of {student_name}: "))
    student_credits = int(input(f"How many credits does {student_name} have?: "))
    student_GPA = float(input(f"What is {student_name}'s GPA?: "))
    new_student = {
        'name': student_name,
        'id': student_ID,
        'credits': student_credits,
        'gpa': student_GPA
    }
    student_list.append(new_student)

def masters(student_list):
    for student in student_list:
        if int(student['credits']) < 25:
            print(f"{student['name']} has {student['credits']} credits.")

def probation(student_list):
    for student in student_list:
        if float(student['gpa']) < 2.0:
            print(f"{student['name']} has a gpa of {student['gpa']}")

def honors(student_list):
    for student in student_list:
        if float(student['gpa']) > 3.0:
            print(f"{student['name']} has a gpa of {student['gpa']}")

def processUserInput(option, student_list):
    if option == "1":
        add(student_list)
    elif option == "2":
        masters(student_list)
    elif option == "3":
        probation(student_list)
    elif option == "4":
        honors(student_list)
    elif option == "5":
        exit(0)
    else:
        print("Invalid Option")

def main():
    student_list = LoadData("students.txt", "|")
    while True:
        menu()
        user_input = input("> ")
        processUserInput(user_input, student_list)

main()
