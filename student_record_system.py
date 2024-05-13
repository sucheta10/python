# Student Records System
# Create a Python program that models a simple student records system using classes. Each student should have attributes such as name, age, and grade. The program should allow the user to create multiple student objects, display their information, and update their grades.

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display_info(self):
        print(f"Name: {self.name},Age: {self.age}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade=new_grade

def main():
        students=[]

        while True:
            print("\n1. Add Student")
            print("2. Display Students")
            print("3. Update Grade")
            print("4. Quit")

            choice= (input("Enter your choice: "))

            if choice == '1':
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                grade = input("Enter student's grade: ")
                student = Student(name, age, grade)
                students.append(student)
                print("Student added successfully!")

            elif choice == '2':
                if not students:
                    print("No students in the record.")
                else:
                    print("Student Information:")
                    for student in students:
                        student.display_info()

            elif choice == '3':
                if not students:
                    print("No students in the record.")
                else:
                    name = input("Enter student's name to update grade: ")
                    found = False
                    for student in students:
                        if student.name == name:
                            new_grade = (input("Enter new grade: "))
                            student.update_grade(new_grade)
                            found = True
                            print("Grade updated successfully!")
                            break
                    if not found:
                            print("Student not found.")

            elif choice == '4':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


main()