# email = input("What is your email? ").strip()
# # if "@" and "." in email:
# #   print("valid")
# # else:
# #   print("Invalid")  
# username,domain = email.split('@')

# # if username and "." in domain:
# if username and domain.endswith(".com"):
#   print("Valid")
# else:
#   print("Invalid")  

# Regex

import re
email = input("What is your email? ").strip()
# if re.search("..*@..*",email):
# if re.search(r"^.+@.+\.com$",email):
# if re.search(r"^[^@]+@[^@]+\.com$",email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$",email):
# if re.search(r"^\w+@\w+\.com$",email):
if re.search(r"^\w+@\w+\.(edu|gov|com)$",email,re.IGNORECASE):
  print("Valid")
else:
   print("Invalid")  