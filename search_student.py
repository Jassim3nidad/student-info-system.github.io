class SearchStudent:
    def __init__(self, student):
        self.student_data = student
    
    def search_student(self, keyword):
        for student in self.student_data.allstudents:
            if student[2] == keyword:
                name, age, idnum, email, phone = student
                filler = '=' * 23
                print('\nStudent Found:\n', '=' * 20, "Student's Information", '=' * 20)
                return f'\nName: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}\n'
        return f'\nThe student with the ID number {keyword} does not exist.\n'
    
    def verify_login(self, idnum):
        for student in self.student_data.allstudents:
            if student[2] == idnum:
                return [student[0], student[2]]
        return False