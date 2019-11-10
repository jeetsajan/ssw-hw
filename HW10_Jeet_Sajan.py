"""
Created on Sat Nov 9 11:08:01 2019

@author: Jeet Sajan

"""

import HW08_Jeet_Sajan as hw8
from prettytable import PrettyTable as pt
from collections import defaultdict


class Repository:
    """ This class represents a university and it contains the tables for _students and _instructors """

    def __init__(self, directory):
        """ This method is the initialization constructor for class University """
        self._directory = directory
        self.student_table = pt()
        self.student_table.field_names = ["CWID", "Name", "Major", "Completed Courses"]
        self.instructor_table = pt()
        self.instructor_table.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        self.majors_table = pt()
        self.majors_table.field_names = ["Dept", "Required", "Electives"]
        self.student_list = list()
        self.instructor_list = list()
        self.majors_list = list()
        self.analyze_data()

    def get_majors_data(self):
        """ This function gets the majors data and stores it into an instance of prettytable """
        _major = dict()  # Dictionary containing final fields for the instructors prettytable
        _major = defaultdict(lambda: "")
        _majors_file = self._directory + "/majors.txt"
        _majors = list()
        _major_titles = list()
        _aux1 = list()
        _aux2 = list()

        for major, typeof, course in hw8.file_reading_gen(_majors_file, 3, "\t", True):
            _majors.append([major, typeof, course])

        for i in _majors:
            if i[0] not in _major_titles:
                _major_titles.append(i[0])
            if i[1] == 'R':
                _major.setdefault(i[0]+'R', []).append(i[2])
            else:
                _major.setdefault(i[0]+'E', []).append(i[2])

        for i in _major_titles:
            self.majors_table.add_row([i, _major[i + 'R'], _major[i + 'E']])
            self.majors_list.append([i, _major[i + 'R'], _major[i + 'E']])

    def get_instructor_data(self):
        """ This function gets the instructor data and stores it into an instance of prettytable """
        _instructor = dict()  # Dictionary containing final fields for the instructors prettytable
        _instructor = defaultdict(lambda: "")
        _instructor_file = self._directory + "/instructors.txt"
        _grade_file = self._directory + "/grades.txt"
        _instructors = list()  # List containing input fields from instructors.txt
        _aux = dict()
        _grades = list()  # List containing input fields from grades.txt

        for instructor_cwid, instructor_name, dept in hw8.file_reading_gen(_instructor_file, 3, "|", True):
            _instructors.append([instructor_cwid, instructor_name, dept])
        for student_cwid, course, grade, instructor_cwid in hw8.file_reading_gen(_grade_file, 4, "|", True):
            _grades.append([student_cwid, course, grade, instructor_cwid])

        for i in _grades:  # Getting values for instructor prettytable (Course name and Number of students)
            _instructor[i[1]] = list()
            _instructor[i[1]].append(0)
            for j in _grades:
                if i[1] == j[1]:
                    _instructor[i[1]][0] += 1
        for i in _instructors:  # Getting the rest of the values for instructor prettytable (CWID, Name and Dept)
            for j in _grades:
                if i[0] == j[3] and i[1] not in _instructor[j[1]]:
                    _instructor[j[1]].insert(0, i[1])
                    _instructor[j[1]].insert(0, i[0])
                    _instructor[j[1]].insert(2, i[2])
        for key, value in sorted(_instructor.items(),
                                 key=lambda e: e[1][1]):  # Sorting the dictionary according to name
            _aux[key] = value  # Storing the sorted dictionary into a temporary dictionary
        _instructor = _aux
        for key, value in _instructor.items():  # Populating the instructor prettytable
            self.instructor_table.add_row([value[0], value[1], value[2], key, value[3]])
            self.instructor_list.append([value[0], value[1], value[2], key, value[3]])

    def get_student_data(self):
        """ This function gets the student data and stores it into an instance of prettytable """
        _student = dict()  # Dictionary containing final fields for the students prettytable
        _student = defaultdict(lambda: "")
        _student_file = self._directory + "/students.txt"
        _grade_file = self._directory + "/grades.txt"
        _grades = list()  # List containing input fields from grades.txt
        _students = list()  # List containing input fields from students.txt

        for student_cwid, student_name, dept in hw8.file_reading_gen(_student_file, 3, ";", True):
            _students.append([student_cwid, student_name, dept])
        for student_cwid, course, grade, instructor_cwid in hw8.file_reading_gen(_grade_file, 4, "|", True):
            _grades.append([student_cwid, course, grade, instructor_cwid])

        for i in _students:  # Getting values for students prettytable
            _student[i[0]] = list()
            _student[i[0]].append(i[1])
            _student[i[0]].append(i[2])
            for j in _grades:
                if i[0] == j[0]:
                    if j[2] == 'A' or j[2] == 'A-' or j[2] == 'B' or j[2] == 'B-' or j[2] == 'C':
                        _student[i[0]].append(j[1])  # Adding course only if passing requirement is met
        for key, value in _student.items():  # Populating the students prettytable
            self.student_table.add_row([key, value[0], value[1], value[2:]])
            self.student_list.append([key, value[0], value[1], value[2:]])

    def analyze_data(self):
        """ This function gets the data for the table from the three files and populates the table """
        try:
            if self._directory.endswith("/"):
                self._directory[-1] = ""
            self.get_student_data()
            self.get_instructor_data()
            self.get_majors_data()

        except ValueError:
            print("ValueError: One of the data files might have wrong number of fields!")
        except FileNotFoundError:
            print("FileNotFoundError: The files doesn't exist in the directory provided!")

    def print_tables(self):
        """ This function is used inorder to print the student and instructor tables """
        print(self.student_table)
        print(self.instructor_table)
        print(self.majors_table)


def main(directory):
    """ This is the main implementation for HW10_Jeet_Sajan """
    college = Repository(directory)
    college.print_tables()


# main("/Users/jeetsajan/PycharmProjects/SSW810 Assignments/HW10_Jeet_Sajan")
