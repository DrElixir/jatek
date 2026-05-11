import time
import random
import os

# ===================== Alap változók =====================

inventory = []
kirako_darabok = []

telefon_feloldva = False
merleg_megoldva = False


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


# ===================== STORY (EMLÉKEK) =====================

def memory_event():
    global memories_found

    memories = [
        "Fehér falak. Kiabálás. Valakit lefognak.",
        "Egy hang: 'Adja be az injekciót.'",
        "A kezedben egy fecskendő.",
        "Egy beteg rád néz: 'Ne tedd...'",
        "Egy név villan: ORVOS"
    ]

    if memories_found < len(memories):
        slow("\n[EMLÉK FELVILLAN]")
        slow(memories[memories_found])
        memories_found += 1


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

    print("Kirakó darabok:", kirako_darabok)


# ===================== Tárgy keresés =====================

def szoba_kutatas():
    lehetseges_targyak = ["csont", "gyertya", "fecskendő", "kulcs"]
    talalt_targy = random.choice(lehetseges_targyak)

    slow("Körbenézel a szobában...")

    if talalt_targy in inventory:
        slow("Nem találsz semmi újat.")
        return

    inventory.append(talalt_targy)

    if talalt_targy == "csont":
        slow("Valami roppan a lábad alatt.")
        slow("Egy csont.")
        think("Ez nem jó jel...")
    elif talalt_targy == "gyertya":
        slow("Találsz egy gyertyát.")
        think("Legalább látni fogok.")
    elif talalt_targy == "fecskendő":
        slow("Egy használt fecskendő.")
        think("Ki használta ezt...?")
    elif talalt_targy == "kulcs":
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

    slow('"TE VOLTÁL AZ!"')

    if random.randint(1, 5) == 1:
        clear()
        os.system('color 4')
        slow("Elkaptak...")
        bad_ending()
    else:
        slow("Sikerült elmenekülni.")


# ===================== Folyosó =====================

def sotet_folyoso():
    slow("Belépsz a sötét folyosóra...")

    if "gyertya" not in inventory:
        slow("Semmit nem látsz.")
        think("Kell valami fény.")
        return

    slow("A gyertya fénye remeg a falakon.")

    piece = random.randint(1, 4)

    if piece not in kirako_darabok:
        kirako_darabok.append(piece)
        slow(f"Egy szám van a falra karcolva: {piece}")
        think("Ez talán egy kód része...")
        memory_event()
    else:
        slow("Csak ugyanazok a jelek mindenhol.")

    # random chase
    if random.randint(1, 3) == 1:
        enemy_chase()


# ===================== Telefon =====================

def telefon():
    global telefon_feloldva

    slow("Egy régi telefont találsz.")

    if telefon_feloldva:
        slow("Már fel van oldva.")
        return

    if len(kirako_darabok) < 4:
        slow("Hiányzik pár szám...")
        return

    correct_code = "".join(map(str, sorted(kirako_darabok)))

    guess = input("Kód: ")

    if guess == correct_code:
        slow("A képernyő felvillan...")
        slow("Sikerült feloldani.")
        telefon_feloldva = True
        inventory.append("kórház_kód")

        slow("\nEgy jegyzet jelenik meg:")
        slow('"Projekt: TISZTÍTÁS"')
        slow('"Alanyok: 12 fő"')
        slow('"Eredmény: instabil"')
        slow('"Felelős: TE"')
        think("Ez... én voltam?")
    else:
        slow("Nem történik semmi.")


# ===================== Mérleg puzzlr =====================

def merleg():
    global merleg_megoldva

    slow("Egy régi mérleg áll előtted.")

    if merleg_megoldva:
        slow("Már beállítottad.")
        return

    if "csont" in inventory and "fecskendő" in inventory:
        slow("Ráhelyezed a tárgyakat...")
        time.sleep(1)
        slow("A mérleg lassan kiegyenlítődik.")
        merleg_megoldva = True
    else:
        slow("Valami hiányzik.")


# ===================== Endingek =====================

def good_ending():
    os.system('color 2')
    slow("Az ajtó lassan kinyílik.")
    slow("Friss levegő csap meg.")
    slow("Kijutsz...")

    slow("És most már emlékszel.")
    slow("Mindenre.")

    slow("JÓ BEFEJEZÉS")
    exit()


def bad_ending():
    os.system('color 4')
    slow("Az ajtó nem nyílik.")
    slow("Valami közeledik a sötétből...")
    slow('"Nem mehetsz el..."')
    slow("MEGHALTÁL")
    exit()


def secret_ending():
    os.system('color 6')
    slow("Találsz egy rejtett ajtót.")
    slow("Egy szobába jutsz tele monitorokkal.")
    slow("Kamerák mindenhol.")

    slow("Ez az egész... egy kísérlet volt.")
    slow("És még mindig tart.")

    slow("TITKOS BEFEJEZÉS")
    exit()


# ===================== Kijárat =====================

def try_exit():
    if telefon_feloldva and merleg_megoldva:
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
            szoba_kutatas()

        elif choice == "2":
            sotet_folyoso()

        elif choice == "3":
            telefon()

        elif choice == "4":
            merleg()

        elif choice == "5":
            show_inventory()

        elif choice == "6":
            try_exit()

        else:
            slow("Nem értem.")


# ===================== INDÍTÁS =====================

game_loop()