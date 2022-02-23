"""
Basic of Class and Object
"""

# Student Data Type in Student Class
from Student import Student

# Student Object
student1 = Student("Stacy", "Nano", False)
student2 = Student("Adam", "Mech", True)
# The values are getting passed into the init function.
# Passed values are getting stored inside the respective name, major ....
# Actual Obj.name = name passed


# Access the information inside the object
print(student1.name)
# print(student1.gpa)

print(student2.name)
print(student2.is_on_probation)

print("Honors: ", student1.on_honor_roll(3.6))
print("Honors: ", student2.on_honor_roll(3.2))


"""
MCQ test question
"""

# from Mcq import Mcq
#
# question_prompt = [
#     "What color are oranges?\n(a) Red\n(b) Orange\n",
#     "What color are bananas?\n(a) Yellow\n(b) Red\n\n"
# ]
#
# # Creating the objects with prompt and answer
# questions = [
#     Mcq(question_prompt[0], "b"),
#     Mcq(question_prompt[1], "a")
#
# ]
#
# # Taking user input to the particular question prompt and check the answer
# def run_test(questions):
#     score = 0
#     for sub_question in questions:
#         answer = input(sub_question.prompt)
#         if answer == sub_question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")
#
# run_test(questions)