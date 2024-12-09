class AddStudent:
    def __init__(self, student_info):
        self.student_data = student_info

    def input_add_student(self):
        print("="*10, "Add a New Student", "="*10)
        # Collect student info
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        idnum = input("Enter ID Number: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")

        self.add_student(name, age, idnum, email, phone)
        print("="*10, "Student added successfully", "="*10)

    def add_student(self, name, age, idnum, email, phone):
        print(f"\nAdded student {name} to the list.\n")

        # Write to file
        self.write_to_file(f"{name}, {age}, {idnum}, {email}, {phone}\n")

    def write_to_file(self, data_to_write):
        with open("student_data.txt", "a") as file:
            file.write(data_to_write)
        print("Data saved successfully.")
