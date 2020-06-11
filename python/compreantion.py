# comperantion use to mak your code samll
# basicaly we use below method 

a = []

for i in range (1, 11) :
    a.append(i ** 2)
print(a)

######## this is paytho method 

b = [ i **2 for i in range (10, 21) ]
print (b)

b1 = [-i for i in range (1, 11)]

print(b1)

name = ["amardip", "sakapal","mahi"]
Nl=[i[0] for i in name]

print(Nl)


print( [i[::-1] for i in name ])  # this is to short this is my method in this loop name is list 



def reves(l):           # this is other method 
    return [i[::-1] for i in l ]

print(reves(["amardip", "sakapal","mahi"]))


################################# how to make if satement in pythonic way #################################


num = list(range(1 , 11))
# in old way we can use belwo code 
tmp= []
for i in num:
    if i%2 == 0:
        tmp.append(i)
print(tmp)

################################ pythonic way #################################

res = [i for i in num if i%2 == 0 ]   # in this if methis one setmend & for i in name is defrent meth the first i is var

print(res)
#            |-----------|                  check odd in num list using for loop 
#        |---|-----------|-------------|    it check this if setment tahn assing the curnt value to odd   
res1 = [odd for odd in num if odd%2 != 0]  # this is also same but we tack odd 

print(res1)

# short way to abow code we range enstend of list 

res3 = [i for i in range(1,20) if i%2 != 0]

print(res3)

#################################################################################
def testnuc(l):
#                    |------|   run for loop 
#           |--------|------|-----------------------|  # this will check if stement if ture & convert int or folt   
    return [str(i) for i in l if type(i)== int or type(i) == float] # this code only print int & folat

print(testnuc(["amardip", "sakapal","mahi",1 , 3,3.05, 8, 9] ))    

num = [1,2,3,4,5,6,7,9]
#                    
#       |-----------| it checkc this if stament than print i*2    
newL= [i *2 if (i%2 ==0 ) else -i for i in num ]   # when we use else than we hav to use if in starting of statment
#                           |-----------------------|  than run this code & print -i values 


