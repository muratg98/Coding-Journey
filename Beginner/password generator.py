import random
print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
syms = list('~`! @#$%^&*()_-+={[}]|\:;"<,>.?/')
nums = list('0123456789')
password = list()

while letters > 0:
    randompicker = random.randint(0, len(alphabet)-1)
    password.append(alphabet[randompicker])
    letters = letters - 1
while symbols > 0:
    randompicker = random.randint(0, len(syms)-1)
    password.append(syms[randompicker])
    symbols = symbols - 1
while numbers > 0:
    randompicker = random.randint(0, len(nums)-1)
    password.append(nums[randompicker])
    numbers = numbers - 1

random.shuffle(password)
password = ''.join(password)
print(password)
#print(password)

