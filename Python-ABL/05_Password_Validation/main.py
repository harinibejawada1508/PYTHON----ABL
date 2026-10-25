password = input("Create a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
specials = "!@#$%^&*()-_+=?"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in specials:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password meets the sample policy")
else:
    print("Password does not meet the policy")
    print("Use 8+ characters, uppercase and lowercase letters, a digit, and a special character.")
