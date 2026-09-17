# 🏋️ My Workout Tracker

Ein kleines Python-Projekt, mit dem ich meine Trainingsdaten speichern und auswerten kann.

## Funktionen

- täglicher Abend-Check
- Trainings speichern
- mehrere Übungen pro Training
- Sätze, Wiederholungen und Gewicht
- Notizen
- SQLite-Datenbank
- Trainingshistorie
- SQL-Abfragen für Statistiken
- Diagramme mit Matplotlib
- 3-Minuten-Pausentimer
- optionale Gemini-KI-Analyse

## Starten

### 1. Projekt herunterladen

Python 3 installieren und dieses Projekt öffnen.

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. Programm starten

```bash
python main.py
```

Beim ersten Start wird automatisch `workout.db` erstellt.

## Gemini einrichten

1. `.env.example` zu `.env` kopieren.
2. Deinen Gemini API-Key eintragen.
3. Niemals die `.env`-Datei auf GitHub hochladen.

Beispiel:

```text
GEMINI_API_KEY=dein_key
```

Der API-Key gehört nicht in den Python-Code.

## Abend-Check

Wenn das Programm nach 18:00 Uhr gestartet wird und noch kein Training für den aktuellen Tag gespeichert wurde, fragt das Programm, ob du dein Training eintragen möchtest.

Für eine echte automatische Erinnerung muss `main.py` zusätzlich über den Aufgabenplaner von Windows oder einen ähnlichen Scheduler jeden Abend gestartet werden.

## Datenbank

Das Projekt verwendet SQLite.

Tabellen:

- `workouts` – Datum, Trainingsart und Notizen
- `exercises` – Übung, Sätze, Wiederholungen und Gewicht

Dadurch kann man später weitere SQL-Abfragen hinzufügen.

## Projektstruktur

```text
workout_tracker/
│
├── main.py
├── database.py
├── workout.py
├── statistics.py
├── timer.py
├── gemini.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Idee für später

Mögliche Erweiterungen:

- persönliche Bestleistungen
- Push/Pull/Legs-Auswertung
- Wochen- und Monatsstatistiken
- Export als CSV
- eigene Weboberfläche
- Login
- Basketball-Statistiken
