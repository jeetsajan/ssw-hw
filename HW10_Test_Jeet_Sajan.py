"""
Created on Sat Nov 9 11:09:11 2019

@author: Jeet Sajan

    Test cases for the file HW10_Jeet_Sajan.py

"""

import unittest
from HW10_Jeet_Sajan import Repository


class TestDataRepository(unittest.TestCase):
    """ Class containing the test functions for HW09_Jeet_Sajan.py """

    def test_repository(self):
        """ This function tests the repository comparing the student and instructor prettytables """
        result_student = [["10103", "Baldwin, C", "SFEN", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],
                           ['SSW 540', 'SSW 555'], "None"],
                          ["10115", "Wyatt, X", "SFEN", ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'],
                           ['SSW 540', 'SSW 555'], "None"],
                          ["10172", "Forbes, I", "SFEN", ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'],
                           ['CS 501', 'CS 513', 'CS 545']],
                          ["10175", "Erickson, D", "SFEN", ['SSW 564', 'SSW 567', 'SSW 687'],
                           ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545']],
                          ["10183", "Chapman, O", "SFEN", ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564',
                                                                        'SSW 567'],
                           ['CS 501', 'CS 513', 'CS 545']],
                          ["11399", "Cordova, I", "SYEN", ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], "None"],
                          ["11461", "Wright, U", "SYEN", ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'],
                           ['SSW 540', 'SSW 565', 'SSW 810']],
                          ["11658", "Kelly, P", "SYEN", [], ['SYS 612', 'SYS 671', 'SYS 800'],
                           ['SSW 540', 'SSW 565', 'SSW 810']],
                          ["11714", "Morton, A", "SYEN", ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'],
                           ['SSW 540', 'SSW 565', 'SSW 810']],
                          ["11788", "Fuller, E", "SYEN", ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], "None"]]

        result_instructor = [["98760", "Darwin, C", "SYEN", "SYS 800", 1],
                             ["98760", "Darwin, C", "SYEN", "SYS 750", 1],
                             ["98760", "Darwin, C", "SYEN", "SYS 611", 2],
                             ["98760", "Darwin, C", "SYEN", "SYS 645", 1],
                             ["98765", "Einstein, A", "SFEN", "SSW 567", 4],
                             ["98765", "Einstein, A", "SFEN", "SSW 540", 3],
                             ["98764", "Feynman, R", "SFEN", "SSW 564", 3],
                             ["98764", "Feynman, R", "SFEN", "SSW 687", 3],
                             ["98764", "Feynman, R", "SFEN", "CS 501", 1],
                             ["98764", "Feynman, R", "SFEN", "CS 545", 1],
                             ["98763", "Newton, I", "SFEN", "SSW 555", 1],
                             ["98763", "Newton, I", "SFEN", "SSW 689", 1]]

        result_major = [["SFEN", ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                        ["SYEN", ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        college = Repository("/Users/jeetsajan/PycharmProjects/SSW810 Assignments/HW10_Jeet_Sajan")
        self.assertEqual(college.student_list, result_student)
        self.assertEqual(college.instructor_list, result_instructor)
        self.assertEqual(college.majors_list, result_major)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
