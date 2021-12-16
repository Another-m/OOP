
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(sum(list(self.grades.values())[0])/len(list(self.grades.values())[0]),2)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

class  Lecturer(Mentor):
    """Лекторы"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_l = {}
    def received_rate(self, student, course,  grade_l):
        if course in self.grades_l: self.grades_l[course] += [grade_l]
        else: self.grades_l[course] = [grade_l]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции : {round(sum(list(self.grades_l.values())[0])/len(list(self.grades_l.values())[0]),2)}'


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
# cool_lecturer.courses_attached += ['Python']
# cool_lecturer.courses_attached += ['c++']

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