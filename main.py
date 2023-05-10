#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #cписок студентів
        self.teacher = []#1 завдання
        self.classes = [] #2 завдання
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
    #2 завдання
    def add_class(self, class_obj):
        self.classes.append(class_obj)
        print(f'Клас {class_obj.number} був доданий до школи {self.name}')
    #3 завдання
    def get_students_by_grade(self, grade):
        grade_students = [student for student in self.students if student.grade == grade]
        return grade_students

    def get_school_statistics(self):
        total_students = len(self.students)
        average_grade = sum(student.grade for student in self.students) / total_students
        print(f'Статистика школи {self.name}:')
        print(f'Загальна кількість студентів: {total_students}')
        print(f'Середній рівень (бал): {average_grade}')
        print('Статистика класів:')
        for class_obj in self.classes:
            class_obj.get_average_grade()
    def __str__(self):
        return self.name
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
#Друге завдання
class Class:
    def __init__(self, number, students):
        self.number = number
        self.students = students
    def add_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до класу {self.number}')
    def get_average_grade(self):
        total_students = len(self.students)
        average_grade = sum(student.grade for student in self.students) / total_students
        print(f'Середній рівень (бал) для класу {self.number}: {average_grade}')

itstep_teacher = Teacher('Albina', 'Python', ['Class A', 'Class B'])
my_school.add_teacher(itstep_teacher)
print()
class1 = Class(1, [lisa, masha])
my_school.add_class(class1)
my_school.get_school_statistics()