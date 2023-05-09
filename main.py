#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #cписок студентів
        self.teacher = []#1 завдання
    def admit_student(self, student): #зарахування студентів
        self.students.append(student)
        print(f'{student.name} Був доданий до школи {self.name}') #дописати, коли створемо клас
    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name
                                       and s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був знайдений {self.name}')
    #1 завдання
    def add_teacher(self, teacher):
        self.teacher.append(teacher)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f'{self.name} був підвищений {self.grade}')
    def demote(self):
        self.grade -= 1
        print(f'{self.name} був понижений {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'

lisa = Student('Alisa', 6)
masha = Student('Maria', 2)
andriiko = Student('Andriy', 50)
dima = Student('Dmytro', 23)
gleb = Student('Gleb', 100)
my_school = School('ItStep', [lisa, masha, andriiko, dima, gleb])
print('Початкові студенти')
for student in my_school.students:
    print(student)

my_school.admit_student(Student('Bogdan', 3))
my_school.admit_student(Student('Alisa', 6))
print('Оновлення')
for student in my_school.students:
    print(student)

#Практична робота
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes

