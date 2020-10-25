#Die Datei ist nicht ganz vollständig. Siehe dir lieber die Notebooks an.


######################## Day 1 ##########################

#Über den Programmierkurs

#ihr werdet euch nicht an jedes Detail erinnern, das ist aber normal. Ihr könnt das Script auch benutzen,
#um Dinge nachzuschlagen, aber das wichtige hier ist die Übung und dass ihr Grundwissen habt.
#Sucht im Internet, wenn ihr nicht wisst, wie etwas funktioniert, das gehört zum Programmieren dazu.
#wichtig ist, dass ihr weiter übt, sonst vergesst ihr vieles wieder schnell.
#Es gibt auch noch viel mehr als wir in diesem Kurs behandeln können, wir hoffen ihr macht danach selbstständig weiter.
#Programmieren lernt man durch programmieren, nicht durch Tutorials anschauen.
#Bla Bla Bla

#Die Aufgaben sind das wichtigste, ihr solltet versuchen sie alleine zu machen (oder maximal in zweier Teams, aber schaut, dass dann nicht einer alles alleine macht).
#Wenn ihr etwas nicht verstanden habt, meldet euch direkt.
#Wenn ihr eine Aufgabe nicht lösen könnt, fragt uns, wir helfen euch, versucht es aber unbedingt erst einmal selbst.



# Einführung
## print
print("Hallo!")

print("Mein Name ist Marvin")

### Aufgabe
print("Hallo Welt")

## variablen
### generell Variablen
name = "Marvin"
print(name)

#### Aufgabe
plz = "6...."
ort = "Stuttgart"
print(ort)
ort_mit_plz = plz + " " + ort
print(ort_mit_plz)

### Variablen kombinieren
print("Mein Name ist " + name)


#### Aufgabe
print("Mein Name ist " + name + " und ich komme aus " + ort + ".")

## input + kommentare
#name = "Marvin"
name = input()

print("Wie ist dein Name?")
name = input()

### Aufgabe
print("Woher kommst du?")
ort = input()

## if Bedingung
print("Wie geht es dir?")
antwort = input()

#### Einrückung erklären, mal das zweite if 
if antwort == "gut":
  print("Supi, mir geht es auch gut!")
  if antwort == "schlecht":
    print("Oh das tut mir leid")

if antwort == "gut":
  print("Supi, mir geht es auch gut!")
else:
  print("Ich kann dich nicht verstehen.")

if antwort == "gut":
  print("Supi, mir geht es auch gut!")
elif antwort == "schlecht":
  print("Oh das tut mir leid")
else:
  print("Ich kann dich nicht verstehen.")


#Zahlen erklären
stunden_programmiert = 3000 #Variable (klein geschrieben)
Antwort_auf_alles = 42 #Konstante (groß geschrieben)

print("Wie alt bist du?")
alter = int(input()) #weil input einen String zurückgibt, muss man das zu einem Integer konvertieren


#Mit Zahlen kann man Rechnungen durchführen
meinalter = 17
alter = int(input("Wie alt bist du? "))

if meinalter == alter:
	print("Lustig, ich auch")
elif meinalter > alter:
	print("Dann bin ich ", meinalter - alter, " Jahre älter als du.")
else:
	print("Dann bist du ", alter - meinalter, " Jahre älter als ich")


#Vergleichsoperationen
print("17 >= 17: ", 17 >= 17)
print("17 > 17: ", 17 > 17)
print("13 != 17: ", 13 != 17)
print("26 != 'Hallo': ",26 != "Hallo") #Strings in Strings darstellen
print("'Hi' != 'Hi': ", "Hi" != "Hi")

### Aufgabe Verkauf
#Produkte: Wasser, Bier, Schnaps
#Der Kunde soll eines der Produkte auswählen. Dann musst du ihn ggf nach dem Alter fragen.
#Du kannst ihm immer Wasser, Bier ab 16 Jahren und Schnaps ab 18 Jahren verkaufen

#Lösung
print("Was möchtest du kaufen?")
produkt = input()
if produkt == "Wasser":
	print("Bittesehr :)")
