class Person:
    def __init__(self, name, birth_year, gender):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.age = 2021-birth_year
    def how_old_are_you(self):
        return f"I'm {self.age} year-old"


class Student(Person):
    def __init__(self, name, birth_year, gender, average, phone):
        super().__init__(name, birth_year, gender)
        self.average = average
        self.phone = phone

    def get_average(self):
        return self.name, self.average

    def call_name(self):
        return self.name

#ez most jónak tűnik
class Group:
    def __init__(self, group_name, students):
        self.group_name = group_name
        self.students = students

    def call_name(self):
        return self.group_name

    def call_students_in_group(self):
        student_list = []
        for student in self.students:
            student_list.append(student.call_name())
        return student_list

    def call_averages_in_group(self):
        student_averages = []
        for student in self.students:
            student_averages.append([student.get_average()])
        return student_averages

class Subject:
    def __init__(self, name, description, group):
        self.name = name
        self.description = description
        self.group = group

    def call_students_in_subject(self):
        group_name = self.group.call_name()
        student_averages = self.group.call_averages_in_group()
        return group_name, student_averages

    def call_students_averages_in_subject(self):
        return self.group.call_averages_in_group()


class Teacher(Person):
    def __init__(self, name, birth_year, gender, weekly_hours, wage, subjects):
        super(Teacher, self).__init__(name, birth_year, gender)
        self.weekly_hours = weekly_hours
        self.wage = wage
        self.subjects = subjects

    def calculate_wage(self):
        salary = self.wage * self.weekly_hours * 4
        print(f"Teacher {self.name}'s wage is {salary}")
        return salary

    def call_students_of_teacher(self):
        return self.subjects.call_students_in_subject()

    def call_students_of_teacher_averages(self):
        temp = 0
        group_name, student_averages = self.subjects.call_students_in_subject()
        for student in student_averages:
            temp += student[0][1]
            avg = float(temp / len(student_averages))
        print(f"Teacher {self.name}'s students' has an average of {avg}")
        return avg



class Headmaster(Teacher):
    def __init__(self, name, birth_year, gender, weekly_hours, wage, subjects, group):
        super(Headmaster, self).__init__(name, birth_year, gender, weekly_hours, wage, subjects)
        self.group = group

    def call_headmaster_averages(self):
        temp = 0
        students = self.group.call_averages_in_group()
        for student in students:
            temp += student[0][1]
            avg = float(temp / len(students))
        print(f"Headmaster {self.name}'s students' has an average of {avg}")
        return avg


class Principal(Teacher):
    def __init__(self, name, birth_year, gender, weekly_hours, wage, subjects, bonus):
        super(Principal, self).__init__(name, birth_year, gender, weekly_hours, wage, subjects)
        self.bonus = bonus

    def calculate_wage(self):
        salary = self.wage * self.weekly_hours * 4 + self.bonus
        print(f"Principal {self.name}'s wage is {salary}")
        return salary


class School:
    def __init__(self, name, address, principal, teachers, headmasters, students):
        self.name = name
        self.address = address
        self.principal = principal
        self.teachers = teachers
        self.headmasters = headmasters
        self.students = students

    def calculate_wage(self):
        principal_wage = 0
        teacher_wage = 0
        headmaster_wage = 0
        principal_wage += self.principal.calculate_wage()
        for teacher in self.teachers:
            teacher_wage += teacher.calculate_wage()
        for headmasters in self.headmasters:
            headmaster_wage += headmasters.calculate_wage()
        return (f"The {self.name}'s monthly wage is "
                     f"{sum([principal_wage, headmaster_wage, teacher_wage])}")
