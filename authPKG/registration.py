import re

def readUsers():
    try:
        with open("users.txt", 'r') as f:
            ls = f.readlines()
    except Exception as e:
        print(e)
    return ls


def newUser():
    # getting first and last name from the user
    first_name = input("First Name: ")
    while nameValidation(first_name) == 0:
        print("--- please enter a valid name ---")
        first_name = input("First Name: ")

    last_name = input("Last Name: ")
    while nameValidation(last_name) == 0:
        print("--- please enter a valid name ---")
        last_name = input("Last Name: ")

    # getting email
    email = input("Valid Email: ")
    while emailValidation(email) == 0:
        print("--- please enter a valid email ---")
        email = input("Valid Email: ")

    # getting mobile number
    mobile = input("Mobile(EGY): ")
    while mobileValidation(mobile) == 0:
        print("--- please enter a valid mobile ---")
        mobile = input("Mobile(EGY): ")

    # getting password
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    while passwordValidation(password, confirm_password) == 0:
        print("--- two different passwords ---")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")

    uid = 0
    try:
        with open("users.txt", 'r') as file:
            uid = len(file.readlines())
    except:
        pass

    with open("users.txt", 'a') as file:
        file.write(f'{uid}:{first_name}:{last_name}:{password}:{email}:({mobile})\n')


def nameValidation(sstr):
    return checkRegex('^[-a-zA-Z]+$', sstr)


def emailValidation(sstr):
    # check if it is in our database
    # print that he is already had an email
    # ask him if he forget his password
    try:
        with open("users.txt", 'r') as file:
            for l in file:
                if sstr in l:
                    print("!!! This email is already exists !!!")
                    return 0
    except:
        pass

    return checkRegex(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', sstr)


def mobileValidation(sstr):
    # +20 xxx xxx xxxx
    return checkRegex('^\+20 [0-9]{3} [0-9]{3} [0-9]{4}$', sstr)


def passwordValidation(firstr, secstr):
    if len(firstr) != len(secstr):
        return 0
    else:
        for e in range(len(firstr)):
            if firstr[e] != secstr[e]:
                return 0
    return 1


def checkRegex(regex, sstr):
    if re.compile(regex).match(sstr):
        return 1
    else:
        return 0


def getUser(email, passwd):
    u_email = []
    u_passwd = []
    u_id = []

    try:
        with open("D:\\ITI AI-Track\\Python\\Projects\\Lab_03\\CrowdFunding\\users.txt", 'r') as file:
            for l in file:
                x = l.split(':')
                u_email.append(x[4])
                u_passwd.append(x[3])
                u_id.append(x[0])

    except Exception as e:
        print(e)

    for i in range(len(u_email)):
        if re.fullmatch(email, u_email[i]) and re.fullmatch(passwd, u_passwd[i]):
            return u_id[i]

    return -1
