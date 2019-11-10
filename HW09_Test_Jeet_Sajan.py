"""
Created on Sat Nov 2 10:12:09 2019

@author: Jeet Sajan

    Test cases for the file HW09_Jeet_Sajan.py

"""

import unittest
from HW09_Jeet_Sajan import Repository


class TestDataRepository(unittest.TestCase):
    """ Class containing the test functions for HW09_Jeet_Sajan.py """

    def test_repository(self):
        """ This function tests the repository comparing the student and instructor prettytables """
        result_student = [["10103", "Baldwin, C", ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501']],
                               ["10115", "Wyatt, X", ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545']],
                               ["10172", "Forbes, I", ['SSW 555', 'SSW 567']],
                               ["10175", "Erickson, D", ['SSW 567', 'SSW 564', 'SSW 687']],
                               ["10183", "Chapman, O", ['SSW 689']],
                               ["11399", "Cordova, I", ['SSW 540']],
                               ["11461", "Wright, U", ['SYS 800', 'SYS 750', 'SYS 611']],
                               ["11658", "Kelly, P", ['SSW 540']],
                               ["11714", "Morton, A", ['SYS 611', 'SYS 645']],
                               ["11788", "Fuller, E", ['SSW 540']]]

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

        college = Repository("/Users/jeetsajan/PycharmProjects/SSW810 Assignments/HW09_Jeet_Sajan")
        self.assertEqual(college.student_list, result_student)
        self.assertEqual(college.instructor_list, result_instructor)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
