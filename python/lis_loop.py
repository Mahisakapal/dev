num=[1,2,3,4,9,8,7,6,5]

for i in num:
    
    print (i)
print("               this is new list            ")
i =0 

while i < len(num):
    i+=1
    
    print(i)
print("               this is new list            ")


num1 = [[1, 2, 3,], [8, 9, 7], [4, 6, 5]]

print(num1[1])
print("               this is new list            ")


for sublist in num1:
    for i in sublist :
        print(i, end = "")   # here we use , end = "" to print in on row or in line 



###########################################################################
# to check your data type we have type 

s="amadip"
num
print(type(s))
print(type(num))        

############################ exmple for testing #####################################


number = list(range(1, 21))  # we use lsit and range function to ganret the list 

print(number)


print (number.pop())  # if you want to knwo which item is dele by pop u can use this methid  u can stor it in var also 


print(number)

print(number.index(10 , 1 , ))  # we can find the postion of item using index methid 
                                # the second argument is for where to start sharching 
                                # & 3rd parameter is for where to end shearching     

############################ exmple for testing #####################################
# here we creat function & pass input of our list 

def print_nig(l) :
    negative = []
    for i in l:
       negative.append(-i)
    return negative

print(print_nig(number))

 