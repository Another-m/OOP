
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_value(self):
        return round(sum(list(self.grades.values())[0])/len(list(self.grades.values())[0]), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_value()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, (int, float, Student)):
            print("Not a Student!")
            return
        return self.average_value() < other.average_value()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


class Lecturer(Mentor):
    """Лекторы"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_l = {}
    def received_rate(self, student, course,  grade_l):
        if course in self.grades_l: self.grades_l[course] += [grade_l]
        else: self.grades_l[course] = [grade_l]

    def average_value(self):
        return round(sum(list(self.grades_l.values())[0])/len(list(self.grades_l.values())[0]),2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции : {self.average_value()} '

    def __lt__(self, other):
        if not isinstance(other, (int, float, Lecturer)):
            print("Not a Reviewer!")
            return
        return self.average_value() < other.average_value()

class Reviewer(Mentor):
    """Эксперты, проверяющие домашние задания"""

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Bill', 'Gates')
cool_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_lecturer.received_rate(best_student, 'Python', 5)
cool_lecturer.received_rate(best_student, 'c++', 5)
cool_lecturer.received_rate(best_student, 'c++', 4)

print(f"{best_student.name} {best_student.surname}: предмет: {list(best_student.grades.keys())} оценки: {list(best_student.grades.values())}")
print(f"{cool_lecturer.name} {cool_lecturer.surname}: предмет: {list(cool_lecturer.grades_l.keys())} оценки: {list(cool_lecturer.grades_l.values())}")

print(best_student)
print()
print(cool_mentor)
print()
print(cool_lecturer)
print('---------------------')

some_student = Student('Ruby', 'Jik', '22')
some_student.courses_in_progress += ['Python']
some_mentor = Reviewer('George', 'Bild')
some_mentor.courses_attached += ['Python']
some_lecturer = Lecturer('Steve', 'Jobs')
some_lecturer.courses_attached += ['Python']
some_mentor.rate_hw(some_student, 'Python', 3)
some_mentor.rate_hw(some_student, 'Python', 4)
some_lecturer.received_rate(some_student, 'Python', 3)

print(some_student)
print()
print(some_mentor)
print()
print(some_lecturer)
print(cool_lecturer > some_lecturer)
print(best_student < some_student)
print('---------------------')


stud_list = [best_student, some_student]
lect_list = [cool_lecturer, some_lecturer]

def average_rate_student(stud_list, courses):
    result = 0
    for student in stud_list:
        if courses in student.courses_in_progress:
            result += student.average_value()
    result = result/len(stud_list)
    print(f" Средний балл сдудентов кураса {courses}: {result}")


def average_rate_lecturers(lect_list, courses):
    result = 0
    for lecturer in lect_list:
        if courses in lecturer.courses_attached:
            result += lecturer.average_value()
    result = result/len(lect_list)
    print(f" Средний балл лекторов кураса {courses}: {result}")

average_rate_student(stud_list, 'Python')
average_rate_lecturers(lect_list, 'Python')