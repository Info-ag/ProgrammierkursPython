# Python Anfänger Programmierkurs

## Konzept
- 2 Tage (Samstag/Sonntag) in Präsenz, jeweils 10–17 Uhr
- 5,5h Programm pro Tag: 1h Mittagspause und 2× 15min Pause
- Wir arbeiten in Google Colab, alles läuft über die Notebooks:
  - Die Theorie steht im Notebook, die Mentoren erklären sie abschnittsweise.
  - Nach jedem Abschnitt kommen kurze Aufgaben direkt im Notebook. Die Mentoren gehen herum, helfen und fangen Fehler ab.
  - Aufgaben mit *(Zusatz)* sind für die Schnellen.
- Am Ende von Tag 2 programmieren alle in Zweiergruppen ein eigenes Spiel (Hangman).
- Pro Block gibt es ein Notebook, jeweils als `student_version` (ohne Lösungen) und `teacher_version` (mit Lösungen und Hinweisen für Mentoren).

## Ablauf

### Samstag: Grundlagen

| Zeit | Block | Theorie | Aufgaben |
|---|---|---|---|
| 10:00–11:15 | [Block 1](Programming_course_Day1_Block1_student_version.ipynb) | Begrüßung, Colab, print, Variablen/Strings, input, Kommentare, if | Hallo Welt, Vorstellen, Passwortabfrage |
| 11:15–11:30 | *Pause* | | |
| 11:30–12:30 | [Block 2](Programming_course_Day1_Block2_student_version.ipynb) | int/float, Vergleiche, Booleans, mathematische Operatoren inkl. `//` und `%` | Gerade/ungerade, Getränkeverkauf, FizzBuzz, *Schaltjahr* |
| 12:30–13:30 | *Mittagspause* | | |
| 13:30–15:00 | [Block 3](Programming_course_Day1_Block3_student_version.ipynb) | while, for, range, Listen, Indexe, `len`, `in` | Countdown, 7er-Reihe, Zweierpotenzen, Alphabet rückwärts, Vokale zählen, Quersumme |
| 15:00–15:15 | *Pause* | | |
| 15:15–17:00 | [Block 4](Programming_course_Day1_Block4_student_version.ipynb) | Slices, Löschen, Dictionaries | Palindrom, Einkaufsliste, Preisrechner, Buchstaben zählen, *Caesar* |

### Sonntag: Funktionen, Klassen, Projekt

| Zeit | Block | Theorie | Aufgaben |
|---|---|---|---|
| 10:00–11:15 | [Block 1](Programming_course_Day2_Block1_student_version.ipynb) | Wiederholung, import/random, Funktionen, Parameter, return | Wiederholungsaufgabe, Ratespiel, sum_to_n, ist_gerade |
| 11:15–11:30 | *Pause* | | |
| 11:30–12:30 | [Block 2](Programming_course_Day2_Block2_student_version.ipynb) | Funktionen kombinieren, Standardwerte, Geltungsbereich; Klassen, Objekte, Attribute, Methoden | min_of_list, häufigster Buchstabe, rotate_string, *Caesar mit Funktionen*, Tier |
| 12:30–13:30 | *Mittagspause* | | |
| 13:30–14:15 | [Block 3](Programming_course_Day2_Block3_student_version.ipynb) | Wiederholung Klassen, Vererbung, OOP vs. funktional | Hund/Vogel |
| 14:15–16:30 | [Block 4](Programming_course_Day2_Block4_student_version.ipynb) | Projekt Hangman (Pause nach Bedarf) | Schritt für Schritt aus Funktionen, dann Erweiterungen (Galgen in ASCII, Klasse, ...) |
| 16:30–17:00 | | Vorstellung der Spiele, Ausblick: wie geht es weiter | |

Das Projekt ist ohne Klassen lösbar, die Klassenversion ist eine Erweiterung.
Die Grundversion zählt nur die Versuche herunter, den ASCII-Galgen kann man als Erweiterung einbauen.

## Material
- `Programming_course_DayX_BlockY_{student,teacher}_version.ipynb`: die Notebooks pro Block
- `Aufgabensammlung_{student,teacher}_version.ipynb`: Zusatzaufgaben, u.a. die Themen, die es nicht mehr in den Kurs geschafft haben (2D-Listen, Rekursion, Effizienz, Sortieren, Binäre Suche, Sets, Permutationen, Filmbewertungen)
- `CoronaExample/`: optionales Material zu CSV-Dateien und Matplotlib
- `images/`: Bilder für die Notebooks. Sie werden in Colab über GitHub (raw-URL auf den Branch `2days`) eingebunden, damit sie auch ohne lokale Dateien angezeigt werden.

## Notebooks in Colab öffnen
`https://colab.research.google.com/github/Info-ag/ProgrammierkursPython/blob/2days/<Dateiname>.ipynb` \
Danach *Datei → Kopie in Drive speichern*, sonst gehen die Änderungen verloren.

## Zusatzinhalte (Ausblick am Ende)
1. Was ist der Unterschied zwischen .ipynb und .py Dateien? Was sind IDEs und wie installiere ich diese?
2. Python Libraries: numpy (große Datentabellen), pandas (csv Datentabellen einlesen), matplotlib (Diagramme/Plots)
3. git Versionsverwaltung
4. Typisierung von Variablen in Python


- laptops ersatz
- vorher da sein (Luan+ich eine Stunde vorher)
- seminarraum trennen
- mentoren gruppen, labbie gruppen trennen wie?
- colab oder jupyterhub? alles vorher fertig aufsetzen
