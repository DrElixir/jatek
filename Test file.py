# ZÁRT OSZTÁLY — 15 PERCES TERMINÁLOS HORROR JÁTÉK

Ez egy teljesen újraírt, hosszabb, történetközpontú verzió.
A játék kb. 10–15 perces gameplayre van felépítve:

* több helyszín
* több story event
* memory rendszer
* chase sequence
* puzzle progression
* több ending
* jobb pacing
* stabilabb kód
* nincs softlock
* nincs unreachable ending

A játék Python terminálban fut.

## Főbb újítások

### Story

A játékos fokozatosan jön rá:

* ki ő
* mi történt a kórházban
* mit jelent a „Projekt Tisztítás”
* hogy valóban orvos volt-e

### Új helyszínek

* Sötét folyosó
* Kazánház
* Tükörszoba
* Labor
* Rejtett lift

### Új mechanikák

* menekülős jelenet
* random események
* progresszív emlékek
* inventory progression
* több ending

### Endingek

* Jó ending
* Rossz ending
* Titkos ending

## Fontos javítások

* minden változó inicializálva van
* nincs végtelen item repeat
* nincs softlock
* nincs crash
* Windows/Linux kompatibilis
* input hibák javítva
* stabilabb inventory rendszer

## Futtatás

```bash
python game.py
```

## Ajánlott futtatás

Windows Terminal vagy VS Code terminal.

## Extra ötletek későbbre

* sanity rendszer
* save/load
* zene és hangok
* ASCII jumpscare
* procedurális folyosók
* több entity
* boss encounter
* timed escape sequence

## A játék struktúrája

```text
INTRO
 ↓
SZOBA
 ↓
FOLYOSÓ
 ↓
KÓD DARABOK
 ↓
TELEFON
 ↓
MÉRLEG PUZZLE
 ↓
KAZÁNHÁZ
 ↓
TÜKÖRSZOBA
 ↓
ENDING
```

# TELJES KÓD

