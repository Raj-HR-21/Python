"""
2.Write a Python script that analyzes a text file containing student grades and generates a comprehensive report. (7 marks)
Input CSV Format:
csv
StudentID,Name,Math,Physics,Chemistry,Biology
S001,Alice Johnson,85,90,88,92
S002,Bob Smith,78,82,75,80
S003,Carol White,92,88,95,90
S004,David Brown,70,68,72,75

Requirements:
Read the CSV file
Create a class Student to store each student's information
Calculate individual student averages
Generate a report showing:
Total number of students
Class average for each subject
Overall class average
Top 3 students by overall average
Students who scored above 90 in any subject
Subject-wise highest and lowest scores

Handle file not found exceptions
Write formatted output to a text file
"""

# write student data to file
with open('student.csv', 'w') as f:
    f.write('StudentID,Name,Math,Physics,Chemistry,Biology\n')
    f.write('S001,Alice Johnson,85,90,88,92 \n')
    f.write('S002,Bob Smith,78,92,75,80 \n')
    f.write('S003,Carol White,92,88,95,90 \n')
    f.write('S004,David Brown,70,68,72,75 \n')


class Student:
    def __init__(self, sid, name, math, physics, chemistry, biology):
        self.sid = sid
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology

    def average(self):
        return ((self.math + self.physics + self.chemistry + self.biology)/4)

# to store each student information
students = []

# read from csv
with open('student.csv', 'r') as f:
    student_info = f.readline()
    for line in f:
        line = line.strip()
        info = line.split(',')
        sid =  info[0]
        name = info[1]
        math = int(info[2])
        physics = int(info[3])
        chemistry = int(info[4])
        biology = int(info[5])

        #for i in student_info:
        students.append(Student(sid, name, math, physics, chemistry, biology))

num_of_students = len(students)

# each subject average
math_avg = sum(i.math for i in students)/num_of_students
physics_avg = sum(i.physics for i in students)/num_of_students
chemistry_avg = sum(i.chemistry for i in students)/num_of_students
biology_avg = sum(i.biology for i in students)/num_of_students

# overall class average
overall_average = sum(i.average() for i in students)/num_of_students

# top 3 students
sorted_list = sorted(students, key = lambda x : x.average(), reverse=True)
top_3 = sorted_list[:3]

# above 90 in any subject
above_90 = [s for s in students if s.math > 90 or s.physics > 90 or s.chemistry > 90 or s.biology > 90]

# subject wise scores
math_score = [s.math for s in students]
physics_score = [s.physics for s in students]
chemistry_score = [s.chemistry for s in students]
biology_score = [s.biology for s in students]
math_highest, math_lowest = max(math_score), min(math_score)
physics_highest, physics_lowest = max(physics_score), min(physics_score)
chemistry_highest, chemistry_lowest = max(chemistry_score), min(chemistry_score)
biology_highest, biology_lowest = max(biology_score), min(biology_score)

# write report to text file
with open('report.txt', 'w') as f:
    f.write(f"Total No., of Students: {num_of_students} \n")
    f.write('\nAverage \n')
    f.write(f"  Math : {math_avg}\n  Physics : {physics_avg}\n  Chemistry : {chemistry_avg}\n  Biology : {biology_avg}\n ")
    f.write(f"Class Average : {overall_average}\n")
    f.write("Top 3 Students \n")
    for s in top_3:
        f.write(f"  {s.sid} | ({s.name}) ({s.average()})\n")
    f.write("Above 90 \n")
    for s in above_90:
        f.write(f"  {s.sid} | ({s.name})\n")
    f.write("Subject-wise highest and lowest \n")
    f.write(f"  Math | Highest : {math_highest}) | Lowest : {math_lowest} \n")
    f.write(f"  Physics | Highest : {physics_highest}) | Lowest : {physics_lowest} \n")
    f.write(f"  Chemistry | Highest : {chemistry_highest}) | Lowest : {chemistry_lowest} \n")
    f.write(f"  Biology | Highest : {biology_highest}) | Lowest : {biology_lowest} \n")

