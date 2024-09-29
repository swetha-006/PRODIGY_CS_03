import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:  # Loop through the password directly
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Weak Password!!!"
    elif strength == 2:
        remarks = "Not A Good Password!!!"
    elif strength == 3:
        remarks = "It's a weak password, consider changing."
    elif strength == 4:
        remarks = "It's a hard password, but can be better."
    elif strength == 5:
        remarks = "A very strong password."

    print(remarks)

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input('Do you want to enter another password (y/n): ')
    else:
        choice = input('Do you want to check a password (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid input, please try again.')
            choice = input('Do you want to check a password (y/n): ')

if __name__ == '__main__':
    print("PASSWORD STRENGTH CHECKER")
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
