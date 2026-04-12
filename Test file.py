import time
import random
import os

# ===================== Alap változók =====================

inventory = []
puzzle_pieces = []

phone_unlocked = False
balance_solved = False


# ===================== Base függvények =====================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print()


def think(text):
    slow(f"[...] {text}")


# ===================== Folyosó kinézet =====================

dark_frames = [
"""
#################################
#                               #
#        O                      #
#       /|\\                     #
#       / \\                     #
#                               #
#################################
""",
"""
#################################
#                               #
#           O                   #
#          /|\\                  #
#          / \\                  #
#                               #
#################################
""",
"""
#################################
#                               #
#               O               #
#              /|\\              #
#              / \\              #
#                               #
#################################
"""
]


# ===================== Start =====================

def intro():
    clear()
    slow("ZÁRT OSZTÁLY")
    slow("Éjjeli műszak...")
    slow("Nem emlékszel semmire.")
    slow("Egy hideg kórteremben ébredsz.")
    think("Hogy kerültem ide?")


# ===================== Inv =====================

def show_inventory():
    if not inventory:
        slow("Nincs nálad semmi.")
        return

    slow("Nálad van:")
    for item in inventory:
        print("-", item)

    print("Puzzle darabok:", puzzle_pieces)


# ===================== Tárgy keresés =====================

def search_room():
    possible_items = ["csont", "gyertya", "fecskendő", "kulcs"]
    found_item = random.choice(possible_items)

    slow("Körbenézel a szobában...")

    if found_item in inventory:
        slow("Nem találsz semmi újat.")
        return

    inventory.append(found_item)

    if found_item == "csont":
        slow("Valami roppan a lábad alatt.")
        slow("Egy csont.")
        think("Ez nem jó jel...")
    elif found_item == "gyertya":
        slow("Találsz egy gyertyát.")
        think("Legalább látni fogok.")
    elif found_item == "fecskendő":
        slow("Egy használt fecskendő.")
        think("Ki használta ezt...?")
    elif found_item == "kulcs":
        slow("Egy rozsdás kulcs.")
        think("Ez még jól jöhet.")


# ===================== Chasing mechanic =====================

def enemy_chase():
    slow("Valamit hallasz...")
    time.sleep(0.5)
    slow("Lépések.")
    time.sleep(0.5)
    slow("FUTNOD KELL!")

    for i in range(6):
        clear()
        print(dark_frames[i % 3])
        time.sleep(0.2)

    if random.randint(1, 5) == 1:
        clear()
        os.system('color 4')
        slow("Elkaptak...")
        bad_ending()
    else:
        slow("Sikerült elmenekülni.")


# ===================== Folyosó =====================

def dark_corridor():
    slow("Belépsz a sötét folyosóra...")

    if "gyertya" not in inventory:
        slow("Semmit nem látsz.")
        think("Kell valami fény.")
        return

    slow("A gyertya fénye remeg a falakon.")

    piece = random.randint(1, 4)

    if piece not in puzzle_pieces:
        puzzle_pieces.append(piece)
        slow(f"Egy szám van a falra karcolva: {piece}")
        think("Ez talán egy kód része...")
    else:
        slow("Csak ugyanazok a jelek mindenhol.")

    # random chase
    if random.randint(1, 3) == 1:
        enemy_chase()


# ===================== Telefon =====================

def phone():
    global phone_unlocked

    slow("Egy régi telefont találsz.")

    if phone_unlocked:
        slow("Már fel van oldva.")
        return

    if len(puzzle_pieces) < 4:
        slow("Hiányzik pár szám...")
        return

    correct_code = "".join(map(str, sorted(puzzle_pieces)))

    guess = input("Kód: ")

    if guess == correct_code:
        slow("A képernyő felvillan...")
        slow("Sikerült feloldani.")
        phone_unlocked = True
        inventory.append("kórház_kód")
    else:
        slow("Nem történik semmi.")


# ===================== Mérleg puzzlr =====================

def balance():
    global balance_solved

    slow("Egy régi mérleg áll előtted.")

    if balance_solved:
        slow("Már beállítottad.")
        return

    if "csont" in inventory and "fecskendő" in inventory:
        slow("Ráhelyezed a tárgyakat...")
        time.sleep(1)
        slow("A mérleg lassan kiegyenlítődik.")
        balance_solved = True
    else:
        slow("Valami hiányzik.")


# ===================== Endingek =====================

def good_ending():
    os.system('color 2')
    slow("Az ajtó lassan kinyílik.")
    slow("Friss levegő csap meg.")
    slow("Kijutottál.")
    slow("JÓ BEFEJEZÉS")
    exit()


def bad_ending():
    os.system('color 4')
    slow("Az ajtó nem nyílik.")
    slow("Valami közeledik a sötétből...")
    slow("ROSSZ BEFEJEZÉS")
    exit()


def secret_ending():
    os.system('color 6')
    slow("Találsz egy rejtett ajtót.")
    slow("Egy titkos folyosón kiszöksz.")
    slow("TITKOS BEFEJEZÉS")
    exit()


# ===================== Kijárat =====================

def try_exit():
    if phone_unlocked and balance_solved:
        good_ending()

    if "kórház_kód" in inventory and "kulcs" in inventory:
        secret_ending()

    bad_ending()


# ===================== Játék alapja =====================

def game_loop():
    intro()

    while True:
        print("""
1 - Szoba átkutatása
2 - Sötét folyosó
3 - Telefon
4 - Mérleg
5 - Inventory
6 - Kijárat
""")

        choice = input("> ")
        clear()

        if choice == "1":
            search_room()

        elif choice == "2":
            dark_corridor()

        elif choice == "3":
            phone()

        elif choice == "4":
            balance()

        elif choice == "5":
            show_inventory()

        elif choice == "6":
            try_exit()

        else:
            slow("Nem értem.")


# ===================== INDÍTÁS =====================

game_loop()