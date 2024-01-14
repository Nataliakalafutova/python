
#ukol1:
#Spočítej celkový počet všech znaků (včetně mezer, netisknutelných a neviditelných znaků) ve sloupci PRIMARYTITLE
#ze souboru netflix_imdb_test.tsv.
#Výsledek má být: 7650. 
#Pošli nám jako odpověď python soubor.

moj_seznam = []
with open("netflix_imdb_test.tsv", mode="r", encoding="utf8") as file:
    next(file)
    for line in file:
        line = line.strip().split('\t')
        #print(line)
        primary_title = line[2]
        #print(primary_title)
        moj_seznam.append(primary_title)
#print(moj_seznam)
pocet_znakov = 0
for nazov in moj_seznam:
    pocet_znakov = pocet_znakov + len(nazov)
print(f" Počet znakov je {pocet_znakov}.")











