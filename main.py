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

def add_schedule():
    sub_id = int(input("Введіть id предмету: "))
    subject = Subject.objects.get(id=sub_id)
    cls_id = int(input("Введіть id класу: "))
    class_room = Class.objects.get(id=cls_id)
    id = int(input("Введіть id вчителя: "))
    teacher = Teacher.objects.get(id=id)
    date = input("Введіть дату: ")
    time = input("Введіть час: ")
    if subject and class_room and teacher:
        Schedule.objects.create(subject=subject, class_room=class_room, teacher=teacher, date=date, time=time)
    
def add_grade():
    id = int(input("Введіть id предмету: "))
    subject = Subject.objects.get(id=id)
    id = int(input("Введіть id студента: "))
    student = Student.objects.get(id=id)
    date = input("Введіть дату: ")
    grade = int(input("введіть оцінку: "))
    if subject and student:
        Grade.objects.create(subject=subject, student=student, date=date, grade=grade)

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
    elif choise == 5:
        add_schedule()
    elif choise == 6:
        add_grade()
    elif choise == 0:
        break
    else:
        print("невідома команда")           
