import ascii_art
import textwrap
import os
import fugue_map
# fugue_map.Fugue_Map()


def title_screen():

    print("#############################")
    print("#          FUGUE            #")
    print("#############################")
    print(ascii_art.castle.center(30))
    print("        1 NEW GAME           ")
    print("        2 CONTINUE           ")
    print("        3 SETTINGS           ")
    print("        4 CREDITS            \n")

    choice = input("What would you like to do?: \n")

    # Choices:

    if choice == "1" or choice == "new game".lower():
        # os.system('cls')
        my_map = fugue_map.Fugue_Map()
        my_map.prep_data()
        new_room = my_map.desert_camp
        new_room.in_current_room = True
        os.system('cls')
        print("###############################################################################################")
        print("\n".join(textwrap.wrap(new_room.long_description, width=100, replace_whitespace=False)))
        print("###############################################################################################")
        print(new_room.ascii_art.center(30) + "\n")
        print("###############################################################################################")
        current_room = new_room

        return


#
    elif choice == "2" or choice.lower == "continue":
        #  Load Game
        pass


#
    elif choice == "3" or choice.lower() == "credits":
        os.system('cls')
        print("###############################################################################################")
        print("                                        FUGUE                                                 ")
        print("                                         BY                                                   \n")
        print("                                    Hayley Leavitt                                            ")
        print("                                     John Koenig                                              ")
        print("                                     Luke Babcock                                             \n")
        print("###############################################################################################\n")
        input("Press any key to go back")
        title_screen()


#
    elif choice == "4" or choice.lower() == "exit":
        sys.exit("Thank you for playing!")


#
    else:
        print("Invalid selection. Try again: ")


