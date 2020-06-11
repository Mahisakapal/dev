
# below is the example of list or array 
# add & remove append , extend , insert  or remove , dell pop

number = [8,1,7, 2, 3,9, 4, 5, 6]


word = ["test1" ,"test1", "test2" , "test3", "test4" , "a", "z", "f", "m"]

print(word[:2])  # is print first 2 value 

mix= [ 1,2,3,4, "test2" , "test3", "test4"]   # this is mix list (array )


mix[1]="two"   # we assing this value to our insex in position 1 
print(number)
print(word)
print(mix)
print(mix[-1]) # we print last value of list 

mix[1:] = 'two' # it replease next to 1 postive value with two like t, w, o 

print (mix)

mix[1:] = ['two','three','four']   # it replcae with this list to old lest after 1 postion 

print (mix)


########################################################################################
#                           now we check append method 
########################################################################################

# this method use to add data in u r list but don't forget it add data in last of your list

mylist = [1, 2, 3, 4,]

print(mylist)

mylist.append('5')

print(mylist)


########################################################################################
#                           now we check insert method 
########################################################################################

mylist = [1, 2, 3, 4,]

print(mylist)

mylist1 = [10, 20, 30, 40,]

mylist.insert(0, '5')

myword = ["testing", "coding","algorethm "]

print(mylist + mylist1 )

mylist.extend(myword)

print(mylist)

########################################################################################
#                           now we check POP method 
########################################################################################

# this is use to delete the data from our list 

print(f" { mix}  thsi si print mix list as it is ")

mix.pop( 1)  # bydefult it will remove the last value or data from your list if you never provide indwx valus

print(f"  {mix}  this is print mix after pop ")

########################################################################################
#                           now we check del method 
########################################################################################
del mix[1]  # it delete from index postive 


print(f"{mix } useing del method ")

########################################################################################
#                           now we check remove method 
########################################################################################
# this is use to remove item from list by his name 

print(word)

word.remove("test1") # if yu have more thane 1 item with same name it will remove only first one 



########################################################################################
#                           now we check item is present or not 
########################################################################################

# to check item is present or not in your list 

if "test1" in word:

    print("we have test1 in our list ")

else:

    print(" we don't have test1 in our list")

print (word.count("test1"))    

word.sort()   # it do sort to your list 

print (word)

print(sorted(number))  # this is not like sort it noly print sort order this is sorted 

print(number)
#####################################################################################
# when you use clear function it will make empty your list

number_copy = number.copy()  # it is copy data from  number list & asseing it to number_copy list

number.clear()


print(number)   # due to clear methid it is empty 

print(number_copy)