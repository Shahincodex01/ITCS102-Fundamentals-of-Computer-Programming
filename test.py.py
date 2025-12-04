import os
import time
#time.sleep()
#print("\033[4mUnderlined\33[0m]")

wel_come = input("HI, CAN YOU TELL ME YOUR \033[4mNAME\33[0m: ").upper()
gen_der = input("WHAT'S YOUR \033[4mGENDER\33[0m? 'M or F': ").upper()

os.system('cls')
if gen_der == 'M':
    title = ("MR.")
elif gen_der == 'F':
    title = ("MS.")
else:
    title = ("THEY/THEM")

while True:
    print("---------------------------------------------------------------------------------------------------")
    time.sleep(0.5)
    print(f"\t\t🌐 WELCOME \033[3m{title} {wel_come}\033[0m TO THE PYTHON PROGRAM 🌐")
    print("---------------------------------------------------------------------------------------------------")
    time.sleep(0.5)
    print("SELECT THE TOPIC THAT YOU WANT BELOW: ")
    print("0 - INTRODUCTION")
    print("1 - FUNCTIONS")
    print("2 - OPERATORS")
    print("A - PRINTING IN PYTHON")
    print("B - CONDITIONAL STATEMENT")
    print("C - LOOPING STATEMENTS")
    print("D - ARRAYS")
    print("E - DICTIONARY")
    print("F - RUN YOUR OWN CODE")
    print("G - EXIT THE PROGRAM")
  
    choice = input("SELECT FOR THE OPTIONS ABOVE ---> ").upper()

    if choice == '0':
        os.system('cls')
        while True:
            print("---------------------------------------------------------------------------------------------------")
            print("HELLO", title, wel_come,)
            what = input("Do you have a background knowledge about Python? 'Y' or 'N': ").upper()

            if what == 'Y':
                print("Good. let's move on.")
                break
            elif what == 'N':
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\t        \033[4mGUIDO VAN ROSSUM\033[0m\n")
                time.sleep(0.5)
                print("Python was created by Guido van Rossum in the late 1980s and was officially released in 1991.\n\n")
                time.sleep(0.5)
                print("He designed it because he wanted a programming language that was simple, clean, and enjoyable\n" \
                "to use—something easier than most languages at that time.\n\n")
                time.sleep(0.5)
                print("Python’s name was inspired by the comedy group “Monty Python,” showing that the language was\n"\
                "meant to be fun and friendly.\n\n")
                time.sleep(0.5)
                print("Over the years, Python grew into one of the most popular languages in the world because people\n"\
                "loved how readable and flexible it is.\n\n")
                time.sleep(0.5)
                print("Today, it is used in almost every field, from education and web development to artificial\n"\
                "intelligence and science.\n")
                time.sleep(0.5)
                print("More in 'https://en.wikipedia.org/wiki/Python_%28programming_language%29?h'\n")
                input("Type anything if you're finished: ")
                time.sleep(0.5)
                break
            else:
                print("INVALID")
                continue
        continue

    
    elif choice == 'A':
        while True:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO PRINT IN PYTHON")
            print("1 - Definition")
            print("2 - Data Types")
            print("3 - Example")
            print("4 - Variables")
            print("5 - Back")
            letter_A = input("SELECT OPTIONS ABOVE: ")
       

            if letter_A == '1':
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\t          DEFINITION OF PYTHON\n")
                print("Python is a high-level programming language that is easy to read, easy to write, and great for beginners.\n" \
                "It uses a clean and simple syntax, which means the code looks neat and almost like plain English.\n" \
                "Because of this, beginners can learn Python faster compared to many other programming languages.\n\n")
                print("Python can be used to:\n")
                print("* build website and web apps")
                print("* create games")
                print("* automate tasks on your computer")
                print("* analyze data")
                print("* develop AI and Machine Learning")
                print("* create desktop applications\n")
                print("In short:\nPython is a beginner friendly language that helps you create almost anything int the world of programming.")
                nako = input("Type anything if your done: ")
                print("Going back...")
                time.sleep(1.2)
                continue
            
            elif letter_A == '2':
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tDATA TYPES\n")
                print("Python has different types of data, which tell the program how to store and use information.\n")
                print("* Integer (int): A whole number, positive or negative, with no decimals.\nExample: 18, 2025. Used for counting, age, or score.\n")
                print("* Float (float): A number with a decimal point.\nExample: 99.99, 36.6. Used for prices, measurements, or calculations.\n")
                print("* String (str): Text or characters, always in quotes.\nExample: 'Shahin', 'Hello'. Used for names, messages, or any text.\n")
                print("* Boolean (bool): A value that can only be True or False.\nUsed for conditions, decisions, and logic.\n")
                anona = input("Do you want an example? 'Y' or 'N': ").upper()
                if anona == 'Y':
                    print("---------------------------------------------------------------------------------------------------\n")
                    print("\t\t\tQuestion Table\n")
                    print("I. Look for the underlined words to identify it. Identify if it's int, float, str, bool. Input your answers in the Answer Table\n")
                    print("1. A Bite of Python \033[4mExersice\033[0m.")
                    print("2. Layla has \033[4m1\033[0m extra notebook for keeping notes in the class of Sir Mesiera.")
                    print("3. Balmond got GPA of \033[4m4.0\033[0m overall.")
                    print("4. Miya thinks Python is fun and saber agrees: \033[4mTrue\033[0m or \033[4mfalse\033[0m?\n ")
                    print("\t\t\tAnswer Table\n")
                    input1 = input("1 = ").lower()
                    input2 = input("2 = ").lower()
                    input3 = input("3 = ").lower()
                    input4 = input("4 = ").lower()
                    print("-------------------------------")
                    if input1 == "str":
                        print("1.", input1, "=", "Correct")
                    else:
                        print("1. Wrong")
                    if input2 == "int":
                        print("2.", input2, "=", "Correct")
                    else:
                        print("2. Wrong")
                    if input3 == "float":
                        print("3.", input3, "=", "Correct")
                    else:
                        print("3. Wrong")
                    if input4 == 'bool':
                        print("4.", input4, "=", "Correct")
                    else:
                        print("4. Wrong\n")
                    
                    input("Type anything to go back to Submenu: ")
                    time.sleep(1.5)
                    continue
                elif anona == 'N':
                    print("Going back to Submenu...")
                    time.sleep(1)
                    continue
                else:
                    print("Invalid")
                    print("Going back to Submenu...")
                    time.sleep(1)
                    continue

            elif letter_A == '3':
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\t\033[1;92mEXAMPLES IN PYTHON\033[0m\n")
                print("- print() in Python is used to show text or values on the screen. -\n")
                print("Example Input:")
                print("\tprint(\"Hello World!\")")
                print("\nExpected Output:")
                print("\tHello World!\n")

                print("Now it's your turn!\n")
                user_code = input("Type something to print (example: 'Hello Python'): ")

                print("\nYour Output:")
                print(user_code)

                input("\nType anything if you're finished: ")
                continue

            elif letter_A == '4':
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------")
                print("Now that you know printing, we can now add Variables.\n")
                print("*WHAT'S A VARIABLE?*")
                print("- A variable in Python is a name that stores a value, which you can use and print anytime\n")
                print("For Example:\n\nInput:")
                print("\tage = 18\n\tprint(age)")
                print("or\n\tprint(\"I'm {age} years old\")")
                print("Output:\n\t18\nor\n\tI'm 18 years old")
                print("---------------------------------------------------------------------------------------------------")
                huy = input("Now you're ready to go, want to try on your very own? 'Y' or 'N': ").upper()
                if huy == 'Y':
                    print("Type anything to execute the code you put:  ")
                    varia = input("Input a variable: ")
                    outpuT = input("Input a output: ")
                    print("\nIn python:\n ")
                    print(varia, "=", outpuT,"\n")
                    print(f'print({varia})\n')
                    print("Output:\n")
                    print(outpuT,"\n")
                    pause = input("Type anything to go back: ")
                    continue
                elif huy == 'N':
                    print("Going back..")
                    time.sleep(1)
                    print("Done.")
                    continue
                else:
                    print("Invalid")
                    continue
            elif letter_A == '5':
                print("You have selected 5 - back")
                time.sleep(1)
                print("Processing...")
                break
            else:
                print("INVALID")
                time.sleep(1)
                continue

    elif choice == '1':
        while True:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO FUNCTIONS")
            print("1 - Functions")
            print("0 - Back")
            bai = input("Select options above: ")
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            if bai == '1':
                print("A function in Python is a reusable block of code that performs a specific task.\n")
                print("Instead of writing the same code many times, you can put it inside a function and reuse it whenever you need.\n")
                print("Here are some of the functions: ")
                print("print() → displays text")
                print("input() → lets the user type something")
                print("len() → counts characters")
                print("type() → shows the data type\n")
                haynako = input("Do you want an example?: 'Y' or 'N': ").upper()
                print("---------------------------------------------------------------------------------------------------")
                if haynako == 'Y':
                    name = input("Enter your name: ")

                    print("\nprint('Hello', name)")
                    print("Hello,", name)

                    print("\ninput('Enter your name: ')")
                    print("You typed:", name)


                    print("\nlen(name)")
                    print("Length of your name:", len(name))

                    print("\ntype(name)")
                    print("Type of your input:", type(name))
                    input("\nType anything to go back: ")
                    continue
                elif haynako == 'N':
                    print("Going back..")
                    time.sleep(1)
                    print("DONE.")
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID")
                    input("TYPE ANYTHING TO GO BACK: ")
                    continue

            elif bai == '0':
                print("Going back..")
                time.sleep(1)
                print("DONE.")
                time.sleep(0.5)
                break
            else:
                print("INVALID")
                continue

    elif choice == '2':
        while True:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO OPERTORS\n")
            print("1 - Types of Operators")
            print("2 - Assignment Operators")
            print("3 - Relational Operators")
            print("4 - Logical Operators")
            print("5 - Back\n")
            anlala = input("Select options above: ")

            if anlala == '1':
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tTYPES OF OPERATORS\n")
                print("Arithmetic operators are used to do basic math operations like addition, \nsubtraction, multiplication, division, modulus, and exponent.")
                print("The following are the arithmetic operators in python:\n")
                print("+ addition                            |  5 + 3   = 8   ")
                print("- subtractions                        |  10 - 4  = 6   ")
                print("* multiplications                     |  6 * 2   = 12  ")
                print("/ division                            |  15 / 3  = 5.0 ")
                print("% Modus Division (remainder)          |  17 % 5  = 2   ")
                print("** exponentation                      |  2 ** 4  = 16  ")
                print("// floor division (integer division)  |  20 // 3 = 6   ")
                hayst = input("\nDo you want to try an example: 'Y' or 'N': ").upper()

                if hayst == 'Y':
                    n1 = eval(input("Input 1st number: "))
                    n2 = eval(input("Input 2nd number: "))

                    a = n1 + n2
                    b = n1 - n2
                    c = n1 * n2
                    d = n1 / n2
                    e = n1 % n2
                    f = n1 ** n2
                    g = n1 // n2
                    
                    print("\nResults:")
                    print(f"{n1} + {n2} = {a}")
                    print(f"{n1} - {n2} = {b}")
                    print(f"{n1} * {n2} = {c}")
                    print(f"{n1} / {n2} = {d}")
                    print(f"{n1} % {n2} = {e}")
                    print(f"{n1} ** {n2} = {f}")
                    print(f"{n1} // {n2} = {g}")

                    input("\nType anything to go back: ")
                elif hayst == 'N':
                    print("Going back..")
                    time.sleep(1)
                    print("DONE.")
                    time.sleep(0.5)
                else:
                    print("INVALID")
                    time.sleep(1)
                continue

            elif anlala == '2':
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tASSIGNMENT OPERATORS\n")
                print("Assignment operators are used to store values in variables or update existing values.\n")
                print("Here are the assignment operators in Python:\n")
                print("OPERATORS\tEXAMPLE\t\tSAME AS\n")
                print("=\t\tx = 10\t\tx = 10")
                print("+=\t\tx += 10\t\tx = x + 10")
                print("-=\t\tx -= 10\t\tx = x - 10")
                print("*=\t\tx *= 10\t\tx = x * 10")
                print("/=\t\tx /= 10\t\tx = x / 10\n")
                ayokona = input("Do you want a quiz? 'Y' or 'N': ").upper()

                if ayokona == 'Y':
                    print("\nLet's have a quiz!\n")

                    print("If x = 10, what is the result of the following?\n")

                    a1 = input("1. x += 5 = ")
                    a2 = input("2. x -= 3 = ")
                    a3 = input("3. x *= 2 = ")

                    print("\n-------------------------------")
                    print("Checking your answers...\n")
                    time.sleep(1)

                    if a1 == "15":
                        print("1. Correct!")
                    else:
                        print("1. Wrong")

                    if a2 == "7":
                        print("2. Correct!")
                    else:
                        print("2. Wrong")

                    if a3 == "20":
                        print("3. Correct!")
                    else:
                        print("3. Wrong")
                    
                    input("\nType anything to go back: ")
                    continue
                
                elif ayokona == 'N':
                    print("Going back to Submenu...")
                    time.sleep(1)
                    continue

                else:
                    print("Invalid")
                    print("Going back to Submenu...")
                    time.sleep(1)
                    continue


            elif anlala == '3':
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------\n")
                print("\t\t\tRELATIONAL OPERATORS\n")
                print("Relational operators are used to compare two values.")
                print("They return True or False depending on the comparison.\n")
                print("The following are the relational operators in Python:\n")
                print("==  Equal to              |  5 == 5   -> True")
                print("!=  Not equal to          |  5 != 3   -> True")
                print(">   Greater than          |  7 > 2    -> True")
                print("<   Less than             |  3 < 1    -> False")
                print(">=  Greater or equal      |  5 >= 5   -> True")
                print("<=  Less or equal         |  4 <= 6   -> True\n")
                print("---------------------------------------------------------------------------------------------------\n")
                grabe = input("Do you want to try an example: 'Y' or 'N': ").upper()

                if  grabe == 'Y':
                    lala1 = int(input("Enter first number: "))
                    lala2 = int(input("Enter second number: "))

                    print("\nResults:")
                    print(f"{lala1} == {lala2}  ->  {lala1 == lala2}")
                    print(f"{lala1} != {lala2}  ->  {lala1 != lala2}")
                    print(f"{lala1} > {lala2}   ->  {lala1 > lala2}")
                    print(f"{lala1} < {lala2}   ->  {lala1 < lala2}")
                    print(f"{lala1} >= {lala2}  ->  {lala1 >= lala2}")
                    print(f"{lala1} <= {lala2}  ->  {lala1 <= lala2}\n")
                    input("Type anything if you're done: ")
                else:
                    print("INVALID")
                    print("Going back..")
                    time.sleep(1)
                    print("DONE.")
                    time.sleep(0.5)
                continue

            elif anlala == '4':
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tWELCOME TO LOGICAL OPERATORS\n")
                print("Logical operators check two or more conditions at the same time.")
                print("They return True or False.")
                print("\nOperators:")
                print("and  = True only if BOTH conditions are true")
                print("or   = True if AT LEAST one condition is true")
                print("not  = Reverses True to Fals")
                print("------------------------------------------------------------")

                choose = input("Do you want to try a demo? 'Y' or 'N': ").upper()

                if choose == "Y":
                    gag = input("\nDid you eat today? (Y/N): ").upper()
                    gog = input("Did you sleep well? (Y/N): ").upper()

                    ate = gag == "Y"
                    slept = gog == "Y"
                    print("\nResults:")
                    print("ate and slept  ->", ate and slept)
                    print("ate or slept   ->", ate or slept)
                    print("not ate        ->", not ate)

                    input("\nType anything to go back: ")
                    continue
                elif choose == 'N':
                    input("Ok, type anything to go back: ")
                    continue
                else:
                    print("INVALID")
                    time.sleep(0.7)
                    print("Going back..")
                    time.sleep(0.7)
                    print("DONE")
                    time.sleep(0.5)
                    continue

            elif anlala == '5':
                print("Going back...")
                time.sleep(1)
                print("DONE")
                time.sleep(0.5)
                break
            else:
                print("INVALID")
                continue
            break

    elif choice == 'B':
        while True:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO THE WORLD OF DECISIONS\n")
            print("Before we begin, i like to test you first 👾\n")
            do0r = input("Choose a door: '1' '2': ")

            print("\nProcessing....")
            time.sleep(1.5)
            print("PROCESSING DONE")
            time.sleep(1)
        
            if do0r == '1':
                print("\nThe left door opens quietly as brining light shine through...\n")
                time.sleep(0.5)
                print("\33[32mYOU CHOOSE THE RIGHT DOOR, YOU LIVED\33[0m")
                time.sleep(0.5)
            elif do0r == '2':
                print("\nThe right door opens DRAMATICALY as fire burst through.... ")
                time.sleep(1)
                print("\n\33[91mYOU CHOOSE THE WRONG DOOR, YOU DIED\33[0m")
                time.sleep(1)
            else:
                print("\nNOTHING HAPPENS. AS YOU WAIT, HUNGER AWAITS. UNFORTUNATELY YOU DIE ☠️")
                time.sleep(0.5)

            print("\nWhat you just witnessed is an example of a Conditional Statement")
            time.sleep(0.5)
            print("It lets Python choose an action depending on your input.\n")
            time.sleep(0.5)
            print("---------------------------------------------------------------------------------------------------")
            print("1 - Definition")
            print("2 - Example")
            print("3 - Back")
            coke = input("Select options above: ")
            if coke == '1':
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tCONDITIONAL STATEMENTS\n")
                print("Conditional Statements in Python are instructions that let the " \
                "program make decisions based on certain conditions.")
                print("They check whether a condition is True or False and then execute" \
                " specific code depending on the result.\n")
                print("Main Types are:\n")
                print("* \033[1mif\033[0m -> Runs code only if the condition is true.\n* \033[1melif\033[0m -> (short for “else if”)" \
                " Runs code if the previous if or elif conditions were false, but this one is true\n* \033[1melse\033[0m -> Runs code if all previous conditions are false.\n")
                input("Type anything if you're done: ")
                continue
            elif coke == "2":
                print("---------------------------------------------------------------------------------------------------")
                print("\t\t\tEXAMPLES\n")
                print("if weather == 'raining':")
                print("    print('Take an umbrella.')") 
                print("elif weather == 'cloudy':")
                print("    print('Wear a jacket.')")
                print("elif weather == 'sunny'")
                print("    print('Wear sunglasses.')")
                print("else:")
                print("    print('Invalid.')\n")
                weather = input("Whats the weather today? 'Raining', 'Cloudy', 'Sunny': ").upper()
                if weather == 'RAINING':
                    print("\nTake an umbrella.\n")
                    time.sleep(1)
                elif weather == 'CLOUDY':
                    print("\nWear a jacket.\n")
                    time.sleep(1)
                elif weather =='SUNNY':
                    print("\nWear sunglasses.\n")
                    time.sleep(1)
                else:
                    print("\nInvalid.\n")
                    time.sleep(1)
                print("---------------------------------------------------------------------------------------------------")
                print("2nd Example: \n")
                print("if age < 13:")
                print("    print('You are a child.')")
                print("elif age >= 13 and age < 20:")
                print("    print('You are a teenager.')")
                print("else:")
                print("    print('You are an adult.')\n")
                age = int(input("Input your age: "))
                if age < 13:
                    print("You are a child.\n")
                elif age >= 13 and age < 20:
                    print("You are a teenager.\n")
                else:
                    print("You are an adult.\n")
                    input("Type anything to go back: ")
                    time.sleep(0.5)
                break
            elif coke == '3':
                print("You've choosed 3 - Back")
                print("Going back...")
                time.sleep(1)
                print("Done")
                break
            else:
                print("INVALID")
                continue
        continue                
    
    elif choice == 'C':
        while True:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO THE WORLD OF REPEATING MAGIC!\n")
            time.sleep(1)
            print("1 - Definitions")
            print("2 - Examples")
            print("3 - Back")
            floryn = input("Select options above: ")

            if floryn == '1':
                print("\nDEFINITIONS\n")
                time.sleep(1)
                print("-> Loop: A way to repeat a block of code multiple times automatically.")
                time.sleep(1)
                print("\n-> For Loop: Used when you know exactly how many times you want to repeat something.")
                print("   Example: repeat something 5 times.")
                time.sleep(1)
                print("\n-> While Loop: Used when you want something to repeat as long as a condition remains TRUE.")
                print("   Example: keep looping while a number is less than 10.")
                time.sleep(1)
                print("\n-> range(): Generates a sequence of numbers, commonly used in for loops.")
                print("   Example: range(5) -> 0 1 2 3 4")
                time.sleep(1)
                input("\nType anything to go back: ")

            elif floryn == '2':
                print("\nEXAMPLES\n")
                print("Example 1: For loop printing 5 times")
                print("for i in range(5):")
                print("    print('Hello')")
                print("\nOutput:")
                for i in range(5):
                    print("Hello")
                print("\nExample 2: Printing numbers 1 to 5")
                print("for i in range(1, 6):")
                print("    print(i)")
                print("\nOutput:")
                for i in range(1, 6):
                    print(i)
                print("\nExample 3: While loop counting up")
                print("count = 1")
                print("while count <= 5:")
                print("    print(count)")
                print("    count += 1")
                print("\nOutput:")
                count = 1
                while count <= 5:
                    print(count)
                    count += 1

                input("\nType anything if you want to go back to the menu ")
                break

    elif choice == 'D':
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------")


    elif choice == 'E':
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------")

    elif choice == 'F':
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------")


    elif choice == 'G':
        print("YOU HAVE EXITED THE PROGRAM THANK YOU")
        break
