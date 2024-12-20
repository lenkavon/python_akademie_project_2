# Hlavicka
```txt
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lenka Urban
email: lenka.vondr@gmail.com
```

spusteni: `./game.py`

- hra umoznuje zvolit 3-7 ciferne cislo, defaultne se spusti s 4 ciframi, take je mozne nastavit opakovani cifer. 
- testy jsou generovane pomoci chatgpt, chtela jsem si vyzkouset setup test suite.
- cely projekt je hodne kosaty - chtela jsem si zkusit tvoreni balicku, lokalni importy. strukturu jsem delala podle https://docs.python-guide.org/ nevim, jestli je to takhle v poradku - bezne pouzivane, vim ze jsou nekteri programatori schopni se porvat do krve, protoze se jim nelibi urcity typ struktury..."
- taky jsem chtela zkusit ukladat statistiky do firebase, ale nechce se mi resit ukladani seceret nebo prihlasovani, takze zatim koukam po alternative, ale asi to jen zapisu do nejakeho lokalniho souboru, ale to se mi zatim moc nechce :D 
- naduzivam rekurzi, v praxi si ji moc neuziju, slo by to udelat do while, ale rekurze je rekurze... (co ma v pythonu lepsi performance?)



# Zadani: 

## Bulls & Cows
Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.

### Program musí splňovat tyto požadavky:

1) Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:

```py
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""
import ...
```

2) program pozdraví užitele a vypíše úvodní text  (viz. níže v ukázkách),
3) program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
4) hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,
5) program vyhodnotí tip uživatele,
6) program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
7) Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows),
8) zápis organizovaný do krátkých a přehledných funkcí.

### Úvodní text:

```
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
```

### Příklad hry s číslem 2017:

```
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's amazing!
```

### Program toho může umět víc. Můžeš přidat například:

- počítání času, za jak dlouho uživatel uhádne tajné číslo 
- uchovávat statistiky počtu odhadů jednotlivých her