elif produkt == "Bier":
	alter = int(input("Wie alt bist du? "))
	if alter > 15:
		print("Bittesehr :)")
	else:
		print("Du bist leider noch zu jung um Bier zu kaufen")
else:#will Schnaps kaufen
	alter = int(input("Wie alt bist du? "))
	if alter > 17:
		print("Bittesehr :)")
	else:
		print("Du bist leider noch zu jung um Schnaps zu kaufen")	


#mathematische Operationen
a = 9
b = 12
print(a+b)
print(a-b)
print(a*b)
print(a/b)#Kommazahl
print(12*3+5)
print(12*(3+5))
print(2**4)#'hoch'
print(3**3)


c = a/b
print(type(a))#int
print(type(c))#double
#Unterschiedlicher Datentyp
#(gut zu wissen, aber in Python erstmal nicht so wichtig)

print(a//b)#floor division (immer einfach abgerundet)
d = a//b
print(type(d))##sollte int sein

print(round(a/b))#rundet zum nächsten Integer


#Modulo ("Rest")
print(a%b)
print(b%a)
print(28 % 6)

#Überprüfe ob eine Zahl gerade ist
z = int(input("Gib mir eine Zahl: "))
if z % 2 == 0:
	print(z, " ist gerade!")
else:
	print(z, " ist ungerade!")


# Hausaufgabe: FizzBuzz
#Spiel geht so: Man bekommt eine Zahl, wenn diese durch 3 und durch 5 teilbar ist sagt man FizzBuzz, sonst,
#wenn sie durch 3 teilbar ist Fizz, sonst wenn sie durch 5 teilbar ist Buzz und ansonsten einfach nur die Zahl
#Aufgabe: Programmiere FizzBuzz

#Lösung
zahl = int(input("Gebe hier die Zahl ein: "))
if zahl % 15 == 0:
	print("Fizzbuzz")
elif zahl % 3 == 0:
	print("Fizz")
elif zahl % 5 == 0:
	print("Buzz")
else:
	print(zahl)

# Lösung 2
zahl = int(input("Gebe hier die Zahl ein: "))
output = ""
if zahl % 3 == 0:
	output += "Fizz"
if zahl % 5 == 0:
	output += "Buzz"
if output == "":
	output = zahl
print(output)






##################### Day 2 ##############################################

#Besprechung Hausaufgabe (auch gut als Wiederholung um wieder rein zu kommen)

#Boolean Zeug

a = True
b = False
c = (17 == 24)
d = (5 <= 78)

e = !c
f = a or b
g = a and b
h = b or (a and not c)

if f:
	print("f is True")
if g:
	print("g is True")
else:
	print("g is False")


## Schleifen

# while

while True:
	print("Endlosschleifen sind böse!")

a = 1
maximum = int(input("Bis zu welcher Zahl möchtest du zählen? "))
while a <= maximum:
	print(a)
	a += 1 # ist das gleiche wie a = a+1

#Es gibt auch -=, *= und /=

while input("Muss ich noch mal Hallo sagen? (y/n) ") == "y":
	print("Hallo")


#For

for i in range(13):#von 0 bis 22
	print(i)

for i in range(2,15): #von 0 bis 43
	print(i)

for i in range(3,36,3): #von drei an jede dritte Zahl, die kleiner als 36 ist
	print(i)


#Listen

list1 = [1,2,4,8,16]

for i in list1:
	print(i)

list2 = []
for i in range(200):
	list2.append(i)
print(list2)


##Aufgabe
#Liste mit allen Zweierpotenzen von 1 bis 2^20

#Lösung
powers_of_2 = []
for i in range(21):
	powers_of_2.append(2**i)


namen = ["Marvin", "Simon", "..."]
print("Leute im Programmierkurs sind: ")
for name in namen:
	print("-", name)

#Indexe

#Indexe beginnen immer mit 0

list3 = [10,20,30,40,50,60]
print(list3[0])#erstes Element in der Liste
print(list3[3])#viertes Element


#geht auch mit Strings
alph = "abcdefghijklmnopqrstuvwxyz"
print(alph[11])#12ter Buchstabe im Alphabet


#Aufgabe
#gebe alle Elemente vom 5. bis zum 9. der Liste list4 aus
list4 = [1,1,2,3,5,8,13,21,34,55,89,144]

#Lösung
for i in range(5,10):
	print(list4[i])


#'von hinten':
print("Der letzte Buchstabe ist: ", alph[-1])
print("Der vorletzte Buchstabe ist: ", alph[-2])


#len() gibt die Länge einer Liste zurück
print(len(list4))
for i in range(len(list4)):
	print("Das Element bei Index ", i, " ist: ", list4[i])


#Aufgabe
#erstelle einen String der das Alphabet rückwärts beinhaltet, indem du den String alph nutzt

#Lösung
rev_alph = ""
for i in range(1,len(alph)+1):
	rev_alph += alph[-i]

#oder
rev_alph = ""
for i in range(len(alph)-1,-1,-1):
	rev_alph += alph[i]


#umgekehrt auf den Index kommen mit index()
print(list3.index(30))

#es gilt a == list[list.index(a)]

print(alph.index("l"))#gibt index von l in alph zurück


#slices

first_half_list3 = list3[:3]#mit Indexen 0,1,2
second_half_list3 = list3[3:]#mit Indexen 3,4,5
middle_of_list3 = list3[2:4]#mit Indexen 2,3

#Wie sonst auch (ähnlich wie bei range()), gibt list[minimum:maximum] alle Elemente von Index minimum bis maximum-1 zurück

#Aufgabe
#erstelle einen String wo zunächst die hintere Hälfte des Alphabets vorkommt und dann die vordere Hälfte.

#Lösung
string = alph[13:] + alph[:13]


#Hausaufgabe 1
#schreibe ein Programm, das checkt, ob ein eingabestring ein Palindrom ist, bzw. ob er vorwärts und rückwärts gleich ist.
#ABBA und LAGERREGAL sind beispielsweise Palindrome.

#Lösung 1
string = input("Gebe deinen String hier ein: ")
rev_string = ""
for i in range(1,len(string)+1):
	rev_string += string[-i]
if string == rev_string:
	print("Juhu, ein Palindrom")
else:
	print("Leider kein Palindrom")

#Lösung 2
string = input("Gebe deinen String hier ein: ")
pal = True
for i in range(len(string)):
	if string[i] != string[-i-1]:
		pal = False
if pal:
	print("Juhu, ein Palindrom")
else:
	print("Leider kein Palindrom")



#Hausaufgabe 2
#Schreibe ein Programm, das die Quersumme einer Zahl ausspuckt. (Tipp: Modulo und floor division)


#Lösung
zahl = int(input("Gebe hier deine Zahl ein: "))
quersumme = 0
while (zahl != 0):
	quersumme += zahl % 10
	zahl //= 10
print(quersumme)




##################################### Day 3 ###########################################

#Wieder Besprechung der Hausaufgaben


#imports and guessing game

import random

mini = 1
maxi = 10
r = random.randint(mini,maxi)
if int(input("Rate meine Zahl: ")) == r:
	print("Richtig, super geraten!")
else:
	print("Das ist leider nicht meine Zahl")


#Aufgabe
#programmiere das Ratespiel, wobei das Programm eine zufällige Zahl zwischen 1 und 100 wählt und man mehrfach raten kann.
#Das Programm soll einem nach jedem mal raten sagen, ob die geratene Zahl größer, gleich oder kleiner als die gesuchte Zahl ist.

#Lösung

mini = 1
maxi = 100
r = random.randint(mini, maxi)
guess = 0
while (guess != r):
	guess = int(input("Rate meine Zahl: "))
	if guess > r:
		print("zu groß")
	elif guess < r:
		print("zu klein")
print("Richtig, das war meine Zahl!")



#Funktionen - Juhu!

def sag_hallo():
	print("Hallo!")

sag_hallo()


#verkürzen, verschönern und vereinfachen Code:

def vorstellen():
	print("Hallo, ich bin Simon.")
	print("Ich bin 17 Jahre alt.")
	print("Ich studiere in Heidelberg Physik.")
	print("Ich war 3 Jahre im Science Lab")
	print("und ich mag Informatik.")


vorstellen()
vorstellen()#wenn man sich mehrfach vorstellen muss, muss man nur die Funktion mehrfach aufrufen, nicht die ganzen prints nochmal schreiben


#Parameter

def vorstellen2(name):#wichtig ist generell, dass ihr unterschiedliche Variablen und Funktionen auch unterschiedlich benennt
	print("Hallo ich bin " + name + ".")


vorstellen2("Simon")
vorstellen2("Marvin")



def f(x):
	print(2*x**2 + 3*x - 5)


f(1)
f(3)

#return

def f2(x):
	return 2*x**2 + 3*x - 5 #return ist sehr nützlich, wenn man das Ergebnis wiederverwenden will

y = f2(1)
print(y)

print(f2(3))


#Aufgabe
#schreibe eine Funktion, die eine Zahl n als Parameter bekommt und dann die Summe aller Zahlen von 1 bis n zurück gibt
#führe die Funktion für die Werte n=10, n=200, n=5000 aus und gebe das Ergebnis aus

#Lösung
def sum_to_n(n):
	res = 0
	for i in range(n+1):
		res += i
	return res

print(sum_to_n(10))
print(sum_to_n(200))
print(sum_to_n(5000))



#Aufgabe
#schreibe eine Funktion, die eine Liste von Zahlen bekommt und das kleinste Element zurückgibt

#Lösung
def min_of_list(list1):
	mini = list1[0]
	for item in list1:
		if item < mini:
			mini = item
	return mini



def reverse(string):
	rev_string = ""
	for i in range(1,len(string)+1):
		rev_string += string[-i]
	return rev_string

print(reverse("Hallo!"))
print(reverse("RACECAR"))


def g(x,y):#es gehen auch mehrere Parameter
	return (x+y)**2

g(2,3)
g(7,2)

#Aufgabe
#schreibe eine Funktion rotate_string, die einen String s und eine Zahl k bekommt, und den String um k rotiert.
#Bei einer Rotation um 1 wird das letzte Zeichen an den Anfang gesetzt. Bei einer Rotation um k wird dies k mal hintereinander ausgeführt

#Tipp: ihr könnt, müsst aber nicht, Slices verwenden

#relativ einfache Version: k <= len(s)

#etwas schwerere Version: k darf größer als len(s) sein (aber kleiner als 10^8). 

#noch schwerere Version: k darf riesig sein (bis zu 10^18). Beachte, dass du nicht so viele Operationen ausführen kannst,
#du kannst also nicht einfach k mal eins weiter rotieren.



#Lösung einfache Version

def rotate_string(string, k):
	return string[-k:] + string[:-k]

#Lösung etwas schwerere Version

def rotate_string(string, k):
	for i in range(k):
		string = string[-1] + string[:-1]

#Lösung noch schwerere Version

def rotate_string(string, k):
	return string[-(k%len(string)):] + string[:-(k%len(string))]




#Tupel
#wie Listen nur nicht vergrößer oder verkleinerbar (und etwas schneller)
#meistens kann man auch einfach Listen verwenden

coordinates1 = (10,25)
coordinates2 = (22,14)

def manhatten_distance(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])#abs ist der Betrag

