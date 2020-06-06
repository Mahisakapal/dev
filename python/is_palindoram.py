def is_palindrom(wrod):
    revers_word = wrod[:: -1]
    if wrod == revers_word :
        return True
    else:                   #you can remove else & remove sapce 
        False     

user_word = input("enter your name ") 
print(is_palindrom(user_word))       



####################################
def palindrom1(wrod):
    return wrod == wrod[::-1]    # her we just check condition & nver defined if else it python will make esy to use
print(palindrom1(user_word))         