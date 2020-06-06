## in python we have to do leas coding & avoid repitasion of code 
## eg "len"  function.   once you defind fun u can call it when you want, 


def my_fun_add(num1, num2 ):  # we defined function with "def" your_fun_name (parmeter1 , parameter2)  
    
    return num1 + num2      # return is not like print but u can use print also it run the code & assine value to function 
                            # here we do lease code but in orignale fun we have do loat of code 

print(my_fun_add(278, 568)) # here we never call return or not do addiction we just call fun & provided 2 number 



################# we replaec the retunr to print 

def add_fun_three(a,b,c):
    print(a+b+c)       # here we user print not retrun so no need to user print when you call it 

add_fun_three(24,6767,896)    



#################### parctice ######################################

def las_cahr(name):
    return name[-1]

print(las_cahr("amardip" ))    

#################### parctice ######################################

def odd_even(number):
     
    if number%2 ==0:
        return "even"
    else :
        return "odd"     
print(odd_even(15000002))

#################### parctice same as abow but less code ######################################

def odd_even1(number):
     
    if number%2 ==0:
        return "even"
                                        ######## no code no else 
    return "odd"     
print(odd_even1(15000002))


#################### parctice ######################################


def is_even(number):
    if number%2 == 0:
        return True
    else :
        return False
print(is_even(786))    



#################### parctice same as abow but less code ######################################

def check_even(num):    # this IMP of python 
    return num%2 ==0 
print(is_even(786))  


######### we can def fun with any paramater & call it bake 

def witout_inp():  # here we never set parameter or never ask for input 
    return   "withou input  funcation "
print (witout_inp())    

#################### exresize ########################################


in1 , in2 , in3  = (input("neter 3 number seprit by , : ").split(","))


def check_number (a , b , c):
    if a < b and b < c  :
        return (f"{c}  is greter than  {a}  and {b}")
    elif a > b and b > c :
            return (f"{a}  is greter than  {b} and {c} ")
        
    return (f"{b}  is greter than  {a} and {c} ")

print (check_number( int(in1), int(in2) , int(in3)))    


#### you can call other fun in your fun

