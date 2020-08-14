# -*- coding:utf-8 -*-
# Author: Nick
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        print(f"Prepare enrollment for {stu_obj.name}")
        self.students.append(stu_obj)

    def hire_teachers(self, staff_obj):
        print(f"{staff_obj.name} is hired by {self.name}")
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        pass


class Teachers(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teachers, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell_info(self):
        print(f"""
            --------------info of Teacher {self.name}------------
            Name: {self.name}
            Age: {self.age}
            Sex: {self.sex}
            Salary: {self.salary}
            Course: {self.course}
            """)

    def teach(self):
        print(f"{self.name} teaches {self.course}")


class Students(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Students, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell_info(self):
        print(f"""
        --------------info of Student {self.name}------------
        Name: {self.name}
        Age: {self.age}
        Sex: {self.sex}
        Id: {self.stu_id}
        Grade: {self.grade}
        """)

    def pay_tuition(self, amount):
        print(f"{self.name} paid {amount}")


school = School("OB IT", "USA")
t1 = Teachers("Nick", 23, "Male", 20000, "Math")
t2 = Teachers("Alex", 33, "Male", 220000, "Python")

s1 = Students("JiaJia", 12, "Female", 1001, 5)
s2 = Students("Qing", 13, "Female", 1002, 6)

t1.tell_info()
t2.tell_info()
s1.tell_info()
s2.tell_info()
school.hire_teachers(t1)
school.hire_teachers(t2)
school.enroll(s1)
school.enroll(s2)
print(school.staffs, school.students)
school.staffs[1].teach()

for s in school.students:
    s.pay_tuition(5000)
    s.tell_info()
