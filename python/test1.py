############################################################
############ now we look user string indexing   #############
#############################################################

# in indexing we can start from 0 , 0=p 1=y 2=t 3=h 4=o 5=n
# revers order use -1 ,-2 so on 

my_var = "python_myString "

print(f"{my_var [0]}")
print(f"{my_var [1]}")
print(f"{my_var [2]}")
print(f"{my_var [3]}")
print(f"{my_var [4]}")
print(f"{my_var [5]}")


print(f"this is for revores order {my_var [5]}")


print(F"print {my_var[1:15]}") # in this cas we [satrtnumer : ending numner ] ending number is should 1 extra in this case 


print(f"this is for check the complit string {my_var[:]}")

print("amardip"[0:4])

print("amardip"[0:7:2]) # in this last 2 is shwoing incerge by 2

print("amardip"[7::-1]) #this for print in revoers but we start from last like 7

# or like this 

print("amardip"[-1::-1])

# or like this 

print("amardip"[::-1])

############################################################
############ now we look user string mathod    #############
#############################################################

my_var= "ThiS check for varable CAPALL"

print(len(my_var))  # this is to get the leght with sapce of your var for string

print(len("amardip"))

######### be  cearfull in function we use direact but in mathod we use . dot 

print(my_var.lower()) # lower mathod

print(my_var.upper())  #uper mathod 

print(my_var.title())   #title mathod  1 cap all samol

print(my_var.count(" c"))  # partical carecater 

############################################################
############ now we look user exsesize     #############
#############################################################

name , charecter = input("plese enter name & charecter you want to shearch use , to sepret : ").split(",")

print(f"this is the legnth of your name {len(name)} & count of {charecter} is {name.lower().count(charecter.lower())}")

## this is the right exmaple in abow line 

print(f"{len(name)}")

print(f"this count of {charecter} {name.strip().lower().count(charecter.strip().lower())}") # here we remove space

#normale we user to do print(f"name.count(charchater)")


