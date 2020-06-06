# now we use for loop it' more simple than while but same function 

for i in range(10):    # we run below code till i is become 10 u don't have to increment it "in range is most imp word"

    print(f"hello wordl ")  #  ## no need of increment 

    ###########or else same as below 

for i in range(1,11) :   # as you know the index start from 0 this will run only 
    print(i)   


########### example ###################  

total = 0

for i in range (1 , 11) :
    
    total += i

print(total)    


############################ exmple for testing #####################################

name = input("enter your name : ")

total = 0
temp =""

for i in range(len(name)):
    total += i
    if name[i] not in temp:
       print(f"{name[i]} : {name.count(name[i]) }")
       temp += name[i]   