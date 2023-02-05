#=====importing libraries===========
from datetime import date
doc_user = open('user.txt', 'r',encoding = 'utf-8')

#=====creating terminal text options===========
# obtained from https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
END = "\033[0m"

#create variables
user = ""
password = ""
user_list = []
count = 0
user_correct = False
password_correct = False
admin = False
new_user = ""
new_pass = ""
confirm_pass = ""
assign = ""
task_title = ""
task_desc = ""
curr_date = ""
due = ""
complete = "No"
new_task_input = ""
user_task_count = 0
task_count = 0
user_count = 0

#====Define functions====

#   create the user registering function
#   first, check if the username already exists. if it does, request a new username. 
#   if both passwords entered match, add to the user.txt file. else, print error message and return to menu
#   if they dont match, provide error message and reload the option menu
def reg_user(x):
    doc_user = open('user.txt', 'r',encoding = 'utf-8')
    user_list = []
    for line in doc_user:
        line = line.strip("\n")
        user_list += line.split(", ")
    doc_user.close()
    new_user = x
    count = 0  
    USER_EXISTS = False  
    while True:
        for i in user_list: 
            if new_user == i and count %2 == 0:         #an even count indicates the usernames and excludes passwords. the new user is compared to all other existing users.
                USER_EXISTS = True                      # if the new user is found in the list of existing users, set USER_EXISTS to true
                break
            count += 1  
        if USER_EXISTS == False:
            break
        else: 
            new_user = input("That user already exists. Please enter a new username: ") # if USER_EXISTS = true, request a new username, reset counter and user_exist variable
            count = 0
            USER_EXISTS = False
            pass


    new_pass = input("Please enter a new password: ")               
    confirm_pass = input("Please confirm the user's password: ")
    
    if confirm_pass == new_pass:
        doc_user = open('user.txt', 'a',encoding = 'utf-8')
        doc_user.write(f"\n{new_user}, {new_pass}")
        doc_user.close()
        print(f"{GREEN}-------------------\nUser added successfully\n-------------------{END}")
    else:
        print(f"{RED}-------------------\nPasswords entered do not match. Please try again.\n-------------------{END}")


def add_task(x):
    #obtain the required user inputs for the task
        assign = x
        task_title = input("Please enter the title of the task: ")
        task_desc = input("Please enter a brief description of the task: ")
        curr_date = input("Please enter the curent date: ")
        due = input("Please enter the due date of the task: ")
        complete = "No"

        #append the document with the input information, print success message
        doc_task = open('tasks.txt', 'a',encoding = 'utf-8')
        doc_task.write(f"\n{assign}, {task_title}, {task_desc}, {curr_date}, {due}, {complete} ")
        doc_task.close()
        print(f"{GREEN}-------------------\nTask added successfully\n-------------------{END}")