print(manhatten_distance(coordinates2,coordinates1))


#Hausaufgabe 1
#Schreibe eine Funktion, die zwei Koordinaten (2er-Tupel) bekommt. Eine Person startet bei der ersten Koordinate 
#und will schrittweise zur zweiten Koordinate laufen.
#Schreibe eine Funktion, die einen Weg von der Startposition zur Endposition findet. Die Funktion soll alle Koordinaten auf
#diesem Weg printen.

#Beispiel: Start: (11,15), Ende: (13,11)
#möglicher Output: (11,15),(12,15),(13,15),(13,14),(13,13),(13,12),(13,11)

#Lösung
def go_path(start,end):
	print(start)
	while (start[0] != end[0]):
		if start[0] > end[0]:
			start[0] -= 1
		else:
			start[0] += 1
		print(start)
	while (start[1] != end[1]):
		if start[1] > end[1]:
			start[1] -= 1
		else:
			start[1] += 1
		print(start)
	


#Hausaufgabe 2 (schwer)
#Vielleicht hast du schonmal was von der Caesar Verschlüsselung gehört. Diese funktioniert wie folgt:
#Du hast einen Nachricht als String und möchtest diese verschlüsseln.
#Du nimmst dir eine Zahl k zwischen 0 und 25 (am besten nicht 0), welche der Schlüssel für deine Verschlüsselung ist.
#Nun schaust du für jeden Buchstaben in deinem String, an welcher Stelle im Alphabet dieser steht.
#Disen Buchstaben ersetzt du nun mit dem Buchstaben, der k Stellen weiter hinten im Alphabet steht (nach Z fängst du einfach wieder mit A an)
#Die Entschlüsselung soll das wieder Rückgängig machen.
#In unserem Fall besteht der String nur aus Großbuchstaben.

