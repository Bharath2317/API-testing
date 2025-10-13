# def main():
#   student = get_student()
#   print(f"{student[0]} from {student[1]}")

# def get_student():
#   name = input("Enter your name: ")
#   house = input("Enter your house: ")

#   return (name,house)  

# def main():
#   student = get_student()
#   if student['name'] == 'padma':
#     student['house'] = 'RavenClaw'
#   print(f"{student['name']} from {student['house']}")



# def get_student():
#   student = {}
#   student['name'] = input("Name: ")
#   student['house'] = input("House: ")
#   return student  


class Student:
    def __init__(self,name,house):
       if not name:
          raise ValueError("You did not entered a name")
       if house not in ["Gryffindor","Hufflepuff","Slytherin","Ravenclaw"]:
          raise ValueError('Select a proper house')

       self.name = name
       self.house = house
    def __str__(self):
      return f"{self.name} from {self.house}"
        
  

def main():
  student = get_student()
  print(student)

def get_student():
  # student = Student()
  name = input("Name: ")
  house = input("House: ")
  return Student(name,house)











if __name__ == "__main__":
  main()