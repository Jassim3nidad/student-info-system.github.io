from tkinter import *
from functools import partial
from add_student import AddStudent
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from student import StudentInfo

# Initialize student management system
student_data = StudentInfo()
add_student = AddStudent(student_data)
search_student = SearchStudent(student_data)
print_all_students = PrintAllStudent(student_data)

# Main Window
win = Tk()
win.title("Student Management System")
win.geometry(f"1366x768+{(win.winfo_screenwidth()-1366)//2}+{(win.winfo_height()-1)//2}")
win.configure(bg="#f5f5f5")

# Login Variables
logged_in_user = None

# Frames
login_frame = Frame(win, bg="#f5f5f5")
main_menu_frame = Frame(win, bg="#ffffff")
menu_div = Frame(main_menu_frame, bg="#2c3e50")
con1_div = Frame(main_menu_frame, bg="#ecf0f1", relief=GROOVE, bd=2)
con2_div = Frame(main_menu_frame, bg="#ecf0f1", relief=GROOVE, bd=2)
con3_div = Frame(main_menu_frame, bg="#ecf0f1", relief=GROOVE, bd=2)
con4_div = Frame(main_menu_frame, bg="#ecf0f1", relief=GROOVE, bd=2)
con5_div = Frame(main_menu_frame, bg="#ecf0f1", relief=GROOVE, bd=2)

# Function to handle frame visibility
def show_frame(frame):
    """Shows the selected frame and hides the others."""
    for f in [con1_div, con2_div, con3_div, con4_div, con5_div]:
        f.pack_forget()
    frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Page Functions
def content1_btn():
    show_frame(con1_div)
    for widget in con1_div.winfo_children():
        widget.destroy()
    Label(con1_div, text="Add a New Student", font=('Arial', 18, 'bold'), bg="#ecf0f1", pady=10).pack()
    fields = ["Name", "Age", "ID Number", "Email", "Phone"]
    entries = {}
    for field in fields:
        Label(con1_div, text=field, font=('Arial', 14), bg="#ecf0f1").pack(pady=2)
        entry = Entry(con1_div, width=30, font=('Arial', 12))
        entry.pack(pady=5)
        entries[field] = entry

    def save_student():
        values = {field: entries[field].get() for field in fields}
        add_student.add_student(
            values["Name"], values["Age"], values["ID Number"], values["Email"], values["Phone"]
        )
        Label(con1_div, text="Student Added Successfully!", fg="green", font=('Arial', 12), bg="#ecf0f1").pack(pady=5)

    Button(con1_div, text="Save Student", command=save_student, font=('Arial', 14), bg="#2ecc71", fg="white", width=15).pack(pady=10)

def content2_btn():
    show_frame(con2_div)
    # Search Student Page
    for widget in con2_div.winfo_children():
        widget.destroy()
    Label(con2_div, text="Search for a Student", font=('Arial', 18, 'bold'), bg="#ecf0f1").pack(pady=10)
    Label(con2_div, text="Enter Student ID:", font=('Arial', 14), bg="#ecf0f1").pack(pady=5)
    id_entry = Entry(con2_div, width=30, font=('Arial', 12))
    id_entry.pack(pady=5)

    def search():
        student_info = search_student.search_student(id_entry.get())
        Label(con2_div, text=student_info, wraplength=600, justify="left", font=('Arial', 12), bg="#ecf0f1").pack(pady=10)

    Button(con2_div, text="Search", command=search, font=('Arial', 14), bg="#3498db", fg="white", width=15).pack(pady=10)

def content3_btn():
    show_frame(con3_div)
    # View Your Own Info Page
    for widget in con3_div.winfo_children():
        widget.destroy()
    Label(con3_div, text="View Your Information", font=('Arial', 18, 'bold'), bg="#ecf0f1").pack(pady=10)
    Label(con3_div, text="Enter Your ID:", font=('Arial', 14), bg="#ecf0f1").pack(pady=5)
    id_entry = Entry(con3_div, width=30, font=('Arial', 12))
    id_entry.pack(pady=5)

    def view_info():
        student_info = search_student.search_student(id_entry.get())
        Label(con3_div, text=student_info, wraplength=600, justify="left", font=('Arial', 12), bg="#ecf0f1").pack(pady=10)

    Button(con3_div, text="View", command=view_info, font=('Arial', 14), bg="#3498db", fg="white", width=15).pack(pady=10)

def content4_btn():
    show_frame(con4_div)
    # Print All Students Page
    for widget in con4_div.winfo_children():
        widget.destroy()
    Label(con4_div, text="All Students Information", font=('Arial', 18, 'bold'), bg="#ecf0f1").pack(pady=10)

    def print_all():
        student_data_str = student_data.__str__()
        Label(con4_div, text=student_data_str, wraplength=600, justify="left", font=('Arial', 12), bg="#ecf0f1").pack(pady=10)

    Button(con4_div, text="Print All", command=print_all, font=('Arial', 14), bg="#3498db", fg="white", width=15).pack(pady=10)


# Login Function
# Initialize login attempts
attempts = 0

def login():
    global logged_in_user, attempts
    # Increment attempts each time login is clicked
    if attempts < 4:
        student_id = login_id_entry.get()
        user = search_student.verify_login(student_id)
        if user:
            logged_in_user = user  # Store logged-in user
            login_frame.pack_forget()
            main_menu_frame.pack(side="left", fill="both", expand=True)
        else:
            attempts += 1
            remaining_attempts = 4 - attempts
            login_status_label.config(
                text=f"Invalid ID. Attempts left: {remaining_attempts}",
                fg="red"
            )
    if attempts >= 4:
        login_status_label.config(
            text="You have exceeded the number of attempts. Goodbye!",
            fg="red"
        )
        win.after(2000, win.destroy)  # Closes the program after 2 seconds

# Logout Function
def logout():
    global logged_in_user
    logged_in_user = None
    main_menu_frame.pack_forget()
    login_frame.pack(side="left", fill="both", expand=True)

# Login Screen
Label(login_frame, text="Student Info System - Login", font=("Arial", 24, "bold"), bg="#f5f5f5", pady=20).pack()
Label(login_frame, text="Enter Student ID:", font=("Arial", 14), bg="#f5f5f5").pack(pady=10)
login_id_entry = Entry(login_frame, width=30, font=("Arial", 14))
login_id_entry.pack(pady=10)
Button(login_frame, text="Login", command=login, font=("Arial", 14), bg="#3498db", fg="white", width=15).pack(pady=20)
login_status_label = Label(login_frame, text="", font=("Arial", 12), bg="#f5f5f5")
login_status_label.pack()
login_frame.pack(side="left", fill="both", expand=True)

# Menu Buttons
btn_txt = ["Add Student", "Search Student", "View Info", "Print All", "Logout"]
function = [content1_btn, content2_btn, content3_btn, content4_btn, logout]
for i, txt in enumerate(btn_txt):
    Button(menu_div, text=txt, command=function[i], font=("Arial", 14), bg="#34495e", fg="white", width=21, pady=10).grid(column=0, row=i+1, pady=5)
menu_div.pack(side="left", fill="y")

mainloop()
