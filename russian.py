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
while alive:
    act = input('''what do yo wish to do?
    you can spin or shoot or both... ''')
    if act.lower() == 'a':
        if other >= 6:
            other = 0
        if berral[other] == "":
            print(True)
            other+=1
        else :
            print("BAAM!!")
            alive = False
    if act.lower()=="s":
        other = random.choice(range(0,6))