#from turtle import *#Turtle ist ein Modul mit dem man zeichnen kann

#pencolor('brown')
#fillcolor('yellow')

# set start position
#penup()
#goto(-160,-100)
#pendown()

strich = 60

"""def zeichneSchritt(nummer):
	nummer = nummer - 1

	# Zeichne Gerüst
	if nummer == 0:
		left(90)
		circle(-60,180)
		circle(-60,-90)
		left(90)
	# Zeichne Balken vertikal
	elif nummer == 1:
		forward(strich*3)
		right(90)
	# Zeichne Balken Horiziontal
	elif nummer == 2:
		forward(strich*2)
	elif nummer == 3:
		right(180)
		forward(strich*1.3)
		left(45)
		forward(strich)
		right(180)
		forward(strich)
		right(45)
		forward(strich*1.3)
		right(90)
	# Zeichne Strick
	elif nummer == 4:
		forward(strich)
	# Zeichne Kopf
	elif nummer == 5:
		pencolor('blue')
		dot(strich/4)
	# Zeichne Körper
	elif nummer == 6:
		forward(strich*1.5)
	# Zeichne Bein links
	elif nummer == 7:
		right(45)
		forward(strich)
		right(180)
		forward(strich)
	# Zeichne Bein rechts
	elif nummer == 8:
		right(90)
		forward(strich)
		right(180)
		forward(strich)
	# Zeichne Hand links
	elif nummer == 9:
		right(45)
		forward(strich)
		left(45)
		forward(strich)
		right(180)
		forward(strich)
	# Zeichne Hand rechts
	elif nummer == 10:
		left(90)
		forward(strich)
		right(180)
		forward(strich)
	else:
		print("Das kann ich nicht zeichnen!")
"""

def buchstabeInSammlung(buchstabe):
	return buchstabe in buchstabenSammlung


def buchstabeInWort(buchstabe):
	if buchstabe != "":
		return (buchstabe in wort)


def fuegeBuchstabeHinzu(buchstabe):
	if buchstabe != "":
		buchstabenSammlung.append(buchstabe)


def printWort():
	ausgabe = ""

	for buchstabe in wort:
		if buchstabe.lower() in buchstabenSammlung:
			ausgabe = ausgabe + buchstabe + " "
		else:
			ausgabe = ausgabe + "_ "
  
	print(ausgabe)

def pruefeGewonnen():
	anzahlRichtigeBuchstaben = 0

	for buchstabe in wort:
		if buchstabe.lower() in buchstabenSammlung:
			anzahlRichtigeBuchstaben = anzahlRichtigeBuchstaben + 1

	return anzahlRichtigeBuchstaben == len(wort)

def printBuchstabenSammlung():
	print("Bekannte Buchstaben: " + " ".join(buchstabenSammlung))

buchstabenSammlung = []


### Letzter Schritt zur Musterlösung ist zuEnde und Verloren hinzufügen
### Musterlösung
print("Willkommen zu Galgenmaennchen vom Science Duo Diana und Marvin!")

wort = "blume"#evtl irgendwie zufällig auswählen

zuEnde = False
gewonnen = False

fehlerNummer = 0

while(not zuEnde):

	printWort()

	buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

	if buchstabeInSammlung(buchstabe):
		fehlerNummer = fehlerNummer + 1
		#zeichneSchritt(fehlerNummer)
		print( buchstabe + " hast du bereits geraten")
	elif buchstabeInWort(buchstabe):
		fuegeBuchstabeHinzu(buchstabe)
		print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
	else:
		fehlerNummer = fehlerNummer + 1
		#zeichneSchritt(fehlerNummer)
		fuegeBuchstabeHinzu(buchstabe)
		print("Der Buchstabe ist leider nicht im Wort!")

  
	printBuchstabenSammlung()

	## verloren
	if fehlerNummer == 11:
		zuEnde = True
		gewonnen = False

	## gewonnen
	if pruefeGewonnen():
		zuEnde = True
		gewonnen = True
	print("")
  
if gewonnen == True:
	print("Juhu!! Du hast gewonnen! Alles richtig!")
else:
	print("Oh schade. Du hast leider verloren :(")



