import csv
# name = input("What is your name?")
# # file = open("name.txt",'w')
# # file = open("name.txt",'a')
# # file.write(f"{name}\n")
# # file.close()
# with open("name.txt",'a') as file:
#   file.write(f"{name}\n")

# with open("name.txt",'r') as file:
#   lines = file.readlines()

# for line in lines:
#   print(f"Hello,{line}")  

# names =[]
# with open("name.txt",'r') as file:
#   for line in file:
#     names.append(line.rstrip())

# for name in sorted(names):
#   print("Hello",name) 

students = []

# with open("name.csv") as file:
#   for line in file:
#     # row = line.rstrip().rsplit(",")
#     # students.append(f"{row[0]} is in {row[1]} house")
#     stu,house = line.rstrip().rsplit(",")
#     students.append(f"{stu} is in {house} house")
# for stu in sorted(students):
#   print(stu)

# with open("name.csv") as file:
#   for line in file:
#     stu,color = line.rstrip().rsplit(",")
#     student = {"name":stu,"color":color}
#     students.append(student)
# for st in students:
#   print(f"{st['name']} is in {st['color']} house")    


# with open("name.csv") as file:
#   for line in file:
#     student,color = line.rstrip().rsplit(",")
#     students.append({"student":student,"color":color})

# def get_name(student):
#   return student['student']

# for student in sorted(students,key=get_name):
#   print(f"{student['student']} is in {student['color']} house")


with open("name.csv") as file:
  reader = csv.reader(file)
  for row in reader:
    students.append({"names":row[0],"color":row[1]})

for student in sorted(students,key = lambda s : s ['names']):
  print(f"{student['names']} is in {student['color']} house")  





