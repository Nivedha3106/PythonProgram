# Strong password checker 
# Must have at least 1 uppercase letter
# Must have at least 1 lowercase letter
# Must have at least 1 special character
# Must  be at least 8 characters long and at most 16 characters long
# Must have  at  least 1 number
# Must not have two consecutive characters that are same



def is_strong_password(password):

    if len(password) <= 8:
        return False, "Password length must be more than 8 characters long."
    
    if len(password) >= 16:
        return False, "Password length must be less than 16 characters long."
    
    up = False
    for i in password:
        if i.isupper():
            up = True
            break
    if not up:
        return False, "Password must have at least one uppercase letter."
    
    lc = False
    for i in password:
        if i.islower():
            lc = True
            break
    if not lc:
        return False, "Password must have at least one lowercase letter."
    
    sp = False
    for i in password:
        if i in "!@#$%^&*()_+-={}[]:;\"'<>,.?/|\\":
            sp = True
            break
    if not sp:
        return False, "Password must have at least one special character."
    
    
    dig = False
    for i in password:
        if i.isdigit():
            dig = True
            break
    if not dig:
        return False, "Password must have at least one number."
    
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            return False, "Password must not have two consecutive characters that are the same."
    
    return True, "Password is strong."

password = input("Enter password: ")
is_strong, message = is_strong_password(password)
print(message)
