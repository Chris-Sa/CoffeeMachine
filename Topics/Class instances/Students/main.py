
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here

        self.student_id = self.name[0] + self.last_name + self.birth_year


s_name = input()
s_last_name = input()
s_year = input()

stud = Student(s_name, s_last_name, s_year)

print(stud.student_id)


