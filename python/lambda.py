# normly we use this func 

def add (d,j):
    return d + j

# but in lamada we code like 

answer = lambda a, b: a+b  # gnerly we never store it in any variable but for esy way we use this 

print(answer(4, 6,))    


# normly we use this func 
def is_evn(l):
    return l%2 == 0 
print(is_evn(5))    

# but in lamada we code like 
anser1 = lambda l : l%2 == 0

print(anser1(6))

# normly we use this func 
def func(i):
    if len(i) > 4:    # you can do this without returen len(i) >4: no need writ 2 line 
        return True
    return False 
print(func('amrdip')) 

func1 = lambda a : True if len(a) > 4 else False

func2 = lambda a :len(a) > 4    # this also same 

print(func1('amar'))
print(func2('amardip'))