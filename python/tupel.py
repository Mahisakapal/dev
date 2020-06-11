############################ exmple for trumpel ####################################
#  this is tupel is use for fix value u cant change the value of tuple it is like ()
tump= (1,2,3,4,5,)

print (tump)

# cant make trumpl wihout ( ) & , if you like this 

one= (1,)  # if you have only one than also we have to use , after value 


# this is also tupel 

test = "testing ", "testing 2" ,"test3"

print(type(test))

print(test)


# you can assing the values of the tupel to any var like below 

var1 , var2, var3 = test   # we have to lentgh of tuple = number of the  var  

print(var1 , var2 , var3)

# this abow method call as tupel unpacking 

### here we try to add the list inside tupel and use the list method like add & del 

tup = ("val", [1, 2,3,9,8,7]  )

tup[1].append("we added")

tup[1].pop(3)

print(tup)


print (min(tump))
print (max(tump))
print (sum(tump))


# now we check when we use 2 retune in function it give you tuple to solve this we can do belwo method 


def func(int1, int2):
    add = int1+ int2
    mul = int1 * int2
    return add , mul

out1 , out2 = func(2,3)

print(out1 , out2 ) 
