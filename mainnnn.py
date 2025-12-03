import random


shape = input("shape")
szam = int(input("kockaszam: "))

if shape=="kocka":
    for i in range(1):
        print(" " + "____" * (szam-round(szam/5-0.2)))
        for j in range(szam):
            print("|" + "    " * (szam-round(szam/5-0.2)) + "|")
        print("|" + "____" * (szam-round(szam/5-0.2))+ "|")
if shape=="pyram":
    for i in range(szam):
        print(" "*(szam-i)+"/"+" "*(i*2)+"\\ "+" "*szam)
    print("TT"*(i-(round(i/6))) + "T"*i)

if shape=="gem":
    tag=0
    for i in range(szam):
        print(" "*(szam-i)+"/"+" "*(i*2)+"\\ "+" "*szam)
        tag+=1
    for i in range(szam+1):
        if tag>0:
            print(" "*i+ " " + "\\"+" "*((tag*2)-2)+"/")
            tag-=1
        else:
            print()
if shape=="black":
    kartya= random.randint(1,11)
    sajkartya = random.randint(1, 11)
    dealer =0
    sajszam=0
    dealer+=kartya
    sajszam+=sajkartya
    print(f"{dealer, sajszam}")
    fact=True
    while fact:
        randnumd=random.randint(1,11)
        randnum=random.randint(1,11)
        igennem=input("hit? [i/n]")
        if igennem=="i":
            print(f"húzás :  {randnum}")
            if randnum==11 and (sajszam + randnum)>21:
                sajszam+=1
            else:
                sajszam+=randnum
            print("now your deck:  ", sajszam)
        if sajszam>=22:
            print("you lost" , sajszam)
            fact=False

        if dealer<=16:
            dealer+=randnumd
        if dealer>=22:
            print("you won enemy has " ,dealer)
            fact=False
        if dealer==21:
            print("enemy has 21 you lost ")
        if fact:
            print("the enemy has ",dealer)
if shape=="3d":
    tav=0
    for i in range(szam):
        print("  "*(szam-tav) +"/"+"  "*tav+"|"+"  "*tav+"\\")
        tav+=1
if shape=="okt161":
    i=0
    szov = []
    while i<=150:

        if i%2==0:
            szov.append(i)
        i+=1
    print(szov)
if shape=="okt162":
    szam=1
    rekord =[]
    kapcs=5
    while not(szam%10==0):
        szam=int(input("10 es szam"))
        rekord.append(szam)
        if szam<0 and szam%10==0:
            print("ez a szam minus biztos hogy használod?")
            mekeres=input("[ i / n ] ")
            if mekeres =="i":
                print("vegsőszám", szam, *rekord, "szam:", len(rekord))
                szam=10
            else:
                print("okay")
                szam=(szam-1)

    print("vegsőszám",szam, *rekord, "szam:" ,len(rekord))
if shape=="recept":
    parts=["+","_"," "]
    els=input("els")
    mas = input("mas")
    harm = input("harm")
    cegnev= input("adj cegnevet")
    osszeg =0
    print(parts[0]*22)
    print("tetelegy",parts[2]*(12-len(els)),els)
    print("tetelegy", parts[2] * (12 - len(mas)), mas)
    print("tetelegy", parts[2] * (12 - len(harm)), harm)
    print(parts[0]*22)
    print(parts[2]*round(11-(len(cegnev)/2)),cegnev,parts[2]*round(11-(len(cegnev)/2)))
    osszeg1=int(els)
    osszeg2=int(mas)
    osszeg3=int(harm)
    osszeg=(osszeg1+osszeg2+osszeg3)
    print("összeg", parts[2] * (14 - len(str(osszeg))), osszeg)
































def bigA():
    return [
        "    /\\    ",
        "   /  \\   ",
        "  / /\\ \\  ",
        " / ____ \\ ",
        "/_/    \\_ "
    ]
def bigB():
    return [
        " ____  ",
        "|  _ \\ ",
        "| |_) |",
        "|  _ < ",
        "|______"
    ]
def bigD():
    return [
        "/''''''\\   ",
        "I      I   ",
        "I      I   ",
        "I      I   ",
        "\\______J   "
    ]
def bigL():
    return [
        "I  I     ",
        "I  I     ",
        "I  I     ",
        "I  I___  ",
        "I------I "
    ]

def bigO():
    return [
        " ______   ",
        "/      \\ ",
        "|      |  ",
        "\\______/ ",
        "          "
    ]
def bigv():
    return [
        "I         I"
        " I       I "
        "  I     I  "
        "   I   I   "
        "    I_I    "
    ]





def bigC():
    return [
        "  ____  ",
        " / ___| ",
        "| |     ",
        "| |___  ",
        " \\____|"
    ]

# Add more letters here!

def bigSpace():
    return [
        "  ",
        "  ",
        "  ",
        "  ",
        "  "
    ]




