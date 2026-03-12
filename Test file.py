import time
import random
import os

inventory = []
puzzle_pieces = 0
phone_unlocked = False
balance_done = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.015)
    print()

hospital_art = r"""
----------------------------------------------------------------------------------------






-----------------------------------------------------------------------------------------
"""

room_art = r"""
+--------------------------+
|        KÓRTEREM          |
|                          |
|    [ÁGY]        [ÁGY]    |
                |
+--------------------------+|                          |
|         ____             |
|        |____|  asztal    |
|          
"""

#Item art

phone_art = r"""
   ___________
  |  _______  |
  | |       | |
  | |       | |
  | |_______| |
  | 1 2 3 4   |
  |___________|
"""

scale_art = r"""
        _______
       /       \
      /         \
     /___________\
        |     |
      __|_____|__
     |           |
     |   MÉRLEG  |
     |___________|
"""

bone_art = r"""
     __
 ___/  \___
|          |
 \__    __/
    |  |
    |__|
"""

#item art

#room art

dark_hall = r"""
#############################################
#                                           #
#     O                                     #
#\   \|/                                    #
# \  / \                                    #
#  \                                        #
#                                           #
#############################################
"""
dark_hall2 = r"""
#############################################
#                                           #
#              O                            #
#\            \|/                           #
# \           / \                           #
#  \                                        #
#                                           #
#############################################
"""
dark_hall3 = r"""
#############################################
#                                           #
#                                 O         #
#\                               \|/        #
# \                              / \        #
#  \                                        #
#                                           #
#############################################
"""

#room art


# No nyulka piszka

def intro():
    clear()
    print(hospital_art)
    slow("Éjjeli műszak...")
    slow("Nem emlékszel semmire.")
    slow("Egy elhagyott kórházban ébredsz.")
    slow("Ki kell jutnod a ZÁRT OSZTÁLYRÓL.\n")

def show_inventory():
    print("\nInventory:", inventory)

def search_room():
    items = ["csont", "fecskendő", "gyertya"]
    item = random.choice(items)

    print(room_art)

    if item not in inventory:
        slow(f"Találtál egy tárgyat: {item}")
        inventory.append(item)
    else:
        slow("Most nem találtál semmit.")

def dark_corridor_event():
    print(dark_hall)

    if "gyertya" not in inventory:
        slow("Túl sötét... Kell valami fény.")
        return

    slow("A gyertya halványan világít...")
    slow("Találsz egy puzzle darabot.")
    global puzzle_pieces
    puzzle_pieces += 1

def phone_puzzle():
    global phone_unlocked

    print(phone_art)

    if phone_unlocked:
        slow("A telefon már fel van oldva.")
        return

    slow("A telefon zárolva van.")
    code = "4312"

    guess = input("Add meg a 4 jegyű kódot: ")

    if guess == code:
        slow("Telefon feloldva!")
        phone_unlocked = True
    else:
        slow("Rossz kód.")

def balance_puzzle():
    global balance_done

    print(scale_art)

    if balance_done:
        slow("A mérleg már meg van oldva.")
        return

    if "csont" not in inventory:
        slow("Valami hiányzik a mérleghez...")
        return

    print(bone_art)

    choice = input("Ráteszed a csontot a mérlegre? (i/n) ")

    if choice == "i":
        slow("A mérleg kiegyenlítődik...")
        slow("Egy ajtó kinyílik!")
        balance_done = True
    else:
        slow("Otthagyod.")

def ending():
    slow("\nElérted a kijáratot...")

    if phone_unlocked and balance_done:
        slow("Megoldottad az összes rejtvényt.")
        slow("SIKERÜLT MEGSZÖKNÖD.")
        slow("JÓ BEFEJEZÉS")
        return True

    if "fecskendő" in inventory and phone_unlocked:
        slow("Egy titkos ajtót találsz.")
        slow("TITKOS BEFEJEZÉS")
        return True

    slow("Az ajtó bezárul mögötted.")
    slow("ROSSZ BEFEJEZÉS")
    return True

def game_loop():
    intro()

    while True:
        print("""
1 - Szoba átkutatása
2 - Sötét folyosó
3 - Telefon
4 - Mérleg puzzle
5 - Inventory
6 - Kijárat
""")

        choice = input("> ")

        clear()

        if choice == "1":
            search_room()

        elif choice == "2":
            dark_corridor_event()

        elif choice == "3":
            phone_puzzle()

        elif choice == "4":
            balance_puzzle()

        elif choice == "5":
            show_inventory()

        elif choice == "6":
            if ending():
                break

        else:
            slow("Ismeretlen parancs.")

game_loop()