# 
from university import University
from models import Professor, Student, Course
from validators import InvalidEmailError

def main_menu():
    menu = ["students", "courses", "professors"]
    i = 1
    for item in menu:
        print(f"{i}. {item.title()}")
        i += 1

def student_menu():
    menu = ["add student", "search for student", "view students", "delete student", "main menu"]
    i = 1
    for item in menu:
        print(f"{i}. {item.title()}")
        i += 1

def professor_menu():
    menu = ["add professor", "search professors", "view professors", "delete professor", "main menu"]
    i = 1
    for item in menu:
        print(f"{i}. {item.title()}")
        i += 1

def course_menu():
    menu = ["add course", "search courses", "view courses", "delete course", "main menu"]
    i = 1
    for item in menu:
        print(f"{i}. {item.title()}")
        i += 1



university = University

def main():
    while True:
        print("Main menu")
        main_menu()
        option = int(input("Choose an option: "))

        # 
        match option:
            case 1:
                print("Student Menu")
                student_menu()
                student_option = int(input("Choose an option: "))
                match student_option:
                    case 1:
                        university.add_student()
                    case 2:
                        university.get_student()
                    case 3:
                        university.list_students()
                    case 4:
                        university.delete_student()
                    case 5:
                        pass
                    case _:
                        print("Invalid input")
            case 2:
                print("Course Menu")
                course_menu()
                course_option = int(input("Choose an option: "))
                match course_option:
                    case 1:
                        university.add_course()
                    case 2:
                        university.get_course()
                    case 3:
                        university.list_courses()
                    case 4:
                        university.delete_course()
                    case 5:
                        pass
                    case _:
                        print("Invalid input")
                
            case 3:
                print("Professor Menu")
                professor_menu()
                professor_option = int(input("Choose an option: "))
                match professor_option:
                    case 1:
                        university.add_professor()
                    case 2:
                        university.get_professor()
                    case 3:
                        university.list_professors()
                    case 4:
                        university.delete_professor()
                    case 5:
                        pass
                    case _:
                        print("Invalid input")

            case _:
                print("Invalid input")
                break


if __name__ == "__main__":
    main()