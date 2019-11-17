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
        self.student_table.field_names = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required",
                                          "Remaining Electives"]
        self.instructor_table = pt()
        self.instructor_table.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        self.majors_table = pt()
        self.majors_table.field_names = ["Dept", "Required", "Electives"]
        self.student_list = list()
        self.instructor_list = list()
        self.majors_list = list()
        self._student_file = self._directory + "/students.txt"
        self._grade_file = self._directory + "/grades.txt"
        self._instructor_file = self._directory + "/instructors.txt"
        self._majors_file = self._directory + "/majors.txt"
        self._majors = list()  # List containing input fields from majors.txt
        self._instructors = list()  # List containing input fields from instructors.txt
        self._students = list()  # List containing input fields from students.txt
        self._grades = list()  # List containing input fields from grades.txt
        try:
            for major, typeof, course in hw8.file_reading_gen(self._majors_file, 3, "\t", True):
                self._majors.append([major, typeof, course])
            for instructor_cwid, instructor_name, dept in hw8.file_reading_gen(self._instructor_file, 3, "|", True):
                self._instructors.append([instructor_cwid, instructor_name, dept])
            for student_cwid, student_name, dept in hw8.file_reading_gen(self._student_file, 3, ";", True):
                self._students.append([student_cwid, student_name, dept])
            for student_cwid, course, grade, instructor_cwid in hw8.file_reading_gen(self._grade_file, 4, "|", True):
                self._grades.append([student_cwid, course, grade, instructor_cwid])
        except ValueError as e:
            print(e)
            quit()
        except FileNotFoundError as e:
            print(e)
            quit()

        self.analyze_data()

    def get_majors_data(self):
        """ This function gets the majors data and stores it into an instance of prettytable """
        _major = dict()  # Dictionary containing final fields for the instructors prettytable
        _major = defaultdict(lambda: "")
        _major_titles = list()
        _aux1 = list()
        _aux2 = list()

        for i in self._majors:
            if i[0] not in _major_titles:
                _major_titles.append(i[0])
            if i[1] == 'R':
                _major.setdefault(i[0] + 'R', []).append(i[2])
            else:
                _major.setdefault(i[0] + 'E', []).append(i[2])

        for key, value in _major.items():
            value.sort()

        for i in _major_titles:
            self.majors_table.add_row([i, _major[i + 'R'], _major[i + 'E']])
            self.majors_list.append([i, _major[i + 'R'], _major[i + 'E']])

    def get_instructor_data(self):
        """ This function gets the instructor data and stores it into an instance of prettytable """
        _instructor = []
        for i in self._grades:
            if [i[1], i[3], '', '', 0] not in _instructor:
                _instructor.append([i[1], i[3], '', '', 0])
        for i in self._grades:
            for j in _instructor:
                if i[1] == j[0]:
                    j[4] += 1
        for i in self._instructors:
            for j in _instructor:
                if i[0] == j[1]:
                    j[2] = i[1]
                    j[3] = i[2]
        _instructor = sorted(_instructor, key=lambda l: l[2], reverse=True)
        for i in _instructor:
            self.instructor_table.add_row([i[1], i[2], i[3], i[0], i[4]])
            self.instructor_list.append([i[1], i[2], i[3], i[0], i[4]])

    def get_student_data(self):
        """ This function gets the student data and stores it into an instance of prettytable """
        _student = dict()  # Dictionary containing final fields for the students prettytable
        _student = defaultdict(lambda: "")
        _aux = list()
        _aux1 = list()
        _aux2 = list()
        _aux_dict1 = dict()
        _aux_dict2 = dict()

        for i in self._students:  # Getting values for students prettytable
            _aux = [list()]
            cnt = 0
            _student[i[0]] = list()
            _student[i[0]].append(i[1])
            _student[i[0]].append(i[2])
            for j in self._grades:
                if i[0] == j[0]:
                    if j[2] == 'A' or j[2] == 'A-' or j[2] == 'B+' or j[2] == 'B' or j[2] == 'B-' or j[2] == 'C+' or \
                            j[2] == 'C':
                        _aux[cnt].append(j[1])  # Adding course only if passing requirement is met
            _aux[cnt].sort()
            _student[i[0]].append(_aux[cnt])
            cnt += 1
        _aux_dict1 = _student
        for key, value in _student.items():  # Adding remaining required courses
            _aux1 = [list()]
            cnt = 0
            for i in self.majors_list:
                if value[1] == i[0]:
                    for j in i[1]:
                        if j not in value[2]:
                            _aux1[cnt].append(j)
                    _aux1[cnt].sort()
                    _aux_dict1[key].append(_aux1[cnt])
                    cnt += 1
        _student = _aux_dict1
        _aux_dict2 = _aux_dict1
        for key, value in _student.items():  # Adding remaining required courses
            _aux2 = [list()]
            cnt = 0
            for i in self.majors_list:
                if value[1] == i[0]:
                    for j in i[2]:
                        if j in value[2]:
                            cnt = 1
                            break
                    if cnt == 1:
                        cnt = 0
                        _aux_dict2[key].append("None")
                    else:
                        _aux_dict2[key].append(i[2])
        _student = _aux_dict2
        for key, value in _student.items():  # Populating the students prettytable
            self.student_table.add_row([key, value[0], value[1], value[2], value[3], value[4]])
            self.student_list.append([key, value[0], value[1], value[2], value[3], value[4]])

    def invalid_check(self):
        """ This function checks if there are no invalid or unconventional input cases """
        for i in self._grades:  # Student in grades.txt doesn't exist in students.txt
            flag = False
            for j in self._students:
                if i[0] in j:
                    flag = True
            if not flag:
                raise ValueError(i[0] + " is an invalid Student CWID in grades.txt!")
        for i in self._grades:  # Instructor in grades.txt doesn't exist in instructors.txt
            flag = False
            for j in self._instructors:
                if i[3] in j:
                    flag = True
            if not flag:
                raise ValueError(i[3] + " is an invalid Instructor CWID in grades.txt!")
        for i in self._students:
            flag = False
            for j in self._majors:
                if i[2] in j:
                    flag = True
            if not flag:
                raise ValueError("In students.txt, " + i[1] + " has an invalid major " + i[2] + "!")

    def analyze_data(self):
        """ This function gets the data for the table from the three files and populates the table """
        try:
            if self._directory.endswith("/"):
                self._directory[-1] = ""
            self.invalid_check()
            self.get_majors_data()
            self.get_student_data()
            self.get_instructor_data()

        except ValueError as e:
            print(e)
            quit()
        except FileNotFoundError as e:
            print(e)
            quit()

    def print_tables(self):
        """ This function is used inorder to print the student and instructor tables """
        print(self.majors_table)
        print(self.student_table)
        print(self.instructor_table)


def main(directory):
    """ This is the main implementation for HW10_Jeet_Sajan """
    college = Repository(directory)
    college.print_tables()


main("/Users/jeetsajan/PycharmProjects/SSW810 Assignments/test")
