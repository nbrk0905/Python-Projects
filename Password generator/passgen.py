#Password Generator Project
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to the PyPassword Generator!")
nletters=int(input(f"How many letters would you need?:\n"))
nsymbols=int(input(f"How many symbols would you need?:\n"))
nnumbers=int(input(f"How many numbers would you need?:\n"))
password_list=[]
for char in range(1,nletters+1):
    randomchar=random.choice(letters)
    password_list+=randomchar
for char in range(1,nnumbers+1):
    password_list+=random.choice(numbers)
for char in range(1,nsymbols+1):
    password_list+=random.choice(symbols)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"Your password is: {password}")        
