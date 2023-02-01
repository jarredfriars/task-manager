# I.D 1
# This program helps users to manage and create tasks assigned to users
# users are stored in the file 'user.txt'
# tasks are stored in the file 'tasks.txt'
# You can perform the following functions:
# r - Registering a user - ONLY ADMINS can register new users
# a - Adding a task
# va - View all tasks
# vm - view my task
# s - statistic (admin only)
# e - Exit

# opens the user file and creates a list for the user and a list for the passwords

user_file = open("user.txt", "r+", encoding="utf-8")

admins = user_file.readlines()

username = []
password = []

for admin in admins:
    admin = admin.replace(" ", "").strip("\n").split(",")
    username.append(admin[0])
    password.append(admin[1])

# opens the task file and creates a list for the tasks

task_file = open("tasks.txt", "a+", encoding="utf-8")

tasks = []

for task in task_file: 
    tasks.append(task)
    tasks = task.strip().split(",")

print("This program adds user logins to the database and assigns them tasks""\n")

# while loop below checks if the user exists in the user txt file, only registered users can login

while True:
    logged_in = input(str("please enter your username: "))
    logged_in_pass = input(str("Please enter your password: "))
    if logged_in in username and logged_in_pass in password:
        print("Success! You have been logged in!")
        break
    else:
        print("Please try again")

# while loop below helps the user navigate the menu, admins have extra privileges

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - statistics (admin only)
e - Exit
: ''').lower()

# this menu only lets admins add new users, checks the user and password logged in matches admin credentials
# users are added to the user txt file with the "write" function and added to the local list with "append"

    if menu == 'r':
        while True:
            if logged_in == username[0] and logged_in_pass == password[0]:
                user = input("\n""please enter the username you are registering: ""\n")
                user_pass = input("please enter the password for the user you are registering: ""\n")
                pass_confirm = input("please confirm the password for the user you are registering: ""\n")
                if user_pass == pass_confirm:
                    print("\n""Success! New user has been registered""\n")
                    user_file.write("\n"f"{user}, {pass_confirm}")
                    username.append(user)
                    password.append(pass_confirm)
                    break
            else:
                print("Only admins can add new users")
                break

# this menu lets users add new tasks to the task txt file
# tasks are added to the txt file with the "write" function and the file is then closed

    elif menu == 'a':
        username = input("\n""please enter the username you want to add a task to: ").lower()
        user_task = input("\n"f"please enter the title of the task you want to add for {username}: ")
        task_desc = input("\n"f"please enter the description of the task you are adding for {username} : ")
        date = input("\n""Please enter today's date in the format " "day mon year:" " e.g 01 Jan 2022: ")
        due_date = input("\n""Please enter the due date in the format " "day mon year:" " e.g 01 Jan 2022: ")
        complete = "No"
        task_file.write("\n"f"{username}, {user_task}, {task_desc}, {due_date}, {date}, {complete}") 
        task_file.close()

# this menu lets users check all tasks from the task txt file

    elif menu == 'va': 
        va_tasks = open("tasks.txt", "r")
        for line in va_tasks:
            tasks = line.strip().split(", ")
            name = tasks[0]
            task = tasks[1]
            desc = tasks[2]
            assign_date = tasks[3]
            due = tasks[4]
            complete = tasks[5]
            header = "_"*100
            print(header, "\n"
                f"Task:                {task}\n"
                f"Assigned to:         {name}\n"
                f"Date assigned:       {assign_date}\n"
                f"Due date:            {due}\n"
                f"Task complete?       {complete}\n"
                f"Task description: \n {desc} \n"
                f"{header}\n")

# this menu lets the user check the task assigned to themselves, if they do not have a task
# they will be told 'no tasks assigned'

    elif menu == 'vm':
        vm_tasks = open("tasks.txt", "r")
        for line in vm_tasks:
            tasks = line.strip().split(", ")
            if logged_in in tasks:
                name = tasks[0]
                task = tasks[1]
                desc = tasks[2]
                assign_date = tasks[3]
                due = tasks[4]
                complete = tasks[5]
                header = "_"*100
                print(header, "\n"
                f"Task:                {task}\n"
                f"Assigned to:         {name}\n"
                f"Date assigned:       {assign_date}\n"
                f"Due date:            {due}\n"
                f"Task complete?       {complete}\n"
                f"Task description: \n {desc} \n"
                f"{header}\n")
            else:
                print("no tasks assigned")

# this menu allows admins to check the statistics for all users and tasks
# it will show the number of users in the user txt file and
# the number of tasks in the task txt file
# if a user is not an admin they will receive the error message:
# "You do not have admin privileges to access this menu"

    elif menu == 's':
        while True:
            if logged_in == "admin" and logged_in_pass == "adm1n":
                with open("user.txt", "r") as user_stats:
                    user_stats = len(user_stats.readlines())
                    print("\nThe number of users registered is: ", user_stats)
                with open("tasks.txt", "r") as task_stats:
                    user_stats = len(task_stats.readlines())
                    print("\nThe number of tasks registered is: ", user_stats)
                    break
            else:
                print("You do not have admin privileges to access this menu")
                break

# allows the user to exit the program by typing 'e'

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# if the wrong selection is made then the error message below is show

    else:
        print("You have made a wrong choice, Please Try again")
