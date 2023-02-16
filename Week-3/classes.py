class Student:
    age = 24
    eye_color = 'brown'
    #functions - 
    def __init__(self,name,hobby,fav_food,age):
        self.name = name
        self.hobby = hobby
        self.fav_food = fav_food
        self.age = age 
    
    def say_hello(self,name):
        print("Hello from "+ self.name.title())

    def run(self):
        print("Student is running ") 



#object - an instance of the class (copy )
# Object oriented programming 

#       Class -Template 
#       Objects - features 
#       name,hobby,fav_food,age

first_student = Student("Mercy","Swimming","chapati",20)

second_student = Student("Bob","driving","Ugali",40)

print("The first student is "+first_student.name.title())
print("The first student's favourite food is "+first_student.fav_food.title())


print("The second student's age is " +str(second_student.age))

second_student.run() #void function
second_student.say_hello(second_student.name)