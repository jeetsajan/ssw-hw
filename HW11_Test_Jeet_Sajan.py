"""

@author: Jeet Sajan

    Test cases for the file HW11_Jeet_Sajan.py

"""

import unittest
from HW11_Jeet_Sajan import Repository


class TestDataRepository(unittest.TestCase):
    """ Class containing the test functions for HW11_Jeet_Sajan.py """

    def test_repository(self):
        """ This function tests the repository comparing the data inside the prettytables """
        result_student = [["10103", "Jobs, S", "SFEN", ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], "None"],
                          ["10115", "Bezos, J", "SFEN", ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546']],
                          ["10183", "Musk, E", "SFEN", ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546']],
                          ["11714", "Gates, B", "CS", ['CS 546', 'CS 570', 'SSW 810'], [], "None"],
                          ["11717", "Kernighan, B", "CS", [], ['CS 546', 'CS 570'], ['SSW 810', 'SSW 565']]]

        result_instructor = [["98763", "Rowland, J", "SFEN", "SSW 810", 4],
                             ["98763", "Rowland, J", "SFEN", "SSW 555", 1],
                             ["98762", "Hawking, S", "CS", "CS 501", 1],
                             ["98762", "Hawking, S", "CS", "CS 546", 2],
                             ["98762", "Hawking, S", "CS", "CS 570", 1],
                             ["98764", "Cohen, R", "SFEN", "CS 546", 2]]

        result_major = [["SFEN", ['SSW 540', 'SSW 810', 'SSW 555'], ['CS 501', 'CS 546']],
                        ["CS", ['CS 570', 'CS 546'], ['SSW 810', 'SSW 565']]]

        expected_data_retrieved = [('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                                   ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                                   ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                                   ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
                                   ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                                   ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)]

        college = Repository("/Users/jeetsajan/PycharmProjects/SSW810 Assignments/HW11_Jeet_Sajan")
        self.assertEqual(college.student_list, result_student)
        self.assertEqual(college.instructor_list, result_instructor)
        self.assertEqual(college.majors_list, result_major)
        self.assertEqual(college.data_retrieved, expected_data_retrieved)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
