"""Stellt den Inhalt fuer die JupyterLite-Seite zusammen.

Kopiert nur die Student-Versionen (keine Loesungen!) nach jupyterlite/content,
benennt sie kurz um und ersetzt die Colab-spezifischen Hinweise durch
JupyterLite-Hinweise. Die Notebooks im Repository bleiben unveraendert,
damit die Colab-Variante weiter funktioniert.

Aufruf (aus dem Repository-Root):  python jupyterlite/prepare_content.py
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "jupyterlite_teacher" / "content"

NOTEBOOKS = {
    "Programming_course_Day1_Block1_student_version.ipynb": "Tag1_Block1.ipynb",
    "Programming_course_Day1_Block2_student_version.ipynb": "Tag1_Block2.ipynb",
    "Programming_course_Day1_Block3_student_version.ipynb": "Tag1_Block3.ipynb",
    "Programming_course_Day1_Block4_student_version.ipynb": "Tag1_Block4.ipynb",
    "Programming_course_Day2_Block1_student_version.ipynb": "Tag2_Block1.ipynb",
    "Programming_course_Day2_Block2_student_version.ipynb": "Tag2_Block2.ipynb",
    "Programming_course_Day2_Block3_student_version.ipynb": "Tag2_Block3.ipynb",
    "Programming_course_Day2_Block4_student_version.ipynb": "Tag2_Block4.ipynb",
    "Aufgabensammlung_student_version.ipynb": "Zusatz_Aufgabensammlung.ipynb",
    "Programming_course_Day1_Block1_teacher_version.ipynb": "Tag1_Block1_teacher.ipynb",
    "Programming_course_Day1_Block2_teacher_version.ipynb": "Tag1_Block2_teacher.ipynb",
    "Programming_course_Day1_Block3_teacher_version.ipynb": "Tag1_Block3_teacher.ipynb",
    "Programming_course_Day1_Block4_teacher_version.ipynb": "Tag1_Block4_teacher.ipynb",
    "Programming_course_Day2_Block1_teacher_version.ipynb": "Tag2_Block1_teacher.ipynb",
    "Programming_course_Day2_Block2_teacher_version.ipynb": "Tag2_Block2_teacher.ipynb",
    "Programming_course_Day2_Block3_teacher_version.ipynb": "Tag2_Block3_teacher.ipynb",
    "Programming_course_Day2_Block4_teacher_version.ipynb": "Tag2_Block4_teacher.ipynb",
    "Aufgabensammlung_teacher_version.ipynb": "Zusatz_Aufgabensammlung_teacher.ipynb",
    "CoronaExample/COVID-19-Faelle_7-Tage-Inzidenz_Bundeslaender_withNames.csv": "CoronaExample/COVID-19-Faelle_7-Tage-Inzidenz_Bundeslaender_withNames.csv",
    "CoronaExample/COVID-19-Faelle_7-Tage-Inzidenz_Bundeslaender.csv": "CoronaExample/COVID-19-Faelle_7-Tage-Inzidenz_Bundeslaender.csv",
    "CoronaExample/COVID-19-Todesfaelle_Deutschland.csv": "CoronaExample/COVID-19-Todesfaelle_Deutschland.csv",
    "CoronaExample/csv.ipynb": "CoronaExample/csv.ipynb",
    "CoronaExample/matplotlib.ipynb": "CoronaExample/matplotlib.ipynb",
}

LITE_INTRO = [
    "## So funktioniert JupyterLite\n",
    "Python läuft hier direkt in eurem Browser, ihr braucht kein Konto.\n",
    "- Beim ersten Öffnen dauert es ein paar Sekunden, bis Python geladen ist (oben rechts steht dann *Python (Pyodide)* und der Kreis daneben ist leer).\n",
    "- Eine **Code-Zelle** führt ihr mit dem ▶-Knopf oben in der Werkzeugleiste oder mit `Shift + Enter` aus. Die Ausgabe erscheint direkt darunter.\n",
    "- Zellen bauen aufeinander auf: Eine Variable gibt es erst, nachdem die Zelle, in der sie definiert wird, ausgeführt wurde.\n",
    "  Wenn etwas komisch ist: *Kernel → Restart Kernel and Run All Cells*.\n",
    "- Wenn eine Zelle mit `input()` auf euch wartet, tippt eure Antwort in das Eingabefeld unter der Zelle und drückt `Enter`.\n",
    "- **Speichern:** mit `Strg + S` (passiert auch automatisch). Eure Änderungen werden **nur in diesem Browser auf diesem Computer** gespeichert.\n",
    "  Wenn ihr eure Lösungen mitnehmen wollt: *File → Download*.",
]

REPLACEMENTS = {
    "(in Colab mit dem ■-Knopf links neben der Zelle).": "(mit dem ■-Knopf oben in der Werkzeugleiste).",
    "Die **Aufgabensammlung** in diesem Repository": "Die **Aufgabensammlung** (`Zusatz_Aufgabensammlung.ipynb` hier in der Dateiliste)",
}

KERNELSPEC = {"display_name": "Python (Pyodide)", "language": "python", "name": "python"}


def convert(nb: dict) -> dict:
    for cell in nb["cells"]:
        src = cell.get("source", [])
        if isinstance(src, str):
            src = src.splitlines(keepends=True)
        if src and src[0].startswith("## So funktioniert Google Colab"):
            src = list(LITE_INTRO)
        new_src = []
        for line in src:
            for old, new in REPLACEMENTS.items():
                line = line.replace(old, new)
            new_src.append(line)
        cell["source"] = new_src
    nb.setdefault("metadata", {}).pop("colab", None)
    nb["metadata"]["kernelspec"] = KERNELSPEC
    return nb


def main() -> None:
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)
    for src_name, dst_name in NOTEBOOKS.items():
        source = ROOT / src_name
        destination = CONTENT / dst_name
        destination.parent.mkdir(parents=True, exist_ok=True)

        if source.suffix == ".ipynb":
            nb = json.loads(source.read_text(encoding="utf-8"))
            text = json.dumps(convert(nb), ensure_ascii=False, indent=1) + "\n"
            destination.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(source, destination)
        print(f"{src_name} -> content/{dst_name}")


if __name__ == "__main__":
    main()
