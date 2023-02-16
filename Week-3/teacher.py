class Teacher:
    def __init__(self,name,tsc_no,subject,salary):
        self.name = name
        self.tsc_no = tsc_no
        self.subject = subject
        self.salary = salary 

    def print_teacher_name(self,name):  #methords related to class
        print(self.name.title())

    def increment_salary(self,salary):
        self.salary += 10000
        return self.salary
    
    def get_subject(self,subject):
        return self.subject

# name,tsc_no,subject,salary
teacher_one = Teacher("Mary",128345,"Chemistry",200000)

teacher_one.print_teacher_name(teacher_one.name)

teacher_one.increment_salary(teacher_one.salary)

print("Teacher ones new salary is : "+str(teacher_one.salary))
