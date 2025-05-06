import datetime
import re  

OUTPUT_FILE = "./checking_password_log.txt"
INPUT_FILE = "./common_passwords.txt"

def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def read_in_file(filename):
    with open(filename, "r") as f:
            return f.read()

PASSWORD_CRITERIA = {
    "length": re.compile(r".{8,}"),  # Minimum 8 characters
    "uppercase": re.compile(r"[A-Z]"),  # Must have uppercase letters
    "lowercase": re.compile(r"[a-z]"),  # Must have lowercase letters
    "digit": re.compile(r"[0-9]"),  # Must have digits
    "special_char": re.compile(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/\|=]"),  # Must have special characters
}

def scramble(string):
     return string[-2:] + string [2:-2] + string [:2]

def log_password(scrambled):
    with open("./entered_passwords.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{scrambled}")

def is_strong_password(password):
    for criteria in PASSWORD_CRITERIA.values():
        if not criteria.search(password):  
            return False
    return True

def get_password_strength(password):
    conditions_passed = 0
    for criteria in PASSWORD_CRITERIA.values():
        if criteria.search(password):  
            conditions_passed += 1

    if conditions_passed == 5:
        return "Strong"
    elif conditions_passed >= 3:
        return "Medium"
    else:
        return "Weak"

def log_all(password, strength, scrambled): 
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:   
        f.write(f"scrambled password {scrambled}. Tested at {get_current_datetime_formatted()}. Password str was {strength}\n")

def log_timestamp(password,strength):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"password {password} tested at {get_current_datetime_formatted()}. Password str was {strength}\n")

def test_all_passwords(pw_list):
    for password in pw_list:
        strength = get_password_strength(password)
        print(f"Password is {password}. Password strength: {strength}")
        #log_timestamp(password,strength) # - would commit every test one to the file- removed for now

def get_password_from_user():
    while True:  # Loop until a strong password is entered
        password = input("Please enter your password: ")

        strength = get_password_strength(password)
        print(f"Password strength: {strength}")
        #log_timestamp(password,strength)

        #log_password(scramble(password))

        log_all(password, strength, scramble(password))

        if password in lines:   
            print ("your password is SO common that it's in the file")
        #else:
            #print ("it's not in the file")

        if strength == "Strong":
            print("Your password is strong.")
            break
        else:
            print("Password does not meet the criteria. Please enter a different password.")

# Read in the poor passwords (replace with actual implementation)
#poor_passwords = read_in_file(OUTPUT_FILE)
poor_passwords = read_in_file(INPUT_FILE)

pw_list = poor_passwords.split("\n")
print (pw_list)
test_all_passwords(pw_list)
# Main execution
#get_password_from_user()

with open(INPUT_FILE,"r", encoding="utf-8") as file: # handles closing atomatically. figure out behaviour of when file exists and doesnt exist 
    data = file.read()
lines = data.split("\n")

print (lines)

get_password_from_user()

