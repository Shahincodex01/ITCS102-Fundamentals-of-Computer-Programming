import os

#os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("---------------------------------")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTION")
    print("A - ADD STUDENT RECORD")
    print("B- PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - EXIT SYSTEM")

    choice = input("SELECT FOR THE OPTIONS ABOVE ---> ").lower()

    if choice == 'a':
        print("\nADDING STUDENT RECORD")

        id_no = input("Please input student id number ---> ")

        first_name = input("Please input student first name ---> ").upper()
        second_name = input("Please input student second name ---> ").upper()
        age = eval(input("Input student age ---> "))
        course = input("Input student course ---> ").upper()
        section = input("Input student section ---> ").upper()

        student_record[id_no]=[first_name, second_name, age, course, section]
        print("DATA SAVED SUCCESFULLY")


        continue
    elif choice == 'b':
      #os.system('cls')
        print("PRINTING STUDENT RECORD")
    
        for i, j in student_record.items():
            print(f"CODE - {i}, INFORMATINO - {j}")
        continue
    elif choice == 'c':
        pass 
        continue
    elif choice == 'd':
        pass 
        continue
    elif choice == 'e':
        pass 
        continue
    elif choice == 'g':
        print('quited system')
        break
    else:
        print('error')
        pass


