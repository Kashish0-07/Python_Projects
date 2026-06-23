import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbol=['!','@','#','$','%','^','&','*','+','(',')']

print("Welcome to Password Generator!!")
n_letters=int(input("How Many Letters You Want In Your Password?\n"))
n_symbols=int(input("How Many Symbols You Want In Your Password?\n"))
n_numbers=int(input("How Many Numbers You Want In Your Password?\n"))
Password_List=[]
for i in range(1,n_letters+1):
  char=random.choice(letters)
  Password_List+=char

for i in range(1,n_symbols+1):
  char=random.choice(letters)
  Password_List+=char

  for i in range(1,n_numbers+1):
   char=random.choice(letters)
   Password_List+=char

print(Password_List)  
random.shuffle(Password_List)
print(Password_List)
password=""
for char in password:
  password+=char

print(password)  