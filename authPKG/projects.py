import re


def readProjects():
    try:
        with open("projects.txt", 'r') as f:
            ls = f.readlines()
    except Exception as e:
        print(e)
    return ls


def projectNames(*args):
    proj_dict = {}
    ls = readProjects()
    for i in range(len(args[0])):
        for j in range(len(ls)):
            if args[0][i] == ls[j].split(':')[0]:
                proj_dict[ls[j].split(':')[1]] = ls[j]

    return proj_dict


def searchByDate(startdate):
    ls = readProjects()
    projs = []
    for l in ls:
        if l.split(':')[4] == startdate:
            projs.append(l)
    return projs


def createProject():
    title = input("Project Title: ")
    details = input("Project Details: ")
    total = input("Total Target: ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")

    pid = 0
    try:
        with open("projects.txt", 'r') as file:
            pid = len(file.readlines())
    except:
        pass

    with open("projects.txt", 'a') as file:
        file.write(f'{pid}:{title}:{details}:{total}:{start_date}:{end_date}\n')

    return pid


def editProject(proj):
    proj_fields = proj.split(':')
    field = input("which field ['title', 'details', 'total target', 'start date', 'end date']: ")
    if field == 'title':
        title = input("New Title: ")
        proj_fields[1] = title

    elif field == 'details':
        details = input("New Details: ")
        proj_fields[2] = details

    elif field == 'total target':
        total_target = input("New Target: ")
        proj_fields[3] = total_target

    elif field == 'start date':
        start_date = input("New Date: ")
        proj_fields[4] = start_date

    elif field == 'end date':
        end_date = input("New Date: ")
        proj_fields[5] = end_date + '\n'

    return ':'.join(proj_fields)