#define the view all task function. 
#   the below gets a line from tasks.txt, removes any \n, splits the items into a list.
#   then, the task gets printed out by item of the list, as per the order of the inputs when a task gets added
def view_all(x):
        doc_task = open('tasks.txt', 'r',encoding = 'utf-8')
        print(f"{PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for line in doc_task:
            line = line.replace("\n", "")
            task_info = line.split(", ")

            print(f"""
Task:\t\t\t{task_info[1]}
Assigned to:\t\t{task_info[0]}
Date assigned:\t\t{task_info[3]}
Due date: \t\t{task_info[4]}
Task Complete?\t\t{task_info[5]}
Task Description:\t\t\t
{task_info[2]}            
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        print(f"{END}")    #remove the yellow text         
        doc_task.close()




#if user enters VM, check if the first word in a line is their name. if this is the case, print out that task
#   use the 'user_task_count_ to track if the user has a task assigned to them. If no task was assigned, 
#       print out a message saying no tasks assigned.
def view_mine(x):
        total_task_count = 0
        doc_task = open('tasks.txt', 'r',encoding = 'utf-8')
        user_task_count = 0
        print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for pos, line in enumerate(doc_task,1):
            total_task_count += 1
            line = line.replace("\n", "")
            task_info = line.split(", ")
            if task_info[0] == user:        #if the username of a task is equal to the user currently logged in, print the task details
                user_task_count += 1
                print(f"""
{RED}Task number [{user_task_count}]{CYAN}              
Task heading:\t\t{task_info[1]}
Assigned to:\t\t{task_info[0]}
Date assigned:\t\t{task_info[3]}
Due date: \t\t{task_info[4]}
Task Complete?\t\t{task_info[5]}
Task Description:\t\t\t
{task_info[2]}    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        
        if user_task_count == 0:
            doc_task.close()
            print("No tasks currently assigned to you")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{END}")    


        while True:
            choice = input("Enter a task number to edit a task or enter -1 to return to the menu: ")

            #ensure the input is a number and not a string
            while not choice.isnumeric(): # learnt https://stackoverflow.com/questions/71506942/how-to-add-an-error-message-when-an-integer-is-input-instead-of-a-string
                choice = input(f"{RED}-------------------\nInvalid input.\n-------------------{END} \nPlease enter a task number or enter -1 to return to the menu:")
            choice = int(choice)-1
            
            
            #once a number has been entered, assess what they have entered
            if choice+1 == -1:  
                break
            elif choice >=0 and choice < user_task_count:
                doc_task = open('tasks.txt','r',encoding = 'utf-8')
                data = doc_task.readlines()

                #ensuring the task being edited is the 'Users task (choice)', NOT the 'overall task (choice)'
                # split the line into a list. if the username in line 1 is the user, increase the user task count AND the true position count. 
                # else, just increase the true position count
                true_count = 0
                user_task = 0
                for lines in data:
                    line_list = lines.split(", ")
                    while user_task <= choice:
                        if user == line_list[0]:
                            user_task +=1
                        true_count += 1     
                        break  
            
                #set the line to be edited using the true count, based on the above
                edit_data = data[true_count-1].split(", ")   
                break 

            else:
                print(f"{RED}-------------------\nInvalid input. Try again.\n-------------------{END}")

        

        while True:
            #if the users selection is already Yes, state they cant edit the task, else request input 'action' to understand what the user wishes to do
            if edit_data[-1] == "Yes\n":
                print(f"{RED}-------------------\nThis task is already completed and cannot be edited further\n-------------------{END}")
                break
            else:
                doc_task.close()
                doc_task = open('tasks.txt','w',encoding = 'utf-8')
                action = input(F"{BLUE}Would you like to \na) Mark the task as complete, or \nb) Edit the task?{END}\nEnter 'a' or 'b': ").lower()
                
                #if the user wants to mask the task as completed, edit the completion item in the list and then return to menu
                if action == 'a':
                    
                    
                    if true_count == total_task_count:
                        edit_data[-1] = "Yes"
                    else:
                        edit_data[-1] = "Yes\n"
                    new_data = ', '.join(edit_data)
                    data[true_count-1] = new_data
                    #write the new data into the tasks file and print a success message
                    for line in data:
                        doc_task.write(line)
                    doc_task.close()
                    print(f"{GREEN}-------------------\nTask is now marked as complete.\n-------------------{END}")
                    break

                #Else, if b is selected, edit the appropriate items in the line list basedo n what the user wishes to change - see the below a,b or c
                elif action == 'b':
                    while True:
                        edit = input(f"{BLUE}Would you like to \na) Edit which user the task is assigned to, or \nb) Change the due date of the task, or\nc) Change both of the above?{END}\nEnter 'a', 'b' or 'c': ").lower()
                        if edit == 'a':
                            
                            new_user = input("Which user would you like this task to be assigned to? ") 
                            if new_user in user_list:
                                edit_data[0] = new_user
                                
                                break
                            else:
                                print(f"{RED}User does not exist. Task was not reassigned{END}")
                                edit_data[0] = user
                                CORRECT = False
                                break
                        
                                
                            
                        #obtain the user info based on their input, and overwrite that line in the data.
                        elif edit == 'b':
                            new_due = input("What would you like the new due date to be? ")
                            edit_data[4] = new_due
                            break

                        elif edit == 'c':
                            new_user = input("Which user would you like this task to be assigned to? ")
                            if new_user in user_list:
                                edit_data[0] = new_user
                                pass
                            else:
                                print(f"{RED}User does not exist. Task was not reassigned{END}")
                                edit_data[0] = user
                                CORRECT = False
                                break
                            new_due = input("What would you like the new due date to be? ")
                            edit_data[0] = new_user
                            edit_data[4] = new_due
                            break

                        else:
                            print("Invalid input")
                            continue

                    new_data = ', '.join(edit_data)
                    data[true_count-1] = new_data

                    #write the new data into the tasks file and print a success message
                    for line in data:
                        doc_task.write(line)
                    doc_task.close()        
                    if CORRECT == True:
                        print(f"{GREEN}-------------------\nTask has been successfully edited.\n-------------------{END}")
                    break
                else:
                    print(f"{RED}-------------------\nInvalid input. Try again.\n-------------------{END}")
            
                
def generate_report():
    
    task_overview = open('task_overview.txt', 'w+',encoding = 'utf-8')
    doc_user = open('user.txt', 'r',encoding = 'utf-8')
    doc_task = open('tasks.txt','r',encoding = 'utf-8')


    #======creating the task overview======
    linecount = 0
    completed_task = 0
    today = date.today() # learnt https://www.programiz.com/python-programming/datetime/current-datetime?fbclid=IwAR3sfE4zNCTkn95Ik-tmb7A5F-olVASo1eW-Uze2KrlXd_9fwRpwtAyIUrY
    present = today.strftime("%d %b %Y")
    overdue = 0

    for line in doc_task:
        linecount += 1
        task_list = line.split(', ')
        if task_list[-1] == "Yes\n":
            completed_task +=1

        if task_list[4] > present and task_list[-1] == "No\n":
            overdue += 1   
    uncomplete_task = linecount - completed_task    

    #write all the info to the task_overview.txt file
    task_overview.write(f'''Total number of tasks: {linecount}
Total number of completed tasks: {completed_task}
Total number of uncompleted tasks: {uncomplete_task}
Total number of incomplete, overdue tasks: {overdue}
The percentage of tasks that are incomplete: {(uncomplete_task/linecount)*100}%
The percentage of tasks that are overdue: {(overdue/linecount)*100}%  
''')
    task_overview.close()



    #======Creating the user_overview =======
    user_linecount = 0
    user_dict = {}
    doc_task.seek(0)
    user_complete = {}
    user_overdue = {}

#add the users to the line
    for line in doc_user:
        user_linecount += 1
        line_split = line.split(', ')
        user_dict[line_split[0]] = 0
        user_complete[line_split[0]] = 0
        user_overdue[line_split[0]] = 0

#count the tasks assigned to each user, count the completed tasks and count the overdue tasks
    for line in doc_task:
        line_split = line.split(', ')
        user_dict[line_split[0]] += 1
        if line_split[-1] == "Yes\n":
            user_complete[line_split[0]] += 1
        if (str(line_split[4]) > str(present)) and (line_split[-1] == "No\n"):
            user_overdue[line_split[0]] += 1
    
#now we have 3 dictionaries, containing total tasks, total completed tasks and total overdue tasks. 
#using this info, we can calculate our final statistics - using the variables below 
    TOTAL = linecount
    TOTAL_USER = 0
    TOTAL_PERCENT = 0
    COMPLETE_PERCENT = 0
    INCOMPLETE_PERCENT = 0
    OVERDUE = 0
    output = ''
    final_print = ''

#if the user entered 'ds', run this section so as to print all the text to the terminal. If the total tasks for a user is 0, there is no point of running stats as this will give error
# otherwise, run the calculations for the user and add the info to the output variable
    if menu == 'ds':
        for user in user_dict.keys():
            TOTAL_USER = user_dict[user]
            
            
            if TOTAL_USER == 0:
                output = f'{BLUE}----------{user}----------{END}\n'
                output += f'Total tasks assigned to user:\t\t\t\t{TOTAL_USER}\n'
                print(output)

            else:
                TOTAL_PERCENT = int(user_dict[user])/TOTAL*100
                COMPLETE_PERCENT = int(user_complete[user])/TOTAL_USER*100
                INCOMPLETE_PERCENT = (TOTAL_USER-int(user_complete[user]))/TOTAL_USER*100
                OVERDUE = int(user_overdue[user])/TOTAL_USER*100

                output = f'{BLUE}----------{user}----------{END}\n'
                output += f'Total tasks assigned to user:\t\t\t\t{TOTAL_USER}\n'
                output += f'User tasks as a percentage of total tasks:\t\t{TOTAL_PERCENT}%\n'
                output += f'Completed tasks as a percentage of users total tasks:\t{GREEN}{COMPLETE_PERCENT}%{END}\n'
                output += f'Incomplete tasks as a percentage of users total tasks:\t{YELLOW}{INCOMPLETE_PERCENT}%{END}\n'
                output += f'Overdue tasks as a percentage of users total tasks:\t{RED}{OVERDUE}%{END}\n'
                print(output)
#else, the user entered 'gr' so write all this info to user_overview.txt. all info is written to the text file  
    else:
        for user in user_dict.keys():
            TOTAL_USER = user_dict[user]
            
            
            if TOTAL_USER == 0:
                output = f'----------{user}----------\n'
                output += f'Total tasks assigned to user:\t\t\t\t\t\t\t{TOTAL_USER}\n\n'
                final_print += output

            else:
                TOTAL_PERCENT = int(user_dict[user])/TOTAL*100
                COMPLETE_PERCENT = int(user_complete[user])/TOTAL_USER*100
                INCOMPLETE_PERCENT = (TOTAL_USER-int(user_complete[user]))/TOTAL_USER*100
                OVERDUE = int(user_overdue[user])/TOTAL_USER*100

                output = f'----------{user}----------\n'
                output += f'Total tasks assigned to user:\t\t\t\t\t\t\t{TOTAL_USER}\n'
                output += f'User tasks as a percentage of total tasks:\t\t\t\t{TOTAL_PERCENT}%\n'
                output += f'Completed tasks as a percentage of users total tasks:\t{COMPLETE_PERCENT}%\n'
                output += f'Incomplete tasks as a percentage of users total tasks:\t{INCOMPLETE_PERCENT}%\n'
                output += f'Overdue tasks as a percentage of users total tasks:\t\t{OVERDUE}%\n\n'
                final_print += output
        user_overview = open('user_overview.txt', 'w+',encoding = 'utf-8')
        user_overview.write(final_print)
        user_overview.close()
           



#====Login Section====

#create lines of users, excluding the "\n" that is passively included in the text file
for line in doc_user:
    line = line.strip("\n")
    user_list += line.split(", ")


# the below while loop obtains a user input.
#   for the input, it assesses if the name is in the list of users - i.e. every second input in the user list
#       if the users input is equal to a name in the list, and is a username - not a password,
#           mark the user input as true.
     
while True:
    user = input("Please enter your username: ")
    if user == "admin":
        admin = True
    for i in user_list: 
        if user == i and count %2 == 0:         #an even count indicates the usernames and excludes passwords
            user_correct = True
            count =user_list.index(i)+1         #finds the index of the username, + 1, to ensure the password following the user login is correct 
            break
        count += 1
    if user_correct == True:
        print(f"{GREEN}-------------------\nValid username.\n-------------------{END}")
        break 
    else:
        print(f"{RED}-------------------\nInvalid username. Try Again\n-------------------{END}")


#once a username is input, a user must enter the password associated with that username, not just any password in the list
#   as such, the "count" variable tracks the next item in the list of usernames & passwords
#       the password entered must agree to the user input and if entered, the password is valid
while True:
    password = input("Please enter your password: ")
    if password == user_list[count]:
        print(f"{GREEN}-------------------\nValid password.\n-------------------{END}")
        break
    else:
        print(f"{RED}-------------------\nInvalid password. Try Again\n-------------------{END}")

doc_user.close()


#once a user is logged in, the menu loop begins, only terminating when 'e' for exit is entered. the menu options are broken down below
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if admin == True:
        print(f"{BOLD}{UNDERLINE}{YELLOW}Menu:{END}")
        menu = input(f'''{YELLOW}Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - Display statistics
e - Exit{END}
User selection: ''').lower()
    else:
        print(f"{BOLD}{UNDERLINE}{YELLOW}Menu:{END}")
        menu = input(f'''{YELLOW}Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit{END}
User selection: ''').lower()
    

# if a user tries to register, check if they are an admin. If this is the case, run function reg_user and request a username.
    if menu == 'r':
        if admin == True: 
            reg_user(input("Please enter a new username: "))
            pass       
        #if the user is not an admin, print error message and return to menu
        else:
            print(f"{RED}-------------------\nOnly the admin can register new users. Select a different option.\n-------------------{END}")
            pass   
          
#if a user wants to add a task, run function 'add_task'
    elif menu == 'a':
        add_task(input("Please enter the username of the person to whom the task shall be assigned: "))
        pass
        

#if user enters va, run view_all function
    elif menu == 'va':
        view_all('true')
        pass

#if user enters vm, run view_mine function
    elif menu == 'vm':
        view_mine('true')

#if the user is admin and types 'ds', run generate_report function with the output being printed to terminal 
    elif menu == 'ds' and admin == True:
        generate_report()       

#if the user is admin and types 'gr', run generate_report function with the output being written to text file 'user_overview.txt' 
    elif menu == 'gr' and admin == True:
        generate_report()
        print(F'{GREEN}-------------------\nReport successfully generated.\n-------------------{END}')




#printing of exit or incorrect input texts
    elif menu == 'e':
        print(f'{YELLOW}-------------------\nGoodbye!!!\n-------------------{END}')
        exit()

    else:
        print(f"{RED}-------------------\nYou have made a wrong choice, Please Try again\n-------------------{END}")


