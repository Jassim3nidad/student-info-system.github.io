class PrintAllStudent:
    def __init__(self, student):
        self.student_data = student

    def print_all_students(self):
        print('=' * 15, "All Students' Information", '=' * 15)
        for i in self.student_data.allstudents:
            name, age, idnum, email, phone = i
            print(f'\nName: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}\n')
        print('=' * 20, "Nothing Follows",'=' * 20)
        input('\nGo back (press Enter).')