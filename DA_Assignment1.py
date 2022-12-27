'''import csv
students = []
with open('MOOC.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)
filtered_students = [row for row in students if (int(row["age"]) < 30 and float(row["weight"]) < 190)]
for student in filtered_students:
    print(student["name"], student["age"], student["weight"])

import csv


def calculate(str1, str2):
    calculated_number = 0.0
    num1 = float(str1)
    num2 = float(str2)
    try:
        calculated_number = num1 / num2
    except ValueError:
        print('Error!')
    return calculated_number


students = []
with open('MOOC.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)
filtered_students = [row for row in students if int(calculate(row["weight"], row["height"])) < 2]

print(calculate('one', 'zero'))


student_info = [{'first name':'Caroline', 'last name':'Harrison', 'birthdate':'1997-03-02'}, {'first name':'Rachel', 'last name':'Reynolds', 'birthdate':'1996-01-07'}, {'first name':'Olivia', 'last name':'James', 'birthdate':'1998-05-09'}]

student_info.sort(key=lambda x: x['last name'])

'''

student_info = [{'first name':'Caroline', 'last name':'Harrison', 'birthdate':'1997-03-02'}, {'first name':'Rachel', 'last name':'Reynolds', 'birthdate':'1996-01-07'}, {'first name':'Olivia', 'last name':'James', 'birthdate':'1998-05-09'}]

youngest_student_info = max(student_info, key=lambda x: x['birthdate'])