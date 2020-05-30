print("'jay shri 'manjunath 'blass me '")
## this is the commit you can print "word " or 'word' or combint 
## you can't " "this" " or ' 'this' ' mud mixmatch  


#############################################################
########################## Now Escape Sequences #############
#############################################################

## to " " in to anther " " you have add \  after evry " "

##  \' = single quote
##  \\" = duble quote
##  \\  = backshlash
##  \n  = new line
##  \t  = tab
##  \b  = baksapce   


print ("this exmple for \"testing \"  " )

print ('i\'m amardip')

print("this is use to when you need  backshalsh in end of word use 2 backshalsh \\")

print ("use \\\\ for \\ to print ")

print ("line A \nline B")

print ("check your tab\t  this to tab in your txt")

print ("this help you to get backsapce\b check this mahi\b ") # it remove last liter or give backsapash 


#############################################################
############################# this is exercise #############
#############################################################
print ("\\\\")

print("/\\/\\/\\/\\")

print('  \\"  \\n  \\t ' "\\' " )

print ("\\\" \\n \\t \\\' ")


## it u use "r" in start of your string it's not reacte 

print(r"this is A \n  this is B\t")

#############################################################
############################# now we look emoji #############
#############################################################

# if you want to print emoji go to this url & copy th code replyce + with 000  https://unicode.org/emoji/charts/full-emoji-list.html

print("\U0001F618")

print("\U0001F602")


#############################################################
####################### now we look claculation #############
#############################################################

### operter is below 
## + :  to add 
## - :  substarction (minus)
## * :  multipul
## / :  float
## // : intiger dived 
## % : module 
## ** : exponte (power)


print(3+3)

print(12-4)

print(12 * 4)

print (12/4) # floating output 

print(12//4)  # intiger output 

print(12% 4)

print(12**4)  # to get power of number 

print(2** 0.5) # in this we got long digit output to fix this we user round 

print (round(2** 0.5, 3 ) ) # we user round(2** 0.5, Number of digit you want in our case we take 2

#############################################################
####################### now we look vireable ################
#############################################################

F_name = "amardip "

M_nub =20

L_name = "sakapal "   # this is my vireable

Full_name =  F_name + " " + L_name

print ( Full_name + str (M_nub))

print(F_name * 3 ) # this will print string 3 time 


#############################################################
#################### now we look user input  ################
#############################################################

#when we take a input from user it is alwsay string 
# if you want to use user input as int you have convert it int(vireableName )

name = input("type your name ") # we get input & save this in vireable name 

age = input("what's your age ")

print("wellcome " + name + ' \n great your now '+  age  ) 

u_after10 = int(age) + 10     # in this we can cover sting to int & add number 

print("you after ten " + str(u_after10))  # here we take 
################################################################################
################################################################################


age_of_expri = int(input("what's your age ")) # her we take user input in int 

u_after1 = (age_of_expri) + 10     # in this we can cover sting to int & add number 

print("cool if you fight 2020 will have good day when you " + str(u_after1))  # here we take int & conver it  string 








