strt , end = input("please neter starting & ending number for power  use , : ").split(",")
number = list(range(int(strt), int(end)))

def print_power(l):
    negative = []
    for i in l :
        negative.append( i* i)
    return negative    


print(print_power(number))

