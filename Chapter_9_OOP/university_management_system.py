'''----------UNIVERSITY MANAGEMENT SYSTEM----------'''

"""-----STUDENT MANAGEMENT CLASS"""
class Student:
    '''-----Constructor-----'''
    def __init__(self, student_id=0, name="", course=None, cgpa=0.0):
        self.id = student_id
        self.name = name
        self.courses = course if course is not None else {}
        self.__cgpa = cgpa


    '''-----Add Course Marks Function-----'''
    def add_course_marks(self, course_title="", course_marks=0):
        self.courses[course_title] = course_marks
        self.cgpa_calculator()
        

    '''-----CGPA Calculator-----'''
    def cgpa_calculator(self):
            if not self.courses: # Check if the courses dictionary is empty to prevent ZeroDivisionError
                self.__cgpa = 0.0
                return

            gpa_list = []
            for marks in self.courses.values():
                if marks > 90:
                    gpa_list.append(4.0)
                elif marks > 80:
                    gpa_list.append(3.0)
                elif marks > 70:
                    gpa_list.append(2.0)
                elif marks > 50:
                    gpa_list.append(1.0)
                else:
                    gpa_list.append(0.0)
                    
            self.__cgpa = round(sum(gpa_list) / len(self.courses), 2)

    '''---Academic Records-----'''
    def display_academic_record(self):
        self.cgpa_calculator()
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name.title()}")
        print("-" * 5, "ENROLLED COURSES", "-" * 5)

        for course, marks in self.courses.items():
            print(f"{course}: {marks}")
            
        print("-" * 30)
        print(f"CGPA: {self.__cgpa}")
        

"""-----UNIVERSITY MANAGEMENT CLASS-----"""
class University:
    def __init__(self, students_list=None):
        self.students_list = students_list if students_list is not None else []

    '''-----Find Student-----'''
    def find_student_by_id(self, search_id):
        for student in self.students_list:
            if student.id == search_id:
                return student
        return None

    '''-----Register Student-----'''
    def register_student(self, student_obj):
        self.students_list.append(student_obj)


  
uni = University()

while True:
    user_choice = input("""
                            1. Press 1 to register new student.
                            2. Press 2 to Search student record.
                            3. Press 3 to Add Coures
                            4. Press 4 to show record
                            5. Press 5 to exit. """)
    match user_choice:
        case "1":
            try:
                id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ").strip()
                if not name.replace(" ", "").isalpha():
                    print("Error: Name must contain only alphabets!")
                    continue
                    
                s1 = Student(id, name)
                uni.register_student(s1)
                print(f"{s1.name.title()} Student Added Successfully!")
            except ValueError:
                print("Invalid Input! ID must be a number.")

        case "2":
            student_id = int(input("Enter student ID to search: "))
            founded_student = uni.find_student_by_id(student_id)
            
            if founded_student is not None:
                print(f"Student Found! Name: {founded_student.name.title()} (ID: {founded_student.id})")
            else:
                print("Student Not Found!")
        case "3":
            student_id = int(input("Enter Student ID to add marks: "))
            found_student = uni.find_student_by_id(student_id)
            
            if found_student is not None:
                course_title = input("Enter course Title: ")
                course_marks = int(input("Enter course Marks: "))
                found_student.add_course_marks(course_title, course_marks)
            else:
                print("Error: Student Not Found.")

        case "4":
            student_id = int(input("Enter Student ID to show record: "))
            found_student = uni.find_student_by_id(student_id)
            
            if found_student is not None:
                print("\n" + "="*10 + " ACADEMIC REPORT " + "="*10)
                found_student.display_academic_record()
            else:
                print("Error: Student Record Not Found.")
        case "5":
            print("Bye-Bye")
            break











#s1 = Student(101, 'Ali')
#s2 = Student(102, 'Ahmad')
#s3 = Student(103, 'Bilal')

#uni = University()
#uni.register_student(s1)
#uni.register_student(s2)
#uni.register_student(s3)
#print(uni.students_list)

# found_student = uni.find_student_by_id(102)
# if found_student is not None:
#     print(f"Student found: {found_student.name}")
# else:
#     print("Student Not Found !")


        

'''-----STUDENT 1-----'''
# s1 = Student(1, "Ali")
# s1.add_course_marks("Math", 90)
# s1.add_course_marks("Computer Science", 90)
# s1.display_academic_record()

# print("-" * 30)
# print("     NEXT STUDENT     ")
# print("-" * 30)
'''-----STUDENT 2-----'''
# s1 = Student(2, "Ahmad")
# s1.add_course_marks("English", 91)
# s1.add_course_marks("Physics", 91)
# s1.display_academic_record()