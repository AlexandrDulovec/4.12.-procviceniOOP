class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []
        self.grades = []
        self.average_grade = None

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_grade(self, grade):
        self.grades.append(grade)
        self.calculate_average_grade()

    def calculate_average_grade(self):
        if self.grades:
            self.average_grade = sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")
        print("Předměty:", ", ".join(self.subjects))
        print("Známky:", ", ".join(map(str, self.grades)))
        if self.average_grade is not None:
            print(f"Průměrné známky: {self.average_grade:.2f}")
        print()


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def display_info(self):
        print(f"Učitel: {self.name}, Věk: {self.age}")
        print("Předměty:", ", ".join(self.subjects))
        print("Studenti:")
        for student in self.students:
            print(f"- {student.name}")
        print()

student1 = Student("Alexandr", 19)
student1.add_subject("Webové programování")
student1.add_grade(1)
student1.add_grade(2)
student1.add_grade(1)
student1.display_info()

teacher1 = Teacher("Bc. Martin Kokeš", 33)
teacher1.subjects.append("Webové programování")
teacher1.add_student(student1)
teacher1.display_info()
