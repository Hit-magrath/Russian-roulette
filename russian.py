import random
print (''' WELCOME TO MY RUSAIN ROULLETE''')
# *************************making the empty berral*************************
berral = [ "","","","","",""]
#**********************************************************

# *****************randomise the bullet placement**********************
num = random.choice(range(0,6))
berral[num] = "b"
#*****************************************************
# **************************************shooting mechaninc*****************
alive = True
other = 0
player = 2
while alive:
    act = input(''' what do yo wish to do?
     you can spin(s) or shoot(f) or both... ''')
    if player > 2 :
        player = 1
    if act.lower() == 'f':
        if other > 6:
            other = 0
        if berral[other] == "":
            print("you survived...switch to player" + " " + f'{player}')
            other+=1
            player+=1
        else :
            print("BAAM!!")
            alive = False
    if act.lower()=="s":
        print("play agian")
        other = random.choice(range(0,6))