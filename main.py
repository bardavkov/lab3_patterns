from datetime import datetime
from typing import List, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod
import random

'''dataclass for info ab students and lecturers '''


@dataclass
class personal_info:
    id: int
    name: str
    surname: str
    # adress: str
    # phone_number: str
    # position: str
    # rank: str
    salary: float


'''you can send all your requests to department'''


class Department:
    def __init__(self, title: str):
        self.students: List[Student] = []
        self.lecturers: List[Lecturer] = []
        self.courses: List[Course.title] = []
        self.requests: List[Any] = []
        self.ill_requests: List[Any] = []

    def proceed_requests(self):
        return self.requests


class Course:  # info abt course

    @abstractmethod
    def __init__(self, title: str,
                 assignments: list[str],  students_num: int, students_limit: int):
        self.title = title
        self.limit = students_limit

        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []

    # function for add students to list
    @abstractmethod
    def add_student(self, student: List):
        pass

    # function for removing students from list
    @abstractmethod
    def delete_student(self, student):
        pass


# bridge between student\lecturer and department
class staff(personal_info):

    @abstractmethod
    def ask_sick_alive(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass


class Student(staff):
    average_mark = 0
    course_progress = [1, 2, 5, 7]
    courses: List[Course] = []

    def send_request(self, department: Department) -> bool:
        a = input('write request : ')
        department.requests.append(f'student {self.name} want a {a}')

    def ask_sick_alive(self, department: Department):
        department.ill_requests.append(f'student {self.name} is ill')
        rand = bool(random.getrandbits(1))
        if rand is True:
            return print(f'{self.name} are free')
        else:
            return print('sit on your lectures')

    def taken_courses(self):
        return print(f'{self.courses}')


class PostGraduateStudent(Student):
    pass


# class Lecturer inherit personal_info
class Lecturer(personal_info):
    average_mark = 0
    post_students: List[PostGraduateStudent] = []

    def check_assignment(self, assignment: dict) -> None:
        if assignment["is_done"]:
            assignment["mark"] = 5.0

    def ask_sick_alive(self, department: Department) -> bool:
        return print(department.ill_requests)

    def send_request(self, department: Department):
        return print(department.requests)

    def add_postgraduate_student(self, pst_student: PostGraduateStudent):
        self.post_students.append(pst_student)

    @abstractmethod
    def create_course(self, course):
        pass


# new class
class Seminars:
    def __init__(self, id):
        self.id = id

        title = ' '
        assignments: List[dict] = []
        related_course: str = ' '

        def implement_item(self, lol):
            pass


class CourseProgres:
    """ course progres of chosen student """

    def __init__(self, received_marks: dict,
                 visited_lectures: int,
                 assignment: dict):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.assignments = {}
        self.assignment = assignment

    # marks are taken from received marks
    def get_final_mark(self) -> float:
        final_mark = sum(self.received_marks.values()) / len(self.received_marks)
        return final_mark


# class for enroll on courses (bridge between student and course classes)
class Enrollment:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def enroll(student: Student, course: Course):
        student.courses.append(course)
        print(f'Student {student.name} enrolled to {course.title} {course.type} course')
        return f'Student {student.name} enrolled to {course.title} {course.type} course'



    @staticmethod
    def unenroll(student: Student, course: Course):
        student.courses.remove(course)
        # self.courses = list(filter(lambda x: x.title == course_title, self.courses))
        print(f'Student {student.name} unenrolled from {course.title} {course.type} course')


# dataclass group
@dataclass
class Group:
    id: int
    title: str
    student_list: list
    department_id: int


class Math(Course):
    def __init__(self, title: str,
                 assignments: list[str],  students_num: int, students_limit: int):
        self.title = title
        self.limit = students_limit
        self.type = 'MATH'
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f'Student {student.name} as been added to the MATH!! course {self.title}')
        else:
            print('Too many students in !!!MATH!!! course')

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f'student {student.name} are removed from the {self.title} !!!MATH COURSE!!!')


class Algorithms(Course):
    def __init__(self, title: str,
                 assignments: list[str], limit: int, students_num: int, students_limit: int):
        self.title = title
        self.limit = students_limit
        self.type = 'ALGORITHMS'
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f'Student {student.name} as been added to the ALGORITHMS!! course {self.title}')
        else:
            print('Too many students in !!!ALGORITHMS!!! course')

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f'student {student.name} are removed from the {self.title} !!!ALGORITHMS COURSE!!!')


class Programing(Course):
    def __init__(self, title: str,
                 assignments: list[str],  students_num: int, students_limit: int):
        self.title = title
        self.limit = students_limit
        self.type = 'PROGRAMMING'
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f'Student {student.name} as been added to the PROGRAMMING!! course {self.title}')
        else:
            print('Too many students in !!!PROGRAMMING!!! course')

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f'student {student.name} are removed from the {self.title} !!!PROGRAMMING COURSE!!!')



class MathLecturer(Lecturer):
    def create_course(self, math: Math):
        if math.type != 'MATH':
            print('ERROR!!!!!! ONLY MATH COURSE!!!!!!!!')
            return 'ERROR!!!!!! ONLY MATH COURSE!!!!!!!!'
        else:
            print(f"!!!MATH!!! Course {math.title} are created by {self.name} {self.surname}")
            return f"!!!PROGRAMING!!! Course {math.title} are created by {self.name} {self.surname}"


class AlgorithmsLecturer(Lecturer):
    def create_course(self, algo: Algorithms):
        if algo.type != 'ALGORITHMS':
            print('ERROR!!!!!! ONLY ALGORITHMS COURSE!!!!!!!!')
        else:
            print(f"!!!ALGO!!! Course {algo.title} are created by {self.name} {self.surname}")
            return f"!!!ALGO!!! Course {algo.title} are created by {self.name} {self.surname}"

class ProgramingLecturer(Lecturer):
    def create_course(self, prog: Programing):
        if prog.type != 'PROGRAMMING':
            print('ERROR!!!!!! ONLY PROGRAMING COURSE!!!!!!!!')
        else:
            print(f"!!!PROGRAMING!!! Course {prog.title} are created by {self.name} {self.surname}")
            return f"!!!PROGRAMING!!! Course {prog.title} are created by {self.name} {self.surname}"




assignment_2 = {"title": "testing", "description": "testing", "is_done": True, "mark": 0.0}
student_1 = Student(1, 'lol', 'bardakov', 2000)
prepod = MathLecturer(1, 'Bogdan', 'Koman', 20)
enr = Enrollment('loll')
programing_course = Programing('cpp', assignment_2, 50, 67)
matan_prepod = ProgramingLecturer(1, 'Bogdan', 'Koman', 20)
enr.enroll(student_1, programing_course)
matan_prepod.create_course(programing_course)
prepod.create_course(programing_course)