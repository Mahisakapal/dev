# we use defult input when we don't know we will eneter the paramiter or not 

def defuult_pr(a,b,c=26 ):   # here we set age 26 as defult value if you nver enter anything 
    print(a , b ,c)         # IMP dfult is 

defuult_pr("amardip", "sakapla" )


# when you defind var inside your function it is local function 
# you can't access this var from  for function dircatly to acive this make your var glaoble 
# like defined it out of your functio 


x= 5  # this is the globel var

def func( ):
    global x            # here we access globle var & chneg it 
    x = 7           # this is the locall var 
    return x        
print(func())   # it will return only local var  untill you never add global 

print (x)   # it retunr only globel var 