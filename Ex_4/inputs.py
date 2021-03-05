from school import *


# Students
Jozsi = Student("Jozsi", 1997, "fiu", 4.6, "+3680546543")
Pista = Student("Pista", 1998, "fiu", 2.6, "+3680546542")
Misi = Student("Misi", 1995, "fiu", 4.5, "+3680546545")
Abel = Student("Abel", 2000, "fiu", 4.8, "+3680546524")
Teofil = Student("Teofil", 1996, "lany", 2.5, "+3680546500")
Anasztazia = Student("Anasztazia", 1999, "lany", 4.0, "+3680546540")
Padme = Student("Padme", 1997, "lany", 5.0, "+368050000")
Student_list = [Jozsi, Pista, Misi, Abel, Teofil, Anasztazia, Padme]

# Groups
A = Group("A", [Jozsi, Pista])
B = Group("B", [Misi, Abel, Teofil])
C = Group("C", [Anasztazia, Padme])
Group_list = [A, B, C]

# Subjects
Physics = Subject("Physics", "In this subject we learn physics", A)
PE = Subject("PE", "In this subject we do sports", B)
Math = Subject("Math", "In this subject we learn math", A)
Grammar = Subject("Grammar", "In this subject we learn grammar", C)
Subject_list = [Physics, PE, Math, Grammar]

# Teachers
Marika = Teacher("Marika", 1956, "no", 20, 2000, Physics)
Icuka = Teacher("Icuka", 1958, "no", 35, 2100, Math)
Gizike = Teacher("Gizike", 1955, "no", 40, 1200, Grammar)
Teacher_list = [Marika, Icuka, Gizike]

# Headmasters
Terike = Headmaster("Terike", 1970, "no", 30, 3500, Math, A)
Ferike = Headmaster("Ferike", 1977, "ferfi", 40, 4000, Grammar, B)
Merike = Headmaster("Merike", 1967, "no", 40, 1000, PE, C)
Headmaster_list = [Terike, Ferike, Merike]

# Principal
Pistike = Principal("Pistike", 1980, "ferfi", 30, 5000, [Math], 10000)
Principal_list = [Pistike]

# School
Virag_gimnazium = School(name = "Virág gimnázium",
                         address = "Budapest, Virág u. 1.",
                         principal = Pistike,
                         teachers = [Marika, Icuka, Gizike],
                         headmasters = [Terike, Ferike, Merike],
                         students = [Jozsi, Pista, Misi, Abel, Teofil, Anasztazia, Padme])



print(Virag_gimnazium.calculate_wage())
avg = []
for teacher in Teacher_list:
    avg.append(teacher.call_students_of_teacher_averages())
print(f"The best average: {max(avg)}")

worst_avg = []
for student in Student_list:
    worst_avg.append(student.get_average()[1])
print(f"The worst average: {min(worst_avg)}")

# New people
Bozsi = Student("Bozsi", 1997, "fiu", 3.6, "+3680546543")
Rista = Student("Rista", 1998, "fiu", 1.6, "+3680546542")
Pisi = Student("Pisi", 1995, "fiu", 3.5, "+3680546545")
Kabel = Student("kabel", 2000, "fiu", 5.8, "+3680546524")
Student_list.append(Bozsi)
Student_list.append(Rista)
Student_list.append(Pisi)
Student_list.append(Kabel)


Lucika = Teacher("Lucika", 1656, "no", 20, 2000, PE)
Teacher_list.append(Lucika)

avg = []
for teacher in Teacher_list:
    avg.append(teacher.call_students_of_teacher_averages())
print(f"The best average: {max(avg)}")

worst_avg = []
for student in Student_list:
    worst_avg.append(student.get_average()[1])
print(f"The worst average: {min(worst_avg)}")