#Programmiere ceasar_enc und ceasar_dec, die eine Nachricht encrypten oder decrypten sollen. (Tipp: Du kannst die rotate_string Funktion verwenden)
#Teste dein Programm

#Beispiel: ceasar_enc("DIEGERMANENGREIFENAN", 2) --> FKGIGTOCPGPITGKHGPCP
#und ceasar_dec("FKGIGTOCPGPITGKHGPCP", 2) --> DIEGERMANENGREIFENAN


def rotate_string(string, k):
	return string[-(k%len(string)):] + string[:-(k%len(string))]


alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ceasar_enc(message, k):
	enc_message = ...
	return enc_message

def ceasar_dec(enc_message, k):
	message = ...
	return message


#Lösung

def rotate_string(string, k):
	return string[-(k%len(string)):] + string[:-(k%len(string))]

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ceasar_enc(message, k):
	rot_alph = rotate_string(alph, k)
	enc_message = ""
	for c in message:
		enc_message += alph[rot_alph.index(c)]
	return enc_message

def ceasar_dec(enc_message, k):
	message = ceasar_enc(enc_message, -k)
	return message

s = "DIEGERMANENGREIFENAN"
enc = ceasar_enc(s,2)
print(enc)
print(ceasar_dec(enc,2))



####################################### Day 4 ###########################################

