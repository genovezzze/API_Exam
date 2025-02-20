'''
Jums jāizveido programma, kurai, ievadot vārdu, tas tiek novietots datu struktūrā atbilstoši
latviešu alfabētam. Vietu alfabētā nosaka ievadītā vārda pirmais burts.
Ja vārda pirmais burts atkārtojas, proti, tiek ievadīts vārds, kura vieta sarakstā jau ir aizņemta,
vārdu apmaina pret ievadīto. Pārbaudīt lietotāja ievadi, lai lietotājs nevarētu ievadīt nederīgas
vērtības. Par derīgu vērtību tiek uzskatīts tikai viens latviešu vārds, kurš sākas ar lielo burtu.
Programmai jāpaziņo, ja ievadītā vērtība neatbilst minētajiem nosacījumiem, tad programmai
jāpieprasa ievadīt jaunu vērtību. Ievadot vārdu, ir jāizvada programmas darbības soļi,
piemēram, ja vārds vēl nav ievietots, programma izvada teikumu „Pievienoju vārdu 1. vietā”.
Ņemt vērā, ka vārdu uzskaite alfabētā sākas ar kārtas skaitļa vietu Nr. 1.
Programma darbojas, līdz tiek pilnībā aizpildīts viss alfabēta saraksts.
Lai pārbaudītu programmas darbību, varat izmantot doto vārdu sarakstu:
Ainaži, Saulkrasti, Dobele, Sigulda, Tukums, Liepāja, Talsi, Ludza, Cēsis, Gulbene, Ventspils,
Vecumnieki, Engure, Ērgļi, Staicele, Kuldīga, Aizpute, Krāslava, Madona, Jūrmala, Rīga.
Punkts par katru no šādām programmas darbībām:
Vārda ievads
2.1. Nodrošināt vārda ievadīšanu.
2.2. Pārbaudīt lietotāja ievadīto vērtību, vai tas ir vārds (visas citas vērtības netiek ieskaitītas
kā pareizas).
2.3. Katru reizi ievadīt tikai vienu vārdu, nevis vārdu virkni.
2.4. Pārbaudīt, vai vārda pirmais burts ir lielais burts.
2.5. Atkārtoti ievadīt vērtību, ja ievadītā vērtība bijusi kļūdaina.
Datu struktūra
2.6. Izveidot datu struktūru, kurā uzglabāt latviešu alfabētu un tam atbilstošā sākumburta
pozīcijas kārtas numuru.
2.7. Izveidot datu struktūru, kurā glabāt jauno izveidoto sarakstu.
2.8. Noteikt ievadītā vārda pirmo burtu.
2.9. Ja vārda pozīcija sarakstā jau ir aizņemta ar kādu vārdu, tad to aizvietot ar ievadīto vārdu.
2.10. Ja vārda pozīcijas sarakstā vārda nav, tad tajā tiek ievietots ievadītais vārds.
2.11. Pārbaudītais vārds tiek ievietots alfabēta secības atbilstošajā pozīcijā, ņemot vērā tā
pirmo burtu.
2.12. Izdrukāt katru programmas darbību kā lasāmu teikumu.
2.13. Izvadīt kļūdas paziņojumu, ja ievadītais vārds neatbilst noteikumiem.
2.14. Datu struktūrā nedrīkst būt nultais elements.
2.15. Programma darbojas, līdz viss saraksts ir aizpildīts.
'''

import re

# Latviešu alfabēts
latvian_alphabet = "AĀBCČDEĒFGĢHIĪJKĶLĻMNŅO PQRŖSŠTUŪVZŽ".replace(" ", "")

# Izveidojam vārdnīcu ar tukšām vērtībām, kas atbilst alfabētam
word_dict = {letter: None for letter in latvian_alphabet}

def is_valid_word(word):
    """Pārbauda, vai ievadītais vārds ir derīgs (tikai viens vārds, sākas ar lielo burtu)"""
    return bool(re.fullmatch(r"[A-ZĒŪĪĀČĢĶĻŅŠŽ][a-zēūīāčģķļņšž]+", word))

def insert_word(word):
    """Ievieto vārdu vārdnīcā, aizstājot veco, ja nepieciešams"""
    first_letter = word[0]
    if first_letter in word_dict:
        if word_dict[first_letter]:
            print(f"Aizvietoju vārdu '{word_dict[first_letter]}' ar '{word}' {latvian_alphabet.index(first_letter) + 1}. vietā.")
        else:
            print(f"Pievienoju vārdu '{word}' {latvian_alphabet.index(first_letter) + 1}. vietā.")
        word_dict[first_letter] = word

def print_status():
    """Izvada pašreizējo saraksta stāvokli"""
    print("\nPašreizējais saraksts:")
    for i, letter in enumerate(latvian_alphabet, 1):
        word = word_dict[letter] if word_dict[letter] else "-"
        print(f"{i}. {word}")

# Galvenā cikla darbība
while None in word_dict.values():
    word = input("Ievadiet vārdu: ").strip()
    if not is_valid_word(word):
        print("Kļūda! Ievadiet derīgu vārdu, kas sākas ar lielo burtu.")
        continue
    insert_word(word)
    print_status()

print("Viss saraksts ir aizpildīts!")
