class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {','.join(self.finished_courses)}')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def best_student(self, student_1, student_2):
        if isinstance(student_1, Student) and isinstance(student_2, Student):
            if student_1.avg_grade() > student_2.avg_grade():
                return f'{student_1.name} {student_1.surname}'
            elif student_1.avg_grade() < student_2.avg_grade():
                return f'{student_2.name} {student_2.surname}'
            else:
                return f'Средние оценки за лекции равны'

    def avg_grade(self):
        result = []
        for grade_list in self.grades.values():
            result += grade_list
        return sum(result) / len(result)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"имя: {self.name}\n"
                f"фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_grade()}")

    def best_lecturer(self, lecturer_1, lecturer_2):
        if isinstance(lecturer_1, Lecturer) and isinstance(lecturer_2, Lecturer):
            if lecturer_1.avg_grade() > lecturer_2.avg_grade():
                return f'{lecturer_1.name} {lecturer_1.surname}'
            elif lecturer_1.avg_grade() < lecturer_2.avg_grade():
                return f'{lecturer_2.name} {lecturer_2.surname}'
            else:
                return f'Средние оценки за лекции равны'

    def avg_grade(self):
        result = []
        for grade_list in self.grades.values():
            result += grade_list
        return sum(result) / len(result)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"имя: {self.name}\n"
                f"фамилия: {self.surname}")

student_1 = Student('Maxim', 'One', 'male')
student_1.finished_courses = ['IB']
student_1.courses_in_progress = ['PY', 'Git']
student_2 = Student('Roma', 'Two', 'male')
student_2.finished_courses = ['PY']
student_2.courses_in_progress = ['IB', 'Git']

lecturer_1 = Lecturer('Alina', 'Max')
lecturer_1.courses_attached = ['PY', 'Git']
lecturer_2 = Lecturer('Peter', 'Parker')
lecturer_2.courses_attached = ['IB', 'Git', 'PY']

reviewer_1 = Reviewer('Oleg', 'Korzun')
reviewer_1.courses_attached = ['PY', 'Git']
reviewer_1.rate_student(student_1, 'PY', 7)
reviewer_1.rate_student(student_1, 'PY', 5)
reviewer_1.rate_student(student_1, 'Git', 5)
reviewer_2 = Reviewer('Mika', 'Morty')
reviewer_2.courses_attached = ['IB', 'Git']
reviewer_2.rate_student(student_2, 'Git', 10)
reviewer_2.rate_student(student_2, 'Git', 10)

student_1.rate_lecturer(lecturer_1, 'PY', 5)
student_1.rate_lecturer(lecturer_1, 'PY', 10)
student_1.rate_lecturer(lecturer_1, 'PY', 7)
student_1.rate_lecturer(lecturer_1, 'Git', 6)
student_2.rate_lecturer(lecturer_2, 'Git', 3)
student_2.rate_lecturer(lecturer_2, 'Git', 3)
student_2.rate_lecturer(lecturer_2, 'Git', 2)
student_2.rate_lecturer(lecturer_2, 'PY', 7)


print(f"Данные студентов\n"
      f"{student_1}\n\n"
      f"{student_2}\n\n"
      f"Лучший студент: {student_1.best_student(student_1, student_2)}\n\n"
      f"Данные лекторов\n"
      f"{lecturer_1}\n\n"
      f"{lecturer_2}\n\n"
      f"Лучший лектор: {lecturer_1.best_lecturer(lecturer_1, lecturer_2)}\n\n"
      f"Данные проверяющих\n"
      f"{reviewer_1}\n\n"
      f"{reviewer_2}")


def all_student_avg(students, course):
    result = []
    for student in students:
        if course in student.courses_in_progress:
            result += student.grades[course]
    return sum(result) / len(result)

print(f"средняя оценка за дз по всем студентам в рамках курса {all_student_avg([student_1, student_2], 'Git')}")

def all_lecturers_avg(lecturers, course):
    result = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            result += lecturer.grades[course]
    return sum(result) / len(result)

print(f"средняя оценка за дз по всем лекторам в рамках курса {all_lecturers_avg([lecturer_1, lecturer_2], 'Git')}")