#Besprechung Hausaufgaben


#Rekursion

#Man kann eine Funktion auch in dieser Funktion aufrufen --> Rekursion

def fib(n):
	if n == 1 or n == 2:#Rekursionsanker
		return 1
	else:#Rekursionsschritt
		return fib(n-1) + fib(n-2)

#wenn der Rekursionsanker fehlt gibt es eine Endlosschleife

#Aufgabe
#Programmiere die Fakultätsfunktion rekursiv
#Diese ist wie folgt definiert: fak(n) = n*(n-1)*(n-2)*...*1

#Lösung
def fak(n):
	if n == 1:
		return 1
	else:
		return n * fak(n-1)


#Man kann eigentlich alles sowohl iterativ als auch rekursiv berechnen. Manchmal ist eines davon aber leichter.

def reverse2(string):
	if len(string) == 0:
		return ""
	else:
		return string[-1] + reverse2(string[:-1])

#Aufgabe
#Programmiere die Berechnung des Binominalkoeffizienten rekursiv
#Für den Binominalkoeffizienten gilt:
#binom(n,0) = 1, binom(n,n) = 1
#binom(n,k) = binom(n-1,k-1) + binom(n-1, k)

def binom(n,k):
	if k == 0 or k == n:
		return 1
	else:
		return binom(n-1,k-1) + binom(n-1,k)



#Effizienz und Laufzeit

#häufig ist es sehr wichtig, dass Algorithmen schnell sind

