userdata = {}

name = input("what is your name ")
age = input("what is your age ")
move = input("move you like  if more than one use , ").split(",")

userdata['name']= name
userdata['age'] = age 
userdata['move'] = move
for key , values in userdata.items():
    print(f"{key} : {values}")
