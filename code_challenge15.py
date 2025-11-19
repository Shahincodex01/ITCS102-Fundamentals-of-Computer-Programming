import os
import json

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
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
        continue

    elif choice == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("RECORD FOUND")
                print("-------------------")
                print(f"\nRecord Found For Id {search_id}")
                for i in student_record[search_id]:
                    print(f"- - {i}")
                print("-----------------")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')

        print("DELETE STUDENT RECORD")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("RECORD FOUND")
                print("-------------------")
                print(f"\nRecord Found For Id {search_id}")
                for i in student_record[search_id]:
                    print(f"- - {i}")
                print("-----------------")

                student_record.pop(search_id)
                print("\nRECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif choice == 'e':
        os.system('cls')

        print("EDIT/MODIFY STUDENT RECORD")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("RECORD FOUND")
                print("-------------------")
                print(f"\nRecord Found For Id {search_id}")
                for i in student_record[search_id]:
                    print(f"- - {i}")
                print("-----------------")

                first_name = input("Please input student first name ---> ").upper()
                second_name = input("Please input student second name ---> ").upper()
                age = eval(input("Input student age ---> "))
                course = input("Input student course ---> ").upper()
                section = input("Input student section ---> ").upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section

                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'f':
        os.system('cls')
        print("EXPORT DATA")

        with open('student_record.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4 )
        
        print("\n\nDATA EXPORTED TO JSON")
        continue
    elif choice == 'g':
        print('quited system')
        break
    else:
        print('error')
        pass


