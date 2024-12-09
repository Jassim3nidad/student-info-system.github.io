from student import *
from search_student import *
from print_all_student import *
from menu import *
from add_student import *
import os

stu = StudentInfo()
addstud, search, printAll = AddStudent(stu), SearchStudent(stu), PrintAllStudent(stu)
menu = MainMenu(addstud, search, printAll)

attempts = 0
while attempts < 4:
    print('=' * 10, "Login - Student Info. System", '=' * 10)
    login_check = input('Student ID: ')
    user = search.verify_login(login_check)
    if user != False:
        menu.main_menu(user)
        break
    else:
        os.system('cls')
        attempts += 1
        print(f'\nThe student with the ID nuimber {login_check} does not exist.\nAttemps left: {4 - attempts}')
    if attempts > 4:
        os.system('cls')
        print('You have exceeded the number of attempts.Goodbye!')
        break 
