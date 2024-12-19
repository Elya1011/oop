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
                f'Средняя оценка за домашние задания: {sum(self.grades.values()) / len(self.grades)}\n'
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
            if sum(student_1.grades.values()) / len(student_1.grades) > sum(student_2.grades.values()) / len(student_2.grades):
                return f'{student_1.name } {student_1.surname}'
            elif sum(student_1.grades.values()) / len(student_1.grades) < sum(student_2.grades.values()) / len(student_2.grades):
                return f'{student_2.name } {student_2.surname}'
            else:
                return f'Средние оценки за лекции равны'


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
                f"Средняя оценка за лекции: {sum(self.grades.values()) / len(self.grades)}")

    def best_lecturer(self, lecturer_1, lecturer_2):
        if isinstance(lecturer_1, Lecturer) and isinstance(lecturer_2, Lecturer):
            if sum(lecturer_1.grades.values()) / len(lecturer_1.grades) > sum(lecturer_2.grades.values()) / len(lecturer_2.grades):
                return f'{lecturer_1.name} {lecturer_1.surname}'
            elif sum(lecturer_1.grades.values()) / len(lecturer_1.grades) < sum(lecturer_2.grades.values()) / len(lecturer_2.grades):
                return f'{lecturer_2.name} {lecturer_2.surname}'
            else:
                return f'Средние оценки за лекции равны'


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

