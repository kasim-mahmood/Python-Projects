import random
import string

password = ' '
characters = string.ascii_letters
numb = string.digits

result = random.choice(characters)
result2 = random.choice(characters)
result3 = random.choice(characters)
result4 = random.choice(characters)
result5 = random.choice(characters)
result6 = random.choice(numb)
result7 = random.choice(numb)
result8 = random.choice(numb)
password = result + result2 + result3 + result4 + result5 + result6 + result7 + result8 

print(password)