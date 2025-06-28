# 

from models import Person, Student, Professor, Course
from data.file_handler import read_json, write_json, append_to_json, delete_json_record

class University:

    def add_student():
        try:
            id = input("Enter student's ID: ")
            name = str(input("Enter student's name: "))
            email = str(input("Enter student's Email: "))
            new_student = Student(id, name, email)
            students = read_json("data/storage/students.json")
        except Exception as e:
            print(f"Error: {e}")
        else:
            for student in students:
                if student["id"] == id or student["email"] == email:
                    print(f"Student Id or Email already exists, enter a new student")
                    return
            students.append(new_student.to_dict())
            write_json("data/storage/students.json", students)
            print("Student added successfully!")

    def get_student():
        id = input("Enter student's ID: ")
        students = read_json("data/storage/students.json")
        for student in students:
            if student["id"] == id:
                print(f"Student Details \n{"-" * 10}")
                print(f"ID: {student["id"]} \nName: {student["name"]} \nEmail: {student["email"]}")
            else:
                print(f"Error: Student Id:{id} doesn't exist!")    

    def list_students():
        students = read_json("data/storage/students.json")
        print(f"{"id":<4} | {"name":<20} | {"email":<20} \n{"-" * 40}")
        for student in students:
            print(f"{student["id"]:<4} | {student["name"]:<20} | {student["email"]:<20}")
        
    def delete_student():
        id = input("Enter student's ID: ")
        students = read_json("data/storage/students.json")
        for student in students:
            if student["id"] == id:
                while True:
                    print(f"You are about to delete a student: {student["name"]} with ID {student["id"]}")
                    choice = str(input("Are you sure? (yes/no)")).strip().lower()
                    if choice == "yes":
                        delete_json_record("data/storage/students.json", key="id", value=id)
                        print(f"{student["name"]} deleted successfully")
                    elif choice == "no":
                        break
                    else:
                        print("Invalid input. Enter yes or no")
                
    def add_professor():
        try:
            id = input("Enter professor's ID: ")
            name = str(input("Enter professor's name: "))
            email = str(input("Enter professor's Email: "))
            department = str(input("Enter professor's department: "))
        except Exception as e:
            print("Error: {e}")
        else:
            new_professor = Professor(id, name, email, department)
            professors = read_json("data/storage/professors.json")
            for professor in professors:
                if professor["id"] == id or professor["email"] == email:
                    print(f"Professor Id or Email already exists, enter a new professor")
                    return
            professors.append(new_professor.to_dict())
            write_json("data/storage/professors.json", professors)
            print("Professor added successfully!")


    def get_professor():
        id = input("Enter professor's ID: ")
        professors = read_json("data/storage/professors.json")
        for professor in professors:
            if professor["id"] == id:
                print(f"Professor Details \n{"-" * 10}")
                print(f"ID: {professor["id"]} Name: {professor["name"]} Email: {professor["email"]} Department: {professor["department"]}")
            else:
                print(f"Error: Professor Id:{id} doesn't exist!")

    def list_professors():
        professors = read_json("data/storage/professors.json")
        print(f"{"ID":<4} | {"NAME":<20} | {"EMAIL":<20} | {"DEPARTMENT":<20}")
        for professor in professors:
            print(f"{professor["id"]:<4} | {professor["name"]:<20} | {professor["email"]:<20} | {professor["department"]:<20}")
   
        
    def delete_professor():
        id = input("Enter student's ID: ")
        professors = read_json("data/storage/professors.json")
        for professor in professors:
            if professor["id"] == id:
                while True:
                    print(f"You are about to delete a professor: {professor["name"]} with ID {professor["id"]}")
                    choice = str(input("Are you sure? (yes/no)")).strip().lower()
                    if choice == "yes":
                        delete_json_record("data/storage/professors.json", key="id", value=id)
                        print(f"{professor["name"]} deleted successfully")
                    elif choice == "no":
                        break
                    else:
                        print("Invalid input. Enter yes or no")

    def add_course():
        try:
            code = input("Enter course code: ")
            title = str(input("Enter course title: "))
            credits = str(input("Enter course credit(s): "))
            professor = str(input("Enter couurse professor: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            new_course = Course(code, title, credits, professor)
            courses = read_json("data/storage/courses.json")
            for course in courses:
                if course["code"] == code:
                    print(f"Course code:{course["code"]} already exists, enter a new course")
                    return
            courses.append(new_course.to_dict())
            write_json("data/storage/courses.json", courses)
            print("Course added successfully!")


    def get_course():
        code = input("Enter course code: ")
        courses = read_json("data/storage/courses.json")
        for course in courses:
            if course["code"] == code:
                print(f"Course Details \n{"-" * 10}")
                print(f"ID: {course["code"]} \nName: {course["title"]} \nCredits: {course["credits"]} \nProfessor Incharge: {course["professor"]}")
            else:
                print(f"Error: Course code:{code} doesn't exist!")
    
    def list_courses():
        courses = read_json("data/storage/courses.json")
        print(f"{"CODE":<4} | {"TITLE":<20} | {"CREDIT":<3} | {"PROFESSOR":<20}")
        for course in courses:
            return course
        
    def delete_course():
        code = input("Enter course code: ")
        courses = read_json("data/storage/courses.json")
        for course in courses:
            if course["code"] == code:
                while True:
                    print(f"You are about to delete a course: {course["code"]}: {course["title"]}")
                    choice = str(input("Are you sure? (yes/no)")).strip().lower()
                    if choice == "yes":
                        delete_json_record("data/storage/courses.json", key="code", value=code)
                        print(f"{course["code"]}: {courses["title"]} deleted successfully")
                    elif choice == "no":
                        break
                    else:
                        print("Invalid input. Enter yes or no")