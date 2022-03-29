import grade as grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_grade(self, lecturer, student, course, grade):
        is_lecturer = isinstance(lecturer, Lecturer)
        if not is_lecturer:
            print("Преподаватель не является лектором")
        is_real_student = isinstance(student, Student)
        if not is_real_student:
            print("Переданный объект не является студентом")
        can_mentor_get_grades = course in lecturer.courses_attached
        if not can_mentor_get_grades:
            print("Преподаватель не ведет этот курс")
        is_course_of_student = course in student.courses_in_progress
        if not is_course_of_student:
            print("Студент не проходит этот курс")
        if is_lecturer and is_real_student and can_mentor_get_grades and is_course_of_student:
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] += [grade]
            else:
                lecturer.grades_for_lecturer[course] = [grade]
        else:
            print('Ошибка')

    def avg_grade(self, grades):
        summa = 0
        count = 0
        for k, v in grades.items():
            summa = summa + sum(v)
            count = count + len(v)
        sum_average = summa / count
        return sum_average

    def __str__(self):
        result = f"Имя: {self.name}\n"
        result = result + f"Фамилия: {self.surname}\n"
        average_grade_hw = self.avg_grade(self.grades)
        result = result + f"Средняя оценка за домашние задания: {average_grade_hw}\n"
        result = result + f"Курсы в процессе изучения: {(', '.join(self.courses_in_progress))}\n"
        result = result + f"Завершенные курсы: {(', '.join(self.finished_courses))}"
        return result

    def __lt__(self, other):  # <
        my_avg_grade = self.avg_grade(self.grades)
        other_avg_grade = other.avg_grade(other.grades)
        return my_avg_grade < other_avg_grade

    def __le__(self, other):  # <=
        return self.avg_grade(self.grades) <= other.avg_grade(other.grades)

    def __eq__(self, other):  # ==
        return self.avg_grade(self.grades) == other.avg_grade(other.grades)

    def __ne__(self, other):  # !=
        return self.avg_grade(self.grades) != other.avg_grade(other.grades)

    def __gt__(self, other):  # >
        return self.avg_grade(self.grades) > other.avg_grade(other.grades)

    def __ge__(self, other):  # >=
        return self.avg_grade(self.grades) >= other.avg_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        is_reviewer = isinstance(self, Reviewer)
        if not is_reviewer:
            print("Преподаватель не является экспертом")
        is_real_student = isinstance(student, Student)
        if not is_real_student:
            print("Переданный объект не является студентом")
        can_mentor_set_grades = course in self.courses_attached
        if not can_mentor_set_grades:
            print("Преподаватель не ведет этот курс")
        is_course_of_student = course in student.courses_in_progress
        if is_course_of_student == False:
            print("Студент не проходит этот курс")
        if is_reviewer and is_real_student and can_mentor_set_grades and is_course_of_student:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')


class Lecturer(Mentor):
    def __init__(self, name, surname,):
        super().__init__(name, surname)
        self.grades_for_lecturer = {}

    def avg_grade(self, grades):
        summa = 0
        count = 0
        for k, v in grades.items():
            summa = summa + sum(v)
            count = count + len(v)
        sum_average = summa / count
        return sum_average

    def __str__(self):
        result = f"Имя: {self.name}\n"
        result = result + f"Фамилия: {self.surname}\n"
        average_grade = self.avg_grade(self.grades_for_lecturer)
        result = result + f"Средняя оценка за лекции: {average_grade}"
        return result

    def __lt__(self, other): # <
        my_avg_grade = self.avg_grade(self.grades_for_lecturer)
        other_avg_grade = other.avg_grade(other.grades_for_lecturer)
        return my_avg_grade < other_avg_grade

    def __le__(self, other):  # <=
        return self.avg_grade(self.grades_for_lecturer) <= other.avg_grade(other.grades_for_lecturer)

    def __eq__(self, other):  # ==
        return self.avg_grade(self.grades_for_lecturer) == other.avg_grade(other.grades_for_lecturer)

    def __ne__(self, other):  # !=
        return self.avg_grade(self.grades_for_lecturer) != other.avg_grade(other.grades_for_lecturer)

    def __gt__(self, other):  # >
        return self.avg_grade(self.grades_for_lecturer) > other.avg_grade(other.grades_for_lecturer)

    def __ge__(self, other):  # >=
        return self.avg_grade(self.grades_for_lecturer) >= other.avg_grade(other.grades_for_lecturer)

class Reviewer(Mentor):
    def __str__(self):
        result = f"Имя: {self.name}\n"
        result = result + f"Фамилия: {self.surname}"

        return result



best_student = Student('Ruoy', 'Eman', 'Female')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Java']

second_student = Student('Ivan', 'Ivanov', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
second_student.finished_courses += ['Git']

first_reviewer = Reviewer('Дмитрий', 'Дмитриев')
first_reviewer.courses_attached += ['Python', 'Java']

first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 5)
first_reviewer.rate_hw(second_student, 'Java', 8)
first_reviewer.rate_hw(second_student, 'Python', 3)

second_reviewer = Reviewer('Темоте', 'Шаломе')
second_reviewer.courses_attached += ['Python', 'Git']

second_reviewer.rate_hw(best_student, 'Python', 10)
second_reviewer.rate_hw(best_student, 'Python', 9)
second_reviewer.rate_hw(best_student, 'Git', 8)
second_reviewer.rate_hw(best_student, 'Python', 10)

first_lecturer = Lecturer('Олег', 'Газманов')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Java']

second_lecturer = Lecturer('Albert', 'Lobov')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

best_student.rate_grade(second_lecturer, best_student, 'Git', 10)
best_student.rate_grade(second_lecturer, best_student, 'Git', 5)
best_student.rate_grade(second_lecturer, best_student, 'Git', 3)

second_student.rate_grade(first_lecturer, second_student, 'Python', 10)
second_student.rate_grade(first_lecturer, second_student, 'Python', 9)
second_student.rate_grade(first_lecturer, second_student, 'Python', 5)


print("=======")
print(best_student)
print("=======")
print(second_student)
print("=======")
print(first_reviewer)
print("=======")
print(second_reviewer)
print("=======")
print(first_lecturer)
print("=======")
print(second_lecturer)
print("=======")


def avarege_grade_course(students, course_name):
    summa = 0
    count = 0
    for student in students:
        for k, v in student.grades.items():
            if course_name != k:
                continue
            summa = summa + sum(v)
            count = count + len(v)
    return summa / count

students = [best_student, second_student]
course_name = 'Python'

print(avarege_grade_course(students, 'Python'))
print(avarege_grade_course(students, 'Git'))
print(avarege_grade_course(students, 'Java'))
print("=======")

def avarege_grade_lectures(mentors, course_name):
    summa = 0
    count = 0
    for lecturer in mentors:
        for k, v in lecturer.grades_for_lecturer.items():
            if course_name != k:
                continue
            summa = summa + sum(v)
            count = count + len(v)
    return summa / count

mentors = [first_lecturer, second_lecturer]
course_name = 'Python'

print(avarege_grade_lectures(mentors, 'Python'))
print(avarege_grade_lectures(mentors, 'Git'))
