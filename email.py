import re
email = input()
if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z]+\.[a-zA-Z]+$", email):
    print("OK")
else:
    print ("WRONG")
