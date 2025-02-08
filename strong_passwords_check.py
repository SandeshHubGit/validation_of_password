## check the strength of the password ##
########### Code Block ####################

def check_password_strength(password):                      # Defin the fucntion name 
    # Checking length of password   
    if len(password) < 8:                                   
        print("password leanght is too short, minimum requried 8 charatctor")                                   
        return False
    # checking password having Uppercase Lowercase special and digit characters 
    # Set the veriable
    up_case = False
    low_case = False
    digit_case = False
    spcialchr_case = False
    # For loop for chacking characters
    for chr_case in (password):
        if chr_case.islower():
            up_case =True
            continue
        if chr_case.isupper():
            low_case = True
            continue
        if chr_case.isdigit():
            digit_case = True
            continue
        else: 
            spcialchr_case = True
    # Loop End
    # After loop cheking which characters are missing from password 
    if not low_case:
            print("Reason: Uppercase letter is missing.")
    if not up_case:
            print("Reason: Lowercase letter is missing.")
    if not digit_case:
            print("Reason: Digit is missing.")
    if not spcialchr_case:
            print("Reason: Special character is missing.")
    # For fuction end, checking all condition are meet 
    if up_case and low_case and digit_case and spcialchr_case:
        return True
    else:
        return False    

## Validation the password 
input_password = input("Enter the password here: ")
if check_password_strength(input_password):
    print ("password meet all criteria")
else:
    print (" password is't meet all criteria. check the reason, and create the valid password")