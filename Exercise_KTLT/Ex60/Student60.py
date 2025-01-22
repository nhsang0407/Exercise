from datetime import datetime


class Student:
    def __init__(self,id,name,birth):
        self.id=id
        self.name=name
        self.birth=datetime.strptime(birth,"%d-%m-%Y")

    @property
    def last_name(self):
        return self.name.split()[-1]

    @property
    def first_name(self):
        return self.name.split()[0]

    @property
    def age(self):
        today = datetime.today()
        age=today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        return age

    def __str__(self):
        return (f"{self.id}"
                f"\n{self.name}"
                f"\n{self.birth}"
                f"\n{self.last_name}"
                f"\n{self.first_name}"
                f"\n{self.age}")


class Manage_Student:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def total_students(self):
        return len(self.students)

    def find_by_full_name(self, full_name):
        return [student for student in self.students if student.name == full_name]

    def find_birthdays_in_current_month(self):
        current_month = datetime.today().month
        return [student for student in self.students if student.birth.month == current_month]

    def sort_by_age(self):
        self.students.sort(key=lambda student: student.age)

    """def display_all_students(self):
        for student in self.students:
            print(student)
            print("-"*30)"""
