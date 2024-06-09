import random
import csv


def paraditLogo():
    print("""
  .---------------. 
  |╔╦╗┌─┐┌─┐┌┬┐┌─┐| 
  | ║ ├┤ └─┐ │ └─┐| 
  | ╩ └─┘└─┘ ┴ └─┘| 
  '---------------'
Biežāk lietotās funkcijas darbam ar simbolu virknēm programmēšanas valodā Python.

Testa noteikumi: 10 jautājumi, uz kuriem Jūs varat atbildēt līdz atbilde pareiza. Beigās Jums tiks paziņots, cik jautājumi atbildēti pareizi ar pirmo reizi. 
Lai veicas!🙂
""")


jautajumi = [{
    "jautajums":
    "Ko atgriež funkcija len()?",
    "varianti": [
        "Simbolu virknes garumu", "Simbolu virknes pirmo burtu",
        "Simbolu virknes pēdējo burtu", "Simbolu virknes apakšvirkni"
    ],
    "atbilde":
    "Simbolu virknes garumu"
}, {
    "jautajums":
    "Kāds būs rezultāts, izpildot 'programmētājs'.upper()?",
    "varianti":
    ["programmētājs", "PROGRAMMĒTĀJS", "Programmētājs", "pROGRAMMĒTĀJS"],
    "atbilde":
    "PROGRAMMĒTĀJS"
}, {
    "jautajums":
    "Kādu darbību veic metode strip()?",
    "varianti": [
        "Noņem liekās atstarpes tikai no sākuma",
        "Noņem liekās atstarpes tikai no beigām",
        "Noņem liekās atstarpes no sākuma un beigām",
        "Aizvieto atstarpes ar '_'."
    ],
    "atbilde":
    "Noņem liekās atstarpes no sākuma un beigām"
}, {
    "jautajums": "Ko atgriež metode find(), ja apakšvirkne nav atrasta?",
    "varianti": ["0", "-1", "None", "False"],
    "atbilde": "-1"
}, {
    "jautajums":
    "Kāds būs rezultāts, izpildot 'Sveiks, programmētāj!'.replace('programmētāj', 'skolēn')?",
    "varianti": [
        "'Sveiks, Skolēn!'", "'Sveiks, programmētāj!'", "'Sveiks,Skolēn'",
        "'Sveiks programmētāj!'"
    ],
    "atbilde":
    "'Sveiks, skolēn!'"
}, {
    "jautajums": "Kāds būs rezultāts, izpildot 'abrakadabra'.count('a')?",
    "varianti": ["4", "5", "6", "7"],
    "atbilde": "5"
}, {
    "jautajums":
    "Kāds būs rezultāts, izpildot ' '.join(['Labs', 'darbs'])?",
    "varianti":
    ["'Labs, darbs'", "'Labs darbs'", "'Labsdarbs'", "'L a b s d a r b s'"],
    "atbilde":
    "'Labs darbs'"
}, {
    "jautajums":
    "Ko pārbauda metode startswith()?",
    "varianti": [
        "Vai virkne sākas ar norādīto apakšvirkni",
        "Vai virkne beidzas ar norādīto apakšvirkni",
        "Vai virkne satur norādīto apakšvirkni", "Vai virkne ir tukša"
    ],
    "atbilde":
    "Vai virkne sākas ar norādīto apakšvirkni"
}, {
    "jautajums":
    "Kāds būs rezultāts, izpildot 'smuks suns'.capitalize()?",
    "varianti":
    ["'Smuks suns'", "'Smuks Suns'", "'smuks suns'", "'SMUKS SUNS'"],
    "atbilde":
    "'Smuks suns'"
}, {
    "jautajums":
    "Kādu funkciju veic metode 'find', ja norādīta apakšvirkne tiek atrasta vairākas reizes?",
    "varianti": [
        "Atgriež visu atrašanas vietu sarakstu",
        "Atgriež pirmo atrašanas vietu", "Atgriež pēdējo atrašanas vietu",
        "Atgriež atrašanas vietu skaitu"
    ],
    "atbilde":
    "Atgriež pirmo atrašanas vietu"
}]


def veiktTestu(jautajumi):
    paraditLogo()

    vardsUzv = ""
    while len(vardsUzv) < 8:
        vardsUzv = input("Ievadiet savu vārdu un uzvārdu: ")

    input("Uzspiediet 'enter' pogu, lai sāktu testu!")

    punktuSkaits = 0
    pareiziPirmajaMeginajuma = 0

    print()

    for idx, jautajums in enumerate(jautajumi, start=1):
        print(str(idx) + ". jautājums. " + jautajums['jautajums'])

        varianti = jautajums["varianti"]
        random.shuffle(varianti)
        for i, varianta in enumerate(varianti, start=1):
            print(" " * 11 + str(i) + ". " + varianta)

        print()

        pareizaAtbilde = jautajums["atbilde"]
        lietotajaAtbilde = ""
        pirmaisMeginajums = True

        while lietotajaAtbilde.lower() != pareizaAtbilde.lower():
            try:
                ievade = input("Jūsu minējums (1-4): ")
                if not ievade:
                    continue
                ievade = int(ievade) - 1
                if ievade < 0 or ievade >= len(varianti):
                    print("Šāds atbilžu variants nav. Mēģiniet vēlreiz.")
                    continue
                lietotajaAtbilde = varianti[ievade]

                if lietotajaAtbilde.lower() != pareizaAtbilde.lower():
                    print("Nepareizi! Mēģiniet vēlreiz.")
                    pirmaisMeginajums = False

            except ValueError:
                print("Šāds atbilžu variants nav. Mēģiniet vēlreiz.")

        print("Pareizi!")
        print()
        punktuSkaits += 1
        if pirmaisMeginajums:
            pareiziPirmajaMeginajuma += 1

    print("\nTests pabeigts! Jūs atbildējāt pareizi ar pirmo reizi uz " +
          str(pareiziPirmajaMeginajuma) + " no " + str(len(jautajumi)) +
          " jautājumiem.")

    with open("rezultati.csv", "a", newline='') as fails:
        laukumi = ['Vārds', 'Punkti']
        rakstitajs = csv.DictWriter(fails, fieldnames=laukumi)
        fails.seek(0, 2)
        if fails.tell() == 0:
            rakstitajs.writeheader()
        rakstitajs.writerow({
            'Vārds': vardsUzv,
            'Punkti': pareiziPirmajaMeginajuma
        })
        
    with open("rezultati.csv", "r") as fails:
        lasītājs = csv.DictReader(fails)
        rezultati = list(lasītājs)

    if rezultati:
        for rinda in rezultati:
            if rinda.get('Punkti') is None:
                rinda['Punkti'] = 10
            else:
                rinda['Punkti'] = int(rinda['Punkti'])

        rezultati = sorted(rezultati, key=lambda rinda: rinda['Punkti'], reverse=True)

        with open("rezultati.csv", "w", newline='') as fails:
            laukumi = ['Vārds', 'Uzvārds', 'Punkti']
            rakstītājs = csv.DictWriter(fails, fieldnames=laukumi)
            rakstītājs.writeheader()
            rakstītājs.writerows(rezultati)
            
veiktTestu(jautajumi)