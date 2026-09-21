
OFFERED_SUBJECTS = ("Math", "Science", "English", "History", "Art")

def main():
    print("Welcome to the Student Data Organizer!\n")
    
   
    students_list = [] 

    while True:
        print("Select an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        
       
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nEnter student details:")
            
        
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: ")) 
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            
           
            subjects_input = input("Subjects (comma-separated): ")
            subjects_list = [sub.strip() for sub in subjects_input.split(',')]

            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects_list
            }
            
            students_list.append(student)
            print("\nStudent added successfully!\n")

        elif choice == '2':
            print("\n--- Display All Students ---")
            if not students_list:
                print("No students found.\n")
            else:
                for stu in students_list:
                    
                    subjects_str = ", ".join(stu['subjects'])
                    
                   
                    print(f"Student ID: \033[33m{stu['id']}\033[0m | Name: {stu['name']} | Age: \033[33m{stu['age']}\033[0m | Grade: {stu['grade']} | Subjects: {subjects_str}")
                print("...\n")

        elif choice == '3':
            print("\n--- Update Student Information ---")
            update_id = int(input("Enter Student ID to update: "))
            found = False
            
            for stu in students_list:
                if stu['id'] == update_id:
                    print(f"Current Name: {stu['name']}, Current Age: {stu['age']}")
                    
                   
                    new_name = input("Enter new name (or press Enter to skip): ").strip()
                    if new_name:
                        stu['name'] = new_name 
                        
                    new_age = input("Enter new age (or press Enter to skip): ").strip()
                    if new_age:
                        stu['age'] = int(new_age) 
                        
                    print("Student information updated successfully!\n")
                    found = True
                    break
                    
            if not found:
                print("Student not found.\n")

        elif choice == '4':
            print("\n--- Delete Student ---")
            delete_id = int(input("Enter Student ID to delete: "))
            found = False
            
            for i, stu in enumerate(students_list):
                if stu['id'] == delete_id:
                    
                    del students_list[i] 
                    
                    print(f"Student with ID {delete_id} deleted successfully!\n")
                    found = True
                    break
                    
            if not found:
                print("Student not found.\n")

        elif choice == '5':
            print("\n--- Display Subjects Offered ---")
            for subject in OFFERED_SUBJECTS:
                print(f"- {subject}")
            print("...\n")

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