#Die Funktionen fib() und binom() brauchen sehr viel Zeit, da häufig sehr viele Teile mehrfach berechnet werden.
#(Bspw. wird fib(2) schon 5 mal berechnet, wenn man fib(6) berechnet)

#Zeigen, dass fib(30) oder fib(35) schon sehr lange braucht.

#Deswegen ist es hier sinnvoll, Zwischenergebnisse zu speichern, oder den Algorithmsu anders zu programmieren,
#sodass nur einmal eine Zahl berechnet werden muss.

#Das geht so (mit Memory Array):

mem = [0,1,1]#Es gibt keine 0te Fibonaccizahl und die ersten beiden sind 1
def fib2(n):
	if len(mem) > n:
		return mem[n]
	else:
		mem.append(fib2(n-1) + fib2(n-2))
		return mem[n]

#oder so:

def fib3(n):
	prev_fib = 1
	prev2_fib = 1
	for i in range(2,n):
		next_fib = prev_fib + prev2_fib
		prev2_fib = prev_fib
		prev_fib = next_fib
	return prev_fib



#Dictionaries

prices = {"Apple":"1€", "Banana":"2€","Strawberries":"3€"} #Key: value Paare
prices2 = {"Apple":1, "Banana":2,"Strawberries":3, "Potato":0.5}
buying = {"Apple":3,"Banana":5,"Potato":10}

print(prices["Apple"])#ähnlich wie Listen, nur mit keys anstatt Indexe
print(prices2["Potato"])
print(buying.keys())
print(buying.values())
print(buying)

prices2["Carrot"] = 1.5
print(prices2["Carrot"])

for key, value in prices2.items():
	print("The product ", key, " costs ", value, "€.")


#Aufgabe
#berechne den Preis (durch ein Programm), den man Zahlen muss, wenn man die Produkte aus buying mit der jeweiligen Anzahl und den Preisen aus prices2 kauft.

#Lösung
cost = 0
for item, amount in buying:#Key=item, value=amount
	cost += prices2[item] * amount
print(cost)




#Sortieren, Binäre Suche und Hashing

#Problem (nicht zum selbst bearbeiten): Du hast zwei Listen gegeben, und möchtest die Elemente finden, die in beiden Listen vorkommen.

list1 = [76,23,6,2,11,42,15,123,8,21,55]
list2 = [87,2,34,85,21,33,55,6,12,76,31,876,35,29]


#langsame Lösung
shared = []
for i in list1:
	for j in list2:
		if i == j:
			shared.append(i)
print(shared)


#schnellere Lösung:
#Sortieren und Binäre suche
#erklären wieso das Sinnvoll ist --> vergleich mit dem Ratespiel, wo man herausfinden muss, was die gesuchte Zahl war

shared = []
list2.sort()#sortiert die Liste
print(list2)

#binäre Suche
for item in list1:
	#left und right geben den Bereich der Indexe an, wo die Zahl item vorkommen könnte
	left = 0
	right = len(list2)-1
	while left <= right:
		mid = (left + right)//2
		if list2[mid] == item:
			shared.append(item)
			break #bricht aus der inneren Schleife aus (wir müssen dann nicht mehr weiter suchen)
		elif list2[mid] < item:
			left = mid+1
		else:
			right = mid-1
print(shared)

#bei der Implementierung von binären Suchen entstehen häufig Fehler


#noch etwas schnellere Lösung

#wir benutzen eine neue Datenstruktur: ein Set
#Ein Set funktioniert über Hashing. #Hashing erklären. (by the way, Dictionaries funktionieren auch mit Hashing)
#Dadurch können wir sehr schnell feststellen, ob ein bestimmtes Element in dem Set drin ist oder nicht.

s = set()
shared = []
for item in list1:
	s.add(item)
for item in list2:
	if item in s:
		shared.append(item)
print(shared)

#Man kann sets übrigens auch so erstellen:

s = {"Apple", 2, -0.5, 42, 73}#wie Dictionaries nur ohne values



