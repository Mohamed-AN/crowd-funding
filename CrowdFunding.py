import authPKG.projects as projects
import authPKG.registration as registration


def printMenu():
    print("############### DASH_BOARD ###############")
    print(" 1 ---> create project\n"
          " 2 ---> edit project\n"
          " 3 ---> delete project\n"
          " 4 ---> view all projects\n"
          " 5 ---> search by date\n"
          " 6 ---> exit\n", end='')
    print("##########################################")

    return input("Please enter the action number: ")


flag = 1
while flag:
    user = input("Please enter 'l' for login, 'r' for registration, and 'q' for exit: ")
    if user == 'l':
        email = input("E-mail: ")
        password = input("Password: ")
        uid = registration.getUser(email, password)
        if uid == -1:
            print("Invalid email or password")
        else:
            while flag:
                # printing our main menu and get the action from the user
                a = printMenu()

                # creating a new project
                if a == '1':
                    pid = projects.createProject()
                    users = registration.readUsers()
                    cur_user = users[int(uid)]
                    if cur_user[-2] == ')':
                        cur_user = cur_user[:-1] + f':{pid},\n'
                    else:
                        cur_user = cur_user[:-1] + f'{pid},\n'
                    users[int(uid)] = cur_user

                    # modifying our users database
                    try:
                        with open("users.txt", 'w') as file:
                            file.writelines(users)
                    except Exception as e:
                        print(e)

                # edit a project
                elif a == '2':
                    users = registration.readUsers()
                    proj_dict = projects.projectNames(users[int(uid)].split(':')[-1].split(',')[:-1])
                    proj_name = input(f"which one do you want to edit {list(proj_dict.keys())}: ")
                    modified_proj = proj_dict[proj_name]

                    # ask current user until he finish his updates
                    flag = 'y'
                    while flag == 'y':
                        modified_proj = projects.editProject(modified_proj)
                        print(modified_proj)
                        flag = input("do you want to edit another field? (y/n) ")

                    # reading our projects from our database
                    users_projects = projects.readProjects()
                    for i in range(len(users_projects)):
                        if users_projects[i].split(':')[0] == proj_dict[proj_name].split(':')[0]:
                            users_projects[i] = modified_proj
                            break

                    # update our projects database
                    with open("projects.txt", 'w') as file:
                        file.writelines(users_projects)

                # delete one project
                elif a == '3':
                    users = registration.readUsers()
                    proj_dict = projects.projectNames(users[int(uid)].split(':')[-1].split(',')[:-1])

                    # getting the project name to be deleted
                    name = input(f"which one do you want to delete {list(proj_dict.keys())}: ")
                    while name not in list(proj_dict.keys()) and name != 'q':
                        name = input(f"Invalid name for your projects, {list(proj_dict.keys())}: ")

                    if name == 'q':
                        pass
                    else:
                        users_projects = projects.readProjects()
                        users_projects_mod = []
                        for i in range(len(users_projects)):
                            if users_projects[i].split(':')[0] == proj_dict[name].split(':')[0]:
                                continue
                            else:
                                users_projects_mod.append(users_projects[i])
                        with open("projects.txt", 'w') as file:
                            file.writelines(users_projects_mod)

                        pid_mod = ''
                        for i in proj_dict:
                            if i == name:
                                continue
                            else:
                                pid_mod += proj_dict[i].split(':')[0] + ','
                        pid_mod += '\n'
                        x = users[int(uid)].split(':')[:-1]
                        x.append(pid_mod)
                        users[int(uid)] = ':'.join(x)
                        with open("users.txt", 'w') as file:
                            file.writelines(users)

                # display all projects details
                elif a == '4':
                    users_projects = projects.readProjects()
                    for i in users_projects:
                        print(i, end='')

                # search by date
                elif a == '5':
                    start_date = input("Please enter the date to search (DD-MM-YYYY): ")
                    print(projects.searchByDate(start_date))

                # exit
                elif a == '6':
                    flag = 0

                else:
                    print("Please enter a valid action")

    elif user == 'r':
        registration.newUser()

    elif user == 'q':
        flag = 0

    else:
        print("Eneter a valid character ['l', 'r', 'q']")
