# Student Data Type, Overivew, or the Template of the user data type
class Student:

    # Here Self is the actual object
    def __init__(self, name, major, is_on_probation):
        self.name = name
        self.major = major

        self.is_on_probation = is_on_probation

    # Creating a fuction inside the class
    def on_honor_roll(self, gpa):
        if gpa >= 3.5:
            return True
        else:
            return False

