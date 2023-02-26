LIGHT_RED = "\033[1;31m"
LIGHT_PURPLE = "\033[1;35m"
END = "\033[0m"

print("""Welcome to the   _   _
                | | | |
 _ __ ___   __ _| |_| |__
| '_ ` _ \ / _` | __| '_ `
| | | | | | (_| | |_| | | |
|_| |_| |_|\__,_|\__|_| |_| Calculator!""")

while True:
    menu = "______________________________________________"
    menu += "\n             MENU OPTIONS"
    menu += "\nA: Perform a calculation"
    menu += "\nB: Show calculation history"
    menu += "\nC: Exit"
    menu += "\n______________________________________________"
    print(menu)
    choice = input("Enter the menu option: ")

    # MENU OPTION A:
    # User chooses option 'A' for performing a calculation and is prompted to enter two numerical values.
    # If an integer or a float are not entered, the except block is executed and a message is printed to the terminal asking the user to try again.
    # The user is then prompted to pick an operation to perform. If-else statements are used to determine if the right option has been picked.
    if choice.lower() == "a":
        while True:
            try:
                first_num, second_num,  = [float(x) for x in input(
                    "\nEnter two numerical values separated by a comma. These will be the two values we will calculate with: ").split(",")]
            except ValueError:
                print(
                    f"{LIGHT_RED}Something went wrong with your number inputs, please try again!{END}")
                continue

            while True:
                operation = input(
                    '''\nWhat calculation would you like to do with the numbers {} and {}?
➕      add (+)
➖      subtract (-)
✖️       multiply (*)
➗      divide (/)
Enter +, -, * or /:  '''.format(first_num, second_num))

                if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                    print(
                        f"{LIGHT_RED}\nYou have not picked a permitted mathematical operation. Please pick again!{END}")
                else:
                    with open("equations.txt", "a",) as equation_file:

                        # ADDITION
                        if operation == "+":
                            answer = first_num + second_num

                        # SUBTRACTION
                        # If the first number entered by the user is smaller than the second value the user is prompted so they can choose to reorder their values.
                        elif operation == "-":
                            if first_num < second_num:
                                while True:
                                    verify = input(
                                        f"{LIGHT_RED}\nAre you sure you want to subtract the larger value from the smaller value? This will give a negative value: y/n: {END}")
                                    if verify.lower() == "y":
                                        answer = first_num-second_num
                                        break
                                    elif verify.lower() == "n":
                                        answer = second_num-first_num
                                        break
                                    elif verify.lower() != "y" and verify.lower() != "n":
                                        print(
                                            f"{LIGHT_RED}\nThis is not a valid option. Please choose y or n{END}")
                            else:
                                answer = first_num-second_num

                        # MULTIPLICATION
                        elif operation == "*":
                            answer = first_num*second_num

                        # DIVISION
                        # If the first number entered by the user is smaller than the second value the user is prompted so they can choose to reorder their values.
                        # If the user is trying to divide a number by zero, the except block is executed and a message is printed explaining that the number cannot be divided by zero.
                        elif operation == "/":
                            while True:
                                if first_num < second_num:
                                    verify = input(
                                        f"{LIGHT_RED}\nAre you sure you want to divide the smaller value by the larger value? y/n: {END}")
                                    if verify.lower() == "y":
                                        try:
                                            answer = first_num/second_num
                                            break
                                        except ZeroDivisionError:
                                            print(
                                                f"{LIGHT_RED}\nYou cannot divide a number by zero{END}")
                                            break
                                    elif verify.lower() == "n":
                                        try:
                                            answer = second_num/first_num
                                            break
                                        except ZeroDivisionError:
                                            print(
                                                f"{LIGHT_RED}\nYou cannot divide a number by zero{END}")
                                            break
                                    elif verify.lower() != "y" and verify.lower() != "n":
                                        print(
                                            f"{LIGHT_RED}\nThis is not a valid option. Please choose y or n{END}")
                                else:
                                    try:
                                        answer = first_num/second_num
                                        break
                                    except ZeroDivisionError:
                                        print(
                                            f"{LIGHT_RED}\nou cannot divide a number by zero{END}")

                        output = f"{first_num} {operation} {second_num} = {answer}\n"
                        print(f"\n{LIGHT_PURPLE}{output}{END}")
                        equation_file.write(f"{output}\n")
                        break
            break
    # MENU OPTION B
    # User chooses option 'B' to see calculation history and is prompted for the file name.
    # The user enters the file name of the txt file where the calculations have been stored.
    # If the file name does not match, they are prompted to try again.
    # If the file name matches, the file is opened, read and the equations are printed.
    elif choice.lower() == "b":
        while True:
            file_name = input("Please enter the file name: ")
            try:
                equation_file = open(f"{file_name}.txt", "r")
                equations = equation_file.readlines()
                print(
                    "Please see all equations entered so far together with results:")
                if equations == []:
                    print(f"{LIGHT_RED}There is no calculation history yet!{END}")
                else:
                    for line in equations:
                        each_equation = line.strip("\n")
                        print(f"{LIGHT_PURPLE}{each_equation}{END}")
                equation_file.close()
                break
            except FileNotFoundError as error:
                print(
                    f"{LIGHT_RED}The file that you are trying to open does not exist")
                print(error)
                print(f"Please try again below\n{END}")

    # MENU OPTION C
    elif choice.lower() == "c":
        print("\nGoodbye!")
        exit
        break
    else:
        print(f"{LIGHT_RED}Not a valid option. Please enter A, B or C. Try again!{END}")
