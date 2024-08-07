#-----------Task 2----------------
#একটি Student ক্লাস বানাবেন , যেখানে একটি মেথড থাকবে `total_student()` ;
#  এখান থেকে মোট স্টুডেন্ট সংখ্যা দেখান।

class Student:
    total_students = 0
    def __init__ (self, name, roll):
        self.name = name
        self.roll = roll
        Student.total_students += 1

    @classmethod
#classmethod একটা স্পেশাল মেথড যা ক্লাস এর অবজেক্ট না ক্লাস
#  এর মেথড কে কল করতে পারে
#The first parameter of a class method is always the class 
# itself, which is conventionally named cls.

#A decorator in Python is a design pattern that allows
# you to modify the behavior of a function or method. 
# Decorators are typically used to extend the functionality
# of functions or methods without modifying their actual code.
#  They are often used for logging, access control, 
# instrumentation, caching, and more.

    def total_student(cls):
        return cls.total_students
    
student1 = Student("Rahim", 101)
student2 = Student("Karim", 102)
student3 = Student("Jodu", 103)
student4 = Student("Modu", 104)

print('Total Student:', Student.total_student())