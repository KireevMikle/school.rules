import setup
from scedule.models import *

def menu():
    num = int(input("1. Додати придмет, 2. Додати вчителя, 3. Додати клас, 4. Додати учня, 5. Додати розклад, 6. Додати оцінку, 0. Вийти"))
    return num

def add_subject():
    name = input('Введіть назву предмету')
    description = input('Введіть опис предмету')
    Subject.objects.create(title=name, summary=description)

def add_teacher():
    first_name = input("Введіть ім'я вчителя:")
    last_name = input('Введіть прізвище')
    #Teacher.objects.create(first_name=first_name, last_name=last_name)
    id = int(input("Введіть id предмету"))
    subject = Subject.objects.get(id=id)
    if subject:
        Teacher.object.create(first_name=first_name, last_name=last_name, subject=subject)

while True:
    choise=menu()
    if choise == 1:
        add_subject()
    elif choise == 2:
        add_teacher()
    elif choise == 0:
        break          
