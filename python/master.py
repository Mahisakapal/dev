def myfunc( * args):   ### when we want method which will take more than 2 in punt we can use * args 
    total = 0 
    for num in args:
        total += num
    return total


print(myfunc(1,2,3,4,56,78,))


def multyply( * args):   ### when we use 1 more paramiter with * args it consider u r input first value as first paramiter  (num )  
    total = 1 
    for num in args:
        total *= num # doing mult 
    return total

print(multyply(2,3,4,56,78,))



# alwasy first num & than only *args 
def multyply1( num, * args):   ### when we use 1 more paramiter with * args it consider u r input first value as first paramiter  (num )  atlis one input is req
    total = 1               
    for num in args:
        total *= num # doing mult 
    return total

print(multyply1(2,3,4,56,78,))




# alwasy first num & than only *args 
def multyply11( num, * args):   ### when we use 1 more paramiter with * args it consider u r input first value as first paramiter  (num )  atlis one input is req
    total = 1               
    for num in args:
        total *= num # doing mult 
    return total

num = [2,3,4,56,78,]
print(multyply11(* num))  # when you have methid with  *arsg * you want to pass list so u have to add * befor listname in parameter 


