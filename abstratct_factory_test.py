import unittest
from abstract_factory import *

class Test_abstract_factory(unittest.TestCase):
    def setUp(self):
        self.assignment_2 = {"title": "testing", "description": "testing", "is_done": True, "mark": 0.0}
        self.student_1 = Student(1, 'lol', 'bardakov', 2000)
        self.enr = Enrollment()
        self.lisst = []
        self.course = Algorithms('heaps', self.assignment_2, 50, 99, 67)
        self.prepod_1 = AlgorithmsLecturer(1, 'Bogdan', 'Koman', 20)
        self.prepod_2 = MathLecturer(1, 'Taras', 'Taras', 20)
        self.group_algos = AlgorithmsGroup(1, 'matan', self.lisst, 0)

    def test_1(self):
        a = self.prepod_1.create_course(self.course, self.group_algos)
        self.assertEqual(a, '!!!ALGO!!! Course heaps are created by Bogdan Koman')


    def test_2(self):
        c = self.prepod_2.create_course(self.course, self.group_algos)
        self.assertEqual(c, 'ERROR!!!!!! ONLY MATH COURSE!!!!!!!!')



    def test_3(self):
        b = self.enr.enroll(self.student_1, self.course, self.group_algos)
        self.assertEqual(b, 'Student lol enrolled to heaps ALGORITHMS course')




