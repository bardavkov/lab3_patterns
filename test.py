import unittest

import unittest
from main import *
class Test_student(unittest.TestCase):
    def setUp(self):
        self.assignment_2 = {"title": "testing", "description": "testing", "is_done": True, "mark": 0.0}
        self.student_1 = Student(1, 'lol', 'bardakov', 2000)
        self.enr = Enrollment('loll')
        self.programing_course = Programing('cpp', assignment_2, 50, 67)
        self.matan_prepod = ProgramingLecturer(1, 'Bogdan', 'Koman', 20)
        self.prepod = MathLecturer(1, 'Taras', 'Taras', 20)


    def test_1_1(self):
        a = self.enr.enroll(self.student_1, self.programing_course)

        self.assertEqual(a, 'Student lol enrolled to cpp PROGRAMMING course')

    def test_1_2(self):
        b = self.matan_prepod.create_course(programing_course)
        self.assertEqual(b, '!!!PROGRAMING!!! Course cpp are created by Bogdan Koman')

    def test_1_3(self):
        c = self.prepod.create_course(programing_course)
        self.assertEqual(c, 'ERROR!!!!!! ONLY MATH COURSE!!!!!!!!'  )






