import random
import string

password_len=15

pass_values=string.ascii_letters + string.digits + string.punctuation

## Using list comprehension

password="".join([random.choice(pass_values) for i in range(password_len)])

# password=""

# for i in range(password_len):
#     password += random.choice(pass_values)

print(f"Your random password is:{password}")
