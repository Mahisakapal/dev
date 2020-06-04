
#############################################################
####################### we are looking if ################
#############################################################

#don't forget to give space if you got indsecantion error mens you have sapce issue 

age = int(input("enter age  :"))

if age >= 18:

    print("your 18 +")

    #don't forget to give sapce you can use pass if u don't want anything

else:

     # don't forget :                   

    print(" hey your below 18") 
    
    # here also space req

#############################################################
######################    we creating game   ################
#############################################################

user_num = int(input("inter your number "))

win_num = 23

if win_num == user_num :
        
        print("greter  you win ....!!!!")
else:
      if win_num < user_num :

          print("your number is to high")

      else:
              print("your number is to low ")
        
#############################################################
######################    and oprater       ################
#############################################################
 
name= "amar"

age = 26

if name=='amar' and age==25 :  # it is true when both condition are ture 

     print("right answer")
else :
     print("wrong")


if name=='amar' or age==26 :  # it is true when one of  condition is ture 

     print("right answer")
else :
     print("wrong")