#Hausaufgabe 1
#programmiere einen Algorithmus, der das Rästelspiel von gestern (oder vorgestern) in möglichst wenig Schritten löst.
#Dein Algorithmus soll dabei immer die Feedback Funktion benutzen

import random
r = random.randint(1,100)

def feedback(guess):
	if r == guess:
		return "="
	elif r < guess:
		return "<"
	else:
		return ">"


#Lösung
left = 1
right = 100
while left <= right:
	mid = (left + right)/2
	f = feedback(mid)
	if f == "=":
		print("Die Zahl ist ", mid)
		break #bricht aus der inneren Schleife aus (wir müssen dann nicht mehr weiter suchen)
	elif f == ">":
		left = mid+1
	else:
		right = mid-1


#Hausaufgabe 2 (schwierig)
#Programmiere ein Programm, das eine Liste bekommt und nacheinander alle Permutationen dieser Liste ausschreibt.
#Bsp: [1,2,3] --> [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
#Tipp: Rekursion (mit einer Schleife)

#Lösung

current = []

def perm(list1):
	if len(list1) == 1:
		current.append(list1[0])
		print(current)
		current.pop()
	else:
		for i in range(len(list1)):
			rest = list1[:i] + list1[i+1:]
			current.append(list1[i])
			perm(rest)
			current.pop()

perm([1,2,3,4])



#Zusatz Hausaufgabe (freiwillig und relativ schwer)
#Programmiere die binom() Funktion effizient (aber ohne Fakultät).

#Lösung

mem = {}
def binom(n,k):
	if k == 0 or k == n:
		return 1
	elif (n,k) in mem:
		return mem[(n,k)]
	else:
		mem[(n,k)] = binom(n-1,k-1) + binom(n-1,k)
		return 	mem[(n,k)]


################################# Day 5 #########################

#Besprechung Aufgaben


#Juhu wir programmieren ein Spiel (Hangman)

#Regeln von Hangman erklären und wie das Spiel aussehen soll

from turtle import *#Turtle ist ein Modul mit dem man zeichnen kann

pencolor('brown')
fillcolor('yellow')

# set start position
penup()
goto(-160,-100)
pendown()

strich = 60

def zeichneSchritt(nummer):
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


def buchstabeInSammlung(buchstabe):
 	return buchstabe in buchstabenSammlung


def buchstabeInWort(buchstabe):
 	if buchstabe != "":
    	return buchstabe in wort


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


### Ab hier etwas verändern


## Aufbau des Programms

### zeichnen mit Turtle
fehlerNummer = 0

while fehlerNummer != 11:
  	fehlerNummer = fehlerNummer + 1
  	zeichneSchritt(fehlerNummer)


### Einlesen
#### Einführen von input mit Parameter
buchstabe = input("Gib hier den naechsten Buchstaben ein: ")
wort = "blume"

if buchstabeInSammlung(buchstabe):
 	print(buchstabe + " hast du bereits geraten")
elif buchstabeInWort(buchstabe):
  	print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
else:
 	print("Der Buchstabe ist leider nicht im Wort!")


### Hinzufügen bekannter Buchstaben
buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

fuegeBuchstabeHinzu(buchstabe)
printBuchstabenSammlung()


### Aufgabe: Einlesen + Hinzufügen
buchstabe = input("Gib hier den naechsten Buchstaben ein: ")
wort = "blume"
fehlerNummer = 0

if buchstabeInSammlung(buchstabe):
  	fehlerNummer = fehlerNummer + 1
  	zeichneSchritt(fehlerNummer)
  	print( buchstabe + " hast du bereits geraten")
elif buchstabeInWort(buchstabe):
  	fuegeBuchstabeHinzu(buchstabe)
  	print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
else:
  	fehlerNummer = fehlerNummer + 1
  	zeichneSchritt(fehlerNummer)
  	fuegeBuchstabeHinzu(buchstabe)
  	print("Der Buchstabe ist leider nicht im Wort!")

printBuchstabenSammlung()


### mehrere Buchstaben mit while hinzufügen
zahl = 0

