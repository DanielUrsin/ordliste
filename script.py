# -*- coding: iso-8859-1 -*-
import os, sys, time



def tall_til_tekst(tall):
    '''
    Translates numericial strings to worded numbers in Norwegian.
    Only numbers 1-99 are supported.
    '''

    nullTilTjue = {"0":"", "1":"en", "2":"to", "3":"tre", "4":"fire", "5":"fem",
                   "6":"seks", "7":"syv", "8":"�tte", "9":"ni", "10":"ti",
                   "11":"elleve", "12":"tolv", "13":"tretten", "14":"fjorten",
                   "15":"femten", "16":"seksten", "17":"s�tten", "18":"atten",
                   "19":"nitten"}
    tiere = {"2":"tjue", "3":"tretti", "4":"f�rti", "5":"femti",
             "6":"seksti", "7":"s�tti", "8":"�tti", "9":"nitti"}

    if 0 <= int(tall, 10) < 20:
        tekst = nullTilTjue[tall]
    elif 20 <= int(tall, 10) < 100:
        tekst = tiere[tall[0]]+nullTilTjue[tall[1]]
    else:
        raise ValueError

    return tekst


def populate():
    '''
    Parses the main dictionary file and creates a pure adjective list.
    The adjectives are written to an output file. The output file will be
    OVERWRITTEN each time this fucntion is called.
    '''
    input = open("fullformsliste.txt", "r", encoding="iso-8859-1", errors='ignore')
    output = open("output.txt", 'w', encoding="iso-8859-1")
    hovedliste = []
    for line in input:
        linje = line.split('\t')
        ord = linje[2]
        klasse = (linje[3].split(' '))
        if ord[0] == '-':
            continue
        if ord[-1] == 'e':
            continue
        if ord[-1] == 't':
            continue
        if 'adj' not in klasse:
            continue
        if 'ub' not in klasse:
            continue
        if 'pos' not in klasse:
            continue
        if 'be' in klasse:
            continue
        hovedliste.append(ord)

    hovedliste = list(set(hovedliste))
    hovedliste.sort(key=str.casefold)

    for ord in hovedliste:
        output.write(ord+'\n')
    input.close()
    output.close()


def hent_adjektiver(alder):
    '''Returns two adjectives with the same first letter as the input string.'''

    input = open("output.txt", 'r', encoding="ISO-8859-1")
    ordliste = []
    for line in input:
        if line[0] == alder[0]:
            ordliste.append(line[:-1])

    input.close()

    if not len(ordliste):
        raise ValueError("Ingen ord funnet")

    rand1 = int.from_bytes(os.urandom(4), byteorder='big')%len(ordliste)
    time.sleep(0.5)
    rand2 = int.from_bytes(os.urandom(4), byteorder='big')%len(ordliste)

    return ordliste[rand1], ordliste[rand2]


def main():

    if "-p" in sys.argv:
        populate()
    try:
        alder = sys.argv[1]
        if alder.isnumeric():
            alder = tall_til_tekst(alder)
        adj1, adj2 = hent_adjektiver(alder)
        print(f"\n\t{adj1}, {adj2} og {alder}\n")
    except:
        print("\nBruksanvisning:")
        print("\nSett inn alder mellom 1 og 99, som tall eller bokstaver.")
        print("Legg til \"-p\" for � sette opp adjektivlisten.")
        print("\nEksempel:\t$ python3 nitti -p\n")



if __name__ == "__main__":
    main()
