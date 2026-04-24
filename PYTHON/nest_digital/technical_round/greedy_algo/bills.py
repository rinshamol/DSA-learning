bills = [5,5,5,10,20,20]
def lemonade_change():
    five = 0
    ten = 0
    

    for b in bills:
        
        if b == 5 :
            five += 1
        elif b == 10:
            if five: 
                five -= 1
                ten  += 1
            else:
                return False    
        else:
            if five and ten :
                five -= 1
                ten -= 1
            elif five >= 3 :
                five -= 3
            else :
                return False
    return True
print(lemonade_change())