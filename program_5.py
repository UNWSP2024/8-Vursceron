# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

class_subjects = {}

while True:
    class_id = input("Enter class id: ")
    class_name = input("Enter class name: ")
    class_subject = class_id.split()[0]
    answer = input("Do you want to add another class? y/n")
    cls = {
        "class_id": class_id,
        "class_name": class_name
    }
    if class_subject not in class_subjects:
        class_subjects[class_subject] = []

    class_subjects[class_subject].append(cls)

    if answer != "y":
        break

subject = input("What class subject do you want to see?")
try:
    for my_class in class_subjects[subject]:
        print(f"{my_class['class_id']} - {my_class['class_name']}")
except KeyError:
    print("Subject not found")
