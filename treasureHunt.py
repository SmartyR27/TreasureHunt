# PROJECT NAME - TREASURE HUNT GAME
# MAJOR PROJECT

# FUNCTION WITH CHARACTERISTIC OF SNAKE ROOM
def snake_room():
    #SOME PROMPT
    print("\nThere is a snake here.\nBehind the snake is another door.\nThe snake is having eggs!!")
    print("What will you do (1 or 2) :")
    print("1. Take the eggs.")
    print("2. Taunt the snake.")
    s_r = input()
    if s_r == "1":
        print("You want eggs not the treasure !! Thats why the snake killed you.")
        game_over()

    else:
        if s_r == "2":
            print("\nFoxy!!")
            treasure_room()

# FUNCTION WITH CHARACTERISTIC OF MONSTER ROOM
def monster_room():
    print("\nNow you entered the room of the monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2) :")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")
    m_r = input()

    if m_r == "1":
        print("Foxy!!")
        treasure_room()

    else:
        if m_r=="2":
            print("The monster was hungry, he/it ate you.")
            game_over()

# FUNCTION WITH CHARACTERISTIC OF TREASURE ROOM
def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is door too!")
    print("What would you do? (1 or 2) :")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")
    t_r = input()

    if t_r == "1":
        print("\nCongratulation!!")
        print("\nYou deserve this success...")
        print("Thanks for playing..")
        lets_play_again()

    else:
        if t_r=="2":
            print("Shitt!!!")
            print("You lose the game...")
            print("Thanks for playing...")
            lets_play_again()

# FUNCTION  FOR END..
def game_over():
    print("Game Over!")
    lets_play_again()

# FUNCITON FOR LOOP
def lets_play_again():
    print("\nDo you want to play again? (y or n) :")

    answer = input(">").lower()

    if answer == "y":
        start()

    else:
        if answer == "n":
            exit()

#Main function
def start():
   print("\nYou are standing in a dark room")
   inp = input("There is a door to your left and right, which one do you take ? (l or r) :")

   if inp == "l" or inp.lower()=="l":
       snake_room()

   elif inp == "r" or inp.lower()=="r":
       monster_room()

#CALL FUNTION..
start()