def bigC():
    return [
        "  ____  ",
        " / ___| ",
        "| |     ",
        "| |___  ",
        " \\____| "
    ]



def bigSpace():
    return [
        "  ",
        "  ",
        "  ",
        "  ",
        "  "
    ]


def bigO():
    return [
        "I------I ",
        "I      I ",
        "I      I ",
        "I      I ",
        "I------I "
    ]

def bigV():
    return [
        r"\         I",
        r" \       I ",
        r"  \     I  ",
        r"   \   I   ",
        r"    \_I    "
    ]

def bigSpace():
    return [
        "  ",
        "  ",
        "  ",
        "  ",
        "  "
    ]

def bigE():
    return [
        "/'''''''''I",
        "I  L'''''' ",
        "I  ====I   ",
        "I  L______ ",
        "I_________I"
    ]
def bigF():
    return [
        "/'''''''''I",
        "I  L'''''' ",
        "I  ====I   ",
        "I  I       ",
        "I__I       "
    ]
def bigN():
    return [
        "/  I      I I",
        "I  I  I   I I",
        "I  I   I  I I",
        "I  I    I   I",
        "I__I     I__I"
    ]
def bigQ():
    return [
        " /''''''\\ ",
        "I        I",
        "I    ''  I",
        "I      I I",
        " \\______/J"
    ]
def bigR():
    return [
        "/  ---   ",
        "I I    J ",
        "I I  --  ",
        "I I  /   ",
        "I_I    / "
    ]
def bigI():
    return [
        "xxx ",
        " x  ",
        " x  ",
        " x  ",
        "xxx "
    ]

def bigG():
    return [
        " /''''''\\  ",
        "I          ",
        "I   ===I   ",
        "I      I   ",
        " \\_____J   "
    ]
def bigH():
    return [
        "I     I   ",
        "I     I   ",
        "I=====I   ",
        "I     I   ",
        "I     I   "
    ]
def bigJ():
    return [
        "    '''I  ",
        "      I   ",
        "      I   ",
        "I     I   ",
        " \\____/   "
    ]

def bigK():
    return [
        "I   /''   ",
        "I  /      ",
        "I=/       ",
        "I  \\      ",
        "I   \\__   "
    ]
def bigM():
    return [
        "I\\    /I  ",
        "I \\  / I  ",
        "I  \\/  I  ",
        "I       I ",
        "I       I "
    ]
def bigN():
    return [
        "/  I      I I",
        "I  I  I   I I",
        "I  I   I  I I",
        "I  I    I   I",
        "I__I     I__I"
    ]
def bigP():
    return [
        "/''''''\\   ",
        "I      I   ",
        "I=====/    ",
        "I          ",
        "I          "
    ]
def bigS():
    return [
        " /''''''\\  ",
        "I          ",
        " \\''''\\    ",
        "       I   ",
        " \\_____/   "
    ]
def bigT():
    return [
        "''''''''I ",
        "    x     ",
        "    x     ",
        "    x     ",
        "    x     "
    ]
def bigW():
    return [
        "I      I        I",
        "I      I        I",
        "I   /\\ I /\\   I  ",
        "I  /  \\I/  \\  I  ",
        " \\_/       \\_/   "
    ]
def bigX():
    return [
        "\\       /",
        " \\     / ",
        "   \\ /   ",
        "  /   \\  ",
        " /     \\ "
    ]
def bigY():
    return [
        "I     I ",
        " I   I  ",
        "  I I   ",
        "   I    ",
        "   I    "
    ]
def bigZ():
    return [
        "''''''''I",
        "     /'  ",
        "   /'    ",
        " /'      ",
        "I________"
    ]

def bigU():
    return [
        "I       I ",
        "I       I ",
        "I       I ",
        "I       I ",
        " \\_____/  "
    ]

ascii_map = {
    "A": bigA,
    "B": bigB,
    "C": bigC,
    "D": bigD,
    "E": bigE,
    "F": bigF,
    "G": bigG,
    "H": bigH,
    "I": bigI,
    "J": bigJ,
    "K": bigK,
    "L": bigL,
    "M": bigM,
    "N": bigN,
    "O": bigO,
    "P": bigP,
    "Q": bigQ,
    "R": bigR,
    "S": bigS,
    "T": bigT,
    "U": bigU,
    "V": bigV,
    "W": bigW,
    "X": bigX,
    "Y": bigY,
    "Z": bigZ,
    " ": bigSpace
}

def print_big(text):
    text = text.upper()
    lines = ["" for _ in range(5)]

    for char in text:
        big_letter = ascii_map.get(char, bigSpace)()
        lines = [line + letter_line + "  " for line, letter_line in zip(lines, big_letter)]

    print("\n".join(lines))

if shape=="big":
    text = input("Enter text: ").upper()
    print_big(text)
if shape!="smile" and shape!="kocka" and shape!="black" and shape!="big" and shape!="pyram" and shape!="gem":
    print("black, big, pyram, kocka ,gem")