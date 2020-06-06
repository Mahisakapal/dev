
# below is the example of list or array 

number = [1, 2, 3, 4, 5, 6]


word = ["test1" , "test2" , "test3", "test4"]

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