age = int(input("Enter your age : "))

if age <=0 :  # this to check age is leass than 0 
    print("you can't see this movie ") 
elif 0<age<=3:                      #this is to check greater tahn 0 & leass than 3 
    print("ticket price 100")     
elif 4<age<=10 :
    print("ticket price 150")  
elif 11<age<=60 :
    print("ticket price 250")
else:
    print("your price is 200")                    

# now we look in with if 

name = "amardip"

if 'Z' in name :            # this is use to check

    print("you have a in name")

else:

    print ("not foun Z ")


# we can check our condition is true or not 

name="test"
var=""

if name:
    print("this condition is ture & not empty ")
else:
    print("this is not tru name empty ")    
if var:
      print("this is not true VAR empty ")       