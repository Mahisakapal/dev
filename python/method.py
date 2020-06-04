############################################################
############ now we look strip methoad         #############
#############################################################

# basicale how to remove space from string 

namw= "          amardip           "
dot="................."

# basicale how to remove space from string 

name= "       ama      rdip     "
dot="................."

print(namw + dot)  # noemal 

print(namw.lstrip() + dot) # remove leftside sapce 

print(namw.rstrip ()+ dot) # remove right space 

print(namw.strip ()+ dot)  # remove both dode sapce 

print(name.replace("  ", ""))  ## this ccase we replce  "sapce " with ""(nothing) this find & replce like excel

# in evry method we take virable.nameOfMathoad(parmeter)

#########################################################
#this is the replace method #############################
#########################################################

var= "this is the demo of replcement is check all"

print(var)

print(var.replace(" ", "_"))

print(var.replace(" is"," was", ))

print(var.replace(" is"," was", 1 )) # whe you add number is will replace only one 

print(var.find("the")) #this is use to find the posintion of of your input(the)

print(var.find("is" ,7)) # here we defind from where to start 

var_pos1=var.find(" is")  # we fined the postion of is & save it in var

print(var.find(" is", var_pos1 + 1)) # now we shearch is from postion of var

#########################################################
######### this is the center ############################
#########################################################


var_name="mahi"

print (var_name.center(8, "*") )# here we add 4 *. our var lenaht is so we set =8 

#################### now realtime exmple ################

var_user_input, star = input("please enter input , nuberof count you want to print  ").split(",")   # now ew tacker input from user

vui = var_user_input.strip()  # here we remove the sapce 

print( vui.center( len(vui)+int (star) , "*") ) # & get lenth of var & add 8 in center metohd 

