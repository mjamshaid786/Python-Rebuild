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
        student_id = int(input("Enter Student ID: "))
        for student in uni.students_list:
            if student.id == student_id:
                course_title = input("Enter course Title: ")
                course_marks = int(input("Enter course Marks: "))
                self.courses[course_title] = course_marks
                print("Record Added Successfully !")
            else:
                print("Student Not Found.")

    '''-----CGPA Calculator-----'''
    def cgpa_calculator(self):
            if not self.courses: # Check if the courses dictionary is empty to prevent ZeroDivisionError
                self.cgpa = 0.0
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
                    
            self.cgpa = round(sum(gpa_list) / len(self.courses), 2)

    '''---Academic Records-----'''
    def display_academic_record(self):
        self.cgpa_calculator()
        student_id = int(input("Enter Student ID: "))
        for student in uni.students_list:
            if student.id == student_id:

                print(f"Student ID: {student.id}")
                print(f"Student Name: {student.name.title()}")
                print("-" * 5, "ENROLLED COURSES", "-" * 5)
                for course in self.courses:
                    print(course)
                print("-" * 30)
                print(f"CGPA: {self.cgpa}")

"""-----UNIVERSITY MANAGEMENT CLASS-----"""
class University:
    def __init__(self, students_list=None):
        self.students_list = students_list if students_list is not None else []

    '''-----Find Student-----'''
    def find_student_by_id(self, search_id):
        for student in self.students_list:
            if student.id == search_id:
                return f"Student(ID: {student.id}, Name: '{student.name}')"
        return None

    '''-----Register Student-----'''
    def register_student(self, student_obj):
        self.students_list.append(student_obj)


  
uni = University()
st = Student()

while True:
    user_choice = input("""
                            1. Press 1 to register new student.
                            2. Press 2 to Search student record.
                            3. Press 3 to Add Coures
                            4. Press 4 to show record
                            5. Press 5 to exit. """)
    match user_choice:
        case "1":
            id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            s1 = Student(id, name)
            uni.register_student(s1)
            print(f"{s1.name.title()} Student Added Successfully: ")

        case "2":
            student_id = int(input("Enter student ID: "))
            founded_student = uni.find_student_by_id(student_id)
            print(founded_student)
        case "3":
            st.add_course_marks()
        case "4":
            st.display_academic_record()
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