```python
import os
import time
import random
import sys

# =====================================================
# ALAP VÁLTOZÓK
# =====================================================

inventory = []
kod_darabok = []

telefon_feloldva = False
merleg_megoldva = False
labor_elerheto = False

memories_found = 0

helyes_kod = [str(x) for x in random.sample(range(1, 10), 4)]

# =====================================================
# SEGÉD FÜGGVÉNYEK
# =====================================================


def clear():
    os.system("cls" if os.name == "nt" else "clear")



def slow(text, speed=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()



def think(text):
    slow(f"[...] {text}", 0.03)



def pause(sec=1):
    time.sleep(sec)


# =====================================================
# ASCII ANIMÁCIÓ
# =====================================================

frames = [
r"""
#################################
#                               #
#    O                          #
#   /|\                         #
#   / \                         #
#                               #
#################################
""",

r"""
#################################
#                               #
#             O                 #
#            /|\                #
#            / \                #
#                               #
#################################
""",

r"""
#################################
#                               #
#                     O         #
#                    /|\        #
#                    / \        #
#                               #
#################################
"""
]

# =====================================================
# STORY EMLÉKEK
# =====================================================

memories = [
    "Fehér falak. Valaki sikít.",
    "Egy hang: 'Adja be az injekciót!'.",
    "Vér folyik végig a kesztyűdön.",
    "Egy beteg rád néz: 'Kérem doktor úr...'.",
    "Egy monitor villog: PROJEKT TISZTÍTÁS.",
    "A neved egy aktán: DR. VARGA ÁDÁM.",
    "Valaki bezárja rád az ajtót.",
    "Egy hang a sötétben: 'Nem emlékezhet.'"
]



def memory_event():
    global memories_found

    if memories_found < len(memories):
        slow("
[EMLÉK FELVILLAN]", 0.03)
        slow(memories[memories_found], 0.03)
        memories_found += 1


# =====================================================
# INTRO
# =====================================================


def intro():
    clear()

    slow("ZÁRT OSZTÁLY")
    pause(1)

    slow("Éjjeli műszak...")
    pause(1)

    slow("Valami csöpög a sötétben.")
    pause(1)

    slow("Lassan kinyitod a szemed.")
    pause(1)

    think("Hol vagyok?")
    think("Mi történt?")

    slow("Egy hideg kórteremben fekszel.")
    slow("Az ajtó résnyire nyitva van.")


# =====================================================
# INVENTORY
# =====================================================


def show_inventory():
    slow("===== INVENTORY =====")

    if not inventory:
        slow("Nincs nálad semmi.")
    else:
        for item in inventory:
            slow(f"- {item}")

    if kod_darabok:
        slow("
Kóddarabok:")
        slow(" ".join(kod_darabok))


# =====================================================
# SZOBA ÁTKUTATÁS
# =====================================================


def szoba_kutatas():

    lehetseges = [
        "gyertya",
        "rozsdás kulcs",
        "fecskendő",
        "csont",
        "betegkártya"
    ]

    talalhato = [x for x in lehetseges if x not in inventory]

    slow("Körbenézel a szobában...")
    pause(1)

    if not talalhato:
        slow("Már mindent átkutattál.")
        return

    targy = random.choice(talalhato)
    inventory.append(targy)

    if targy == "gyertya":
        slow("Találsz egy gyertyát.")
        think("Most már látni fogok.")

    elif targy == "rozsdás kulcs":
        slow("Egy rozsdás kulcs hever az ágy alatt.")

    elif targy == "fecskendő":
        slow("Egy véres fecskendő.")
        think("Frissnek tűnik...")

    elif targy == "csont":
        slow("Valami roppan a lábad alatt.")
        slow("Egy emberi csont.")

    elif targy == "betegkártya":
        slow("Találsz egy betegkartont.")
        slow("Rajta ez áll:")
        slow("'12-es alany'")

    if random.randint(1, 2) == 1:
        memory_event()


# =====================================================
# CHASE SEQUENCE
# =====================================================


def enemy_chase():

    slow("Valamit hallasz...")
    pause(1)

    slow("Lépések.")
    pause(1)

    slow("FUTNOD KELL!", 0.05)

    for i in range(8):
        clear()
        print(frames[i % 3])
        time.sleep(0.15)

    slow('"MEGTALÁLTALAK"')

    choices = ["balra", "jobbra"]
    correct = random.choice(choices)

    guess = input("Merre futsz? (balra/jobbra): ").strip().lower()

    if guess == correct:
        slow("Egy ajtót rád csapsz.")
        slow("Megmenekültél.")
    else:
        bad_ending()


# =====================================================
# FOLYOSÓ
# =====================================================


def sotet_folyoso():

    if "gyertya" not in inventory:
        slow("Semmit nem látsz.")
        think("Kell valami fény.")
        return

    slow("Belépsz a sötét folyosóra...")
    pause(1)

    slow("A falakon vérfoltok vannak.")
    slow("Valahol egy ajtó csapódik.")

    if len(kod_darabok) < 4:

        remaining = [x for x in helyes_kod if x not in kod_darabok]

        if remaining:
            piece = random.choice(remaining)
            kod_darabok.append(piece)

            slow(f"Egy szám van a falra karcolva: {piece}")
            think("Talán egy kód része...")

            memory_event()

    else:
        slow("Ugyanazokat a jeleket látod mindenhol.")

    if random.randint(1, 5) == 1:
        enemy_chase()


# =====================================================
# TELEFON
# =====================================================


def telefon():
    global telefon_feloldva

    slow("Egy régi telefon áll az asztalon.")

    if telefon_feloldva:
        slow("Már fel van oldva.")
        return

    if len(kod_darabok) < 4:
        slow("Hiányzik pár szám.")
        return

    slow("A kijelző kódot kér.")

    guess = input("Kód: ").strip()

    correct_code = "".join(helyes_kod)

    if guess == correct_code:

        telefon_feloldva = True

        slow("A képernyő felvillan.")
        slow("Sikerült feloldani.")

        slow("
Hangfelvétel indul:")
        pause(1)

        slow('"12-es alany instabil."')
        slow('"Memóriatörlés sikertelen."')
        slow('"Az orvos eltűnt."')

        if "kazetta" not in inventory:
            inventory.append("kazetta")
            slow("Kaptál: kazetta")

        memory_event()

    else:
        slow("HIBÁS KÓD")


# =====================================================
# MÉRLEG PUZZLE
# =====================================================


def merleg():
    global merleg_megoldva
    global labor_elerheto

    slow("Egy régi mérleg áll előtted.")

    if merleg_megoldva:
        slow("Már beállítottad.")
        return

    if "csont" in inventory and "fecskendő" in inventory:

        slow("Ráhelyezed a tárgyakat...")
        pause(2)

        slow("A mérleg lassan kiegyenlítődik.")
        slow("Egy rejtett ajtó nyílik ki.")

        merleg_megoldva = True
        labor_elerheto = True

        if "labor kulcs" not in inventory:
            inventory.append("labor kulcs")

        memory_event()

    else:
        slow("Valami hiányzik.")


# =====================================================
# LABOR
# =====================================================


def labor():

    if not labor_elerheto:
        slow("Nem találsz oda vezető utat.")
        return

    slow("Belépsz a laborba.")
    pause(1)

    slow("A monitorok még működnek.")
    slow("Mindenhol akták és vér.")

    if "feljegyzés" not in inventory:

        inventory.append("feljegyzés")

        slow("Találsz egy vérfoltos dokumentumot:")
        pause(1)

        slow('"Dr. Varga elvesztette az eszét."')
        slow('"A betegek agresszívvé váltak."')
        slow('"Az alanyok nem emlékezhetnek."')

        memory_event()

    if random.randint(1, 3) == 1:
        enemy_chase()


# =====================================================
# TÜKÖR SZOBA
# =====================================================


def tukor_szoba():

    slow("Belépsz egy régi mosdóba.")
    pause(1)

    slow("A tükör repedezett.")

    if memories_found >= 4:
        slow("A tükörben egy véres köpenyes orvost látsz.")
        pause(1)

        slow("És ugyanaz az arc néz vissza rád.")

        memory_event()

    else:
        slow("Csak a saját remegő alakodat látod.")


# =====================================================
# ENDINGEK
# =====================================================


def good_ending():

    clear()

    slow("Az ajtó lassan kinyílik.")
    pause(1)

    slow("Friss levegő csap meg.")
    slow("Kilépsz a kórházból.")

    pause(2)

    slow("De ekkor minden visszatér.")
    slow("Az emlékek.")

    pause(2)

    slow("Te vezetted a kísérleteket.")
    slow("Minden beteg miattad halt meg.")

    pause(2)

    slow('"DR. VARGA! ÁLLJON MEG!"')

    slow("
JÓ BEFEJEZÉS")

    sys.exit()



def bad_ending():

    clear()

    slow("Lépések közelednek a sötétből.")
    pause(1)

    slow('"Nem mehetsz el..."')

    pause(2)

    slow("Valami megragad hátulról.")
    slow("A sötétség elnyel.")

    slow("
ROSSZ BEFEJEZÉS")

    sys.exit()



def secret_ending():

    clear()

    slow("A labor egyik fala kinyílik.")
    pause(1)

    slow("Egy rejtett lift ereszkedik lefelé.")
    pause(3)

    slow("Egy hatalmas föld alatti részlegbe érsz.")

    pause(2)

    slow("Monitorok százai villognak.")
    slow("Mindegyiken TE vagy látható.")

    pause(2)

    slow('"12-es alany stabil."')
    slow('"Memória manipuláció sikeres."')

    pause(2)

    slow("Rájössz az igazságra.")
    slow("Nem orvos vagy.")
    slow("Te vagy a beteg.")

    slow("
TITKOS BEFEJEZÉS")

    sys.exit()


# =====================================================
# KIJÁRAT
# =====================================================


def try_exit():

    if telefon_feloldva and merleg_megoldva and "feljegyzés" in inventory:
        good_ending()

    elif "kazetta" in inventory and "rozsdás kulcs" in inventory and memories_found >= 6:
        secret_ending()

    else:
        slow("Az ajtó nem nyílik.")
        think("Még nincs vége.")


# =====================================================
# GAME LOOP
# =====================================================


def game_loop():

    intro()

    while True:

        print("""
===============================
1 - Szoba átkutatása
2 - Sötét folyosó
3 - Telefon
4 - Mérleg
5 - Labor
6 - Tükörszoba
7 - Inventory
8 - Kijárat
===============================
""")

        choice = input("> ").strip()

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
            labor()

        elif choice == "6":
            tukor_szoba()

        elif choice == "7":
            show_inventory()

        elif choice == "8":
            try_exit()

        else:
            slow("Nem értem.")


# =====================================================
# START
# =====================================================


game_loop()
```

## TOVÁBBI FEJLESZTÉS ÖTLETEK

* mentés rendszer
* sanity mechanic
* jumpscare system
* háttérhangok
* több monster
* procedural folyosók
* random endingek
* entity AI
* inventory UI
* combat system
