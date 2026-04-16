import re

def check_password(password):
    rules = {
        "length": len(password) >= 8,
        "upper": bool(re.search(r"[A-Z]", password)),
        "lower": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(rules.values())

    if score <= 2:
        return "Weak password"
    elif score <= 3:
        return "Average password"
    else:
        return "Strong password"


password = input("Enter a password: ")
print(check_password(password))