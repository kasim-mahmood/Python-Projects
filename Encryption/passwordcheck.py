import re

def passwordstrength(password):

    if len(password) < 8:
        return "Weak password"
    234
    if not re.search(r'[A-Z]', password):
        return "Weak password!."
    
    if not re.search(r'[a-z]', password):
        return "Weak password!"
    
    if not re.search(r'[0-9]', password):
        return "Weak password"

    if not re.search(r'[!@#$%^&*]', password):
        return "Weak password!."
    
    return "Strong password!"

password = input("Enter a password: ")

print(passwordstrength(password))