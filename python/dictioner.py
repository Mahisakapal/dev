################################ dictionery ###########################################
# we have dictioner for store data in orgnige way 
# we need { key : value }

user = { "name" : "amardip" , "age" : 26 , "move" : "raaz"}

print(user)

############## we have difrent mathed ##############################
user1 = dict(name = 'amardip' , age = 26, move = 'raaz3' )   # here we never use " " for key word when we use dict 

print(user1)


print(user1['name'])  # in dict we never use indexing we use keyword like name , age , move 


userD = {
     "name" : "amardip" , 
     "age" : 26 , 
     "move" : ["raaz" , "rockstart"] 
     }

print(userD['move'])            # we can add the list in dict 


# how to add data in dict 

userD["move"] = 'raaz3'

print(userD)   

# u can check keyword is there or not in u r dictionery

if 'name' in userD:                 # this mathed for keyword not for value
    print("u have name in dict " )



# if we want to sherch value from dict user below method 

if 'raaz' in userD.values():
    print("u have name in dict " )

# if you want to pritn the all key from dict use belwo 

for i in userD:
    print(i)
    
print("             ")

for i in userD.values():
    print(i)

######################################################
# or we can use the below method 

values = userD.values()
print(values)        # this will return in list 



keyvlau = userD.keys()
print(keyvlau)        # this will return in list 


item = userD.items()
print(item)        # this will return in list to print item 


######################################################

for i , j in userD.items():
    print(f"key is {i} and values is {j}")


######################################################
user1 = dict(name = 'mahi' , age1 = 26, move1 = 'raaz3' ) 
 #userD.pop('nema')      # it will remove this key
# userD.pop()  # this will delete the any random value for dict no need to provied any value 

userD.update(user1)   # thi is use to add from other dict if we have same key than it will replce old with updatw on e

print(userD)
####################################################################################################
# when you want to create diction with same value u can use below method alsoo 

d= dict.fromkeys(['name', 'age','class'], 'samevalues')

print(d)

###################### we have get mathed to access the values of the dict ###########################

print(d.get('name', 'item not found '))  # after dict.get(name of key , instedof non you can writ your woed also )


# u can't use more than one key with same name like name name in this case it will take last key value