while zahl != 6:
  	buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

  	fuegeBuchstabeHinzu(buchstabe)
  	printBuchstabenSammlung()
  	zahl = zahl + 1


### Aufgabe: Einlesen + Hinzufügen + While
wort = "blume"

zahl = 0
fehlerNummer = 0

while zahl != 6:

  	buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

  	if buchstabeInSammlung(buchstabe):
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	print( buchstabe + " hast du bereits geraten")
  	elif buchstabeInWort(buchstabe):
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
  	else:
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Der Buchstabe ist leider nicht im Wort!")

  	printBuchstabenSammlung()

  	zahl = zahl + 1


### Einlesen + Hinzufügen + While + Gewinnen
wort = "blume"

gewonnen = False
fehlerNummer = 0

while gewonnen == False:
  	buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

  	if buchstabeInSammlung(buchstabe):
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	print( buchstabe + " hast du bereits geraten")
  	elif buchstabeInWort(buchstabe):
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
  	else:
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Der Buchstabe ist leider nicht im Wort!")

  	printWort()

  	printBuchstabenSammlung()

  	if pruefeGewonnen():
    	gewonnen = True

print("Juhu!! Du hast gewonnen! Alles richtig!")

### Letzter Schritt zur Musterlösung ist zuEnde und Verloren hinzufügen
### Musterlösung
print("Willkommen zu Galgenmaennchen vom Science Duo Diana und Marvin!")

wort = "blume"

zuEnde = False
gewonnen = False

fehlerNummer = 0

while(not zuEnde):
  	buchstabe = input("Gib hier den naechsten Buchstaben ein: ")

  	if buchstabeInSammlung(buchstabe):
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	print( buchstabe + " hast du bereits geraten")
  	elif buchstabeInWort(buchstabe):
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Richtig! " + buchstabe + " ist in dem gesuchten Wort enthalten!")
  	else:
    	fehlerNummer = fehlerNummer + 1
    	zeichneSchritt(fehlerNummer)
    	fuegeBuchstabeHinzu(buchstabe)
    	print("Der Buchstabe ist leider nicht im Wort!")

  	printWort()
  
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




## Verbesserungsmöglichkeit
### Das Wort mit einem input() einzulesen

## Foto-Shooting



## logische Schritte der Musterlösung
# 1. print Begrüßung
# 2. Wort definieren
# 3. input nächster Buchstabe
# 4. buchstabenSammlung prüfen
# 4.1. Ist Buchstabe schon vorhanden
# 4.2. Ist Buchstabe in Wort
# 4.3. Buchstabe richtig oder falsch evaluieren
# 4.4. Buchstabe zur Sammlung hinzufügen
# 5. Bekannte buchstabenSammlung ausgeben
# 6. Gewonnen und verloren evaluieren (while Abbruchbedingung)










##was viellecht noch fehlt:
#Geltungsbereich der Variablen (nur in einer Funktion oder in einer Schleife, wenn sie dort initialisiert wurden)
#(gibt auch globale Variablen mit global) --> bei der Einführung von Schleifen und Funktionen sagen
#wie man mit Dateien arbeitet: Einlese/Ausgabe
#module und libraries / mit mehreren Dateien arbeiten
#Klassen und so



##Noch ein paar Tipps
#Sucht im Internet --> Stackoverflow ist toll
#matplotlib ist toll zum plotten
#numpy ist toll wenn man schnelle Operationen haben will, numpy arrays sind aber nicht ganz so flexibel wie Listen (so wie Tupel)
#Es gibt einen Haufen von Libraries. Schaut einfach im Internet nach, wenn ihr ein relativ allgemeines Problem lösen wollt,
#vermutlich hat es schon jemand zuvor gelöst
#Debugging Tipps
#Vorteile und Nachteile von Python. Wann man andere Programmiersprachen braucht und was dort anders sein könnte.
#das was wir schon ganz am Anfang gesagt haben


##Weiterführende Links
#Hier noch irgendwelchen online Programmierkurse oder so einfügen, sodass sie weiter machen können


