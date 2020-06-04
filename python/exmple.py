

num=input("please enter number taht is more than 2 digit like 11, 22, 86  :")

total=0

i= 0

while i < len(num) :

    total += int(num[i])
    i += 1 
print(total  )


################next exmple ###################
name = input("enter your name ")
temp_var=""   # set blank 
i =0 

while i < len(name):              # run code till lenth of name 
    if name[i] not in temp_var:   #we check  name cahercter in not in team_var 
        temp_var += name[i]       #than we add temp_var  name charcter + name charcter index+1  
        print (f"{name[i] } : {name.count(name[i])} ")  # name charcter : name.count(nme charter )
    i +=1


#####################infint loop ##############################
# this is to run your loop continusly 

#                           while True:
#                               print("check")
    