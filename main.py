import setup
from scedule.models import *

def menu():
    num = int(input("1. Додати придмет, 2. Додати вчителя, 3. Додати учня, 4. Додати клас, 5. Додати розклад, 6. Додати оцінку, 0. Вийти : "))
    return num

def add_subject():
    name = input('Введіть назву предмету: ')
    description = input('Введіть опис предмету: ')
    Subject.objects.create(title=name, summary=description)

def add_teacher():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input('Введіть прізвище вчителя: ')
    id = int(input("Введіть id предмету: "))
    subject = Subject.objects.get(id=id)
    if subject:
        Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)

def add_student():
    first_name = input("Введіть ім'я студента: ")
    last_name = input('Введіть прізвище студента: ')
    Student.objects.create(first_name=first_name, last_name=last_name)

def add_class():
    name = input('Введіть назву класу: ')
    description = input('Введіть зміст уроку в класі: ')
    id = int(input("Введіть id студента: "))
    student = Student.objects.get(id=id)
    if student:
        Class.objects.create(title=name, summary=description, student=student)

#def add_schedule():
#    id = int(input("Введіть id предмету: "))
#    subject = Subject.objects.get(id=id)
#    if subject:
#        Schedule.objects.create(subject=subject)
#    id = int(input("Введіть id класу: "))
#    class_room = Class.objects.get(id=id)
#    if class_room:
#        Schedule.objects.create(class_room=class_room)
#    id = int(input("Введіть id вчителя: "))
#    teacher = Teacher.objects.get(id=id)
#    if teacher:
#        Schedule.objects.create(teacher=teacher)
#    date = 
#    time = 
#    Schedule.objects.create(date=date, time=time)
    
#def add_grade():
#    id = int(input("Введіть id предмету: "))
#    subject = Subject.objects.get(id=id)
#    if subject:
#        Grade.objects.create(subject=subject)
#    id = int(input("Введіть id студента: "))
#    student = Student.objects.get(id=id)
#    if student:
#        Grade.objects.create(student=student)
#    date = 
#    grade = int(input("введіть оцінку"))
#    Grade.objects.create(date=date, grade=grade)

while True:
    choise=menu()
    if choise == 1:
        add_subject()
    elif choise == 2:
        add_teacher()
    elif choise == 3:
        add_student()
    elif choise == 4:
        add_class()
    #elif choise == 5:
    #    add_schedule()
    #elif choise == 6:
    #    add_grade()
    elif choise == 0:
        break
    else:
        print("невідома команда")           
