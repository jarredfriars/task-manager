#=====importing libraries===========


#====Login Section====

user_file = open("user.txt", "r+", encoding="utf-8")

admins = user_file.readlines()

users = []

for admin in admins:
    admin = admin.strip("\n").split(", ")
    users = admins

print(users)

task_file = open("tasks.txt", "a+", encoding="utf-8")

tasks = task_file.readlines()

tasks = []

for task in task_file: 
    tasks.append(task)
    tasks = task.strip().split(",")

print("This program adds user logins to the database and assigns them tasks""\n")

logged_in = input("please enter your username: ")

logged_in_pass = input("Please enter your password: ")

while True: 
    logged_in = input("please enter your username: ")
    if logged_in in users[0]:
        logged_in_pass = input("Please enter your password: ")
        if logged_in_pass in users[1]:
            print("\n""Success! You have been logged in""\n")
        break
    else:
        print("Please try again")

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    if menu == 'r':
        user = input("\n""please enter the username you are registering: ""\n")
        user_pass = input("please enter the password for the user you are registering: ""\n")
        pass_confirm = input("please confirm the password for the user you are registering: ""\n")
        if user_pass == pass_confirm:
            print("\n""Success! New user has been registered""\n")
            user_file.write("\n"f"{user}, {pass_confirm}")
            users = []
            add_user = user + pass_confirm
            users = users.append(add_user)
            break
        else:
            print("Passwords do not match! Please try again")

    elif menu == 'a':
        username = input("\n""please enter the username you want to add a task to: ").lower()
        user_task = input("\n"f"please enter the title of the task you want to add for {username}: ")
        task_desc = input("\n"f"please enter the description of the task you are adding for {username} : ")
        date = input("\n""Please enter today's date in the format " "day mon year:" " e.g 01 Jan 2022: ")
        due_date = input("\n""Please enter the due date in the format " "day mon year:" " e.g 01 Jan 2022: ")
        complete = "No"
        task_file.write("\n"f"{username}, {user_task}, {task_desc}, {due_date}, {date}, {complete}") 
        task_file.close()
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va': 
        va_tasks = open("T21/tasks.txt", "r")
        for line in va_tasks:
            tasks = line.strip().split(", ")
            name = tasks[0]
            task = tasks[1]
            desc = tasks[2]
            assign_date = tasks[3]
            due = tasks[4]
            complete = tasks[5]
            header = ("_")*100
            print(header,"\n" \
                f"Task:                {task}\n" \
                f"Assigned to:         {name}\n" \
                f"Date assigned:       {assign_date}\n" \
                f"Due date:            {due}\n" \
                f"Task complete?       {complete}\n" \
                f"Task description: \n {desc} \n" \
                f"{header}\n")
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        
        vm_tasks = open("T21/tasks.txt", "r")
        for line in vm_tasks:
            tasks = line.strip().split(", ")
            name = tasks[0]
            task = tasks[1]
            desc = tasks[2]
            assign_date = tasks[3]
            due = tasks[4]
            complete = tasks[5]
            header = ("_")*100
            print(header,"\n" \
                f"Task:                {task}\n" \
                f"Assigned to:         {name}\n" \
                f"Date assigned:       {assign_date}\n" \
                f"Due date:            {due}\n" \
                f"Task complete?       {complete}\n" \
                f"Task description: \n {desc} \n" \
                f"{header}\n")
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

