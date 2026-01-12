password_check = "12345"
if len(password_check) < 6:
    print("weak")
elif len(password_check) >6 and len(password_check) < 10:
    print("medium")
else:
    print("strong")        