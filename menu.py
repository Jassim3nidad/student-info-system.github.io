import os


class MainMenu:
    def __init__(self, add_student, search_student, print_all_student):
        self.addstud = add_student
        self.search = search_student
        self.printAll = print_all_student

    def add_student_option(self):
        while True:
            os.system('cls')
            self.addstud.input_add_student()
            rep = input('Do you want o add another student? (y/n): ')
            if rep.lower() != 'y':
                break

    def search_student_option(self):
        while True:
            os.system('cls')
            print('=' * 10, 'Search Student Information', '=' * 10)
            keyword = input('\n\nEnter ID Number: ')
            print(self.search.search_student(keyword))
            rep = input('Do you want to search again? (y/n): ')
            if rep.lower() != 'y':
                break

    def main_menu(self, student):
        while True:
            os.system('cls')
            print(f'Welcome, {student[0]}!\n', '=' * 15,'Main Menu', '=' * 15)
            print("1. View your information\n2. View other student's information\n3. Register a new student\n4. Print all student\n5. Exit")
            choice = int(input('Your choice: '))
            if choice == 1:
                os.system('cls')
                print(self.search.search_student(student[1]))
                choice = input('Go back (Press Enter).')
            elif choice == 2:
                self.search_student_option()
            elif choice == 3:
                self.add_student_option()
            elif choice == 4:
                self.printAll.print_all_students()
            elif choice == 5:
                os.system('cls')
                print('=' * 10, 'Logging off', '=' * 10, '\nLogging out. Goodbye.')
                break
            else:
                print("Invalid Input")