#Heldur utan um stöðu player

#Prentar möguleika

def prints_options():
    print('You can travel' + str())


#Taka input um hvað user vill gera



print('Lol')

direction = input("where do you want to go ?")

x = 1
y = 1

def direction():
    take_direction = input('Direction: ')
    return take_direction

def movement(take_direction):
    while True:
        if take_direction == 'n' or take_direction == 'N':
            y += 1
        elif take_direction == 'e' or take_direction == 'E':
            x += 1
        elif take_direction == 's' or take_direction == 'S':
            y -= 1
        elif take_direction == 'w' or take_direction == 'W':
            x -= 1
        else:
            print('“Not a valid direction!')
            direction()

