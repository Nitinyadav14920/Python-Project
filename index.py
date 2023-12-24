# a to z 
# 0 to 9
# . _ one time 
# @ one time
# .  2 3


import re

email_condition = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
user_email = input("Please enter your email address: ")

if(re.search(email_condition, user_email)):
    print("Your email address is valid", user_email )
else:
    print("Your email address is Invalid", user_email )