########################################################################
#                   we will undstand the set                           #
#             this is alwasy unoreder but uniq itme                    #
#           you can't add dict , tuple & list in side set              # 
########################################################################
 
 # in set we dos't need the key we can directly use values

s = {1, 2, 3,4 ,2}  # if you add same vlaues twice you will get only one 

print(s)

# where we use set when we have duplicate item we use set 

l = [2,4,5,6,7,8,9,3,4,5,6,2,47,8,9,]   # here we have some dublicate now we are going remove that values

print(l)

print(" without set it's look like abow ")


s1= list(set(l))  # v use set than pass our list in that 
print (s1)

s1.remove(9) # this is to remove item 

print(" using  set it's look like abow ")

s.add(7) # this to add new values 

s.remove(1) # this is to remove item 

print (s)

# in remove method we have some error like when we pass value whice is not percent in our set 
# it will thro the error to you for this issue we use discard methad 


s.discard(11)
print (s)
s.clear()
print(s)

for i in s1 :
    print(i)            # same as pthe to check or print all the item in set 

## we can use union or intersection mether in set 

d1= {1,2,3,4,5,}
d2= {9,2,6,7,5,}

print(d1 | d2 )   # "|" use for union 

print (d1 & d2)  # "&" for intersection


