from datetime import datetime
from database import add_workout_to_db

def get_number(text, allow_zero=False):
    while True:
        try:
            number = float(input(text))

            if number < 0 or (not allow_zero and number == 0):
                print("❌ Bitte eine gültige Zahl eingeben.")
                continue

            return number

        except ValueError:
            print("❌ Bitte nur Zahlen eingeben.")

def add_workout():
    print("\n" + "=" * 45)
    print("          TRAINING EINTRAGEN")
    print("=" * 45)

    date = datetime.now().strftime("%Y-%m-%d")

    print("\nTraining:")
    print("1. Gym")
    print("2. Basketball")
    print("3. Sonstiges")

    choice = input("Auswahl: ").strip()

    workout_types = {
        "1": "Gym",
        "2": "Basketball",
        "3": "Sonstiges"
    }

    workout_type = workout_types.get(choice, "Sonstiges")

    exercises = []

    print("\nJetzt kannst du deine Übungen eintragen.")
    print("Bei Körpergewichtsübungen einfach 0 kg eingeben.")

    while True:
        print("\n--- Neue Übung ---")

        name = input("Übung: ").strip()

        if not name:
            print("❌ Der Name darf nicht leer sein.")
            continue

        sets = int(get_number("Sätze: "))
        reps = int(get_number("Wiederholungen pro Satz: "))
        weight = get_number("Gewicht in kg (0 bei Körpergewicht): ", allow_zero=True)

        exercises.append({
            "name": name,
            "sets": sets,
            "reps": reps,
            "weight": weight
        })

        answer = input("\nNoch eine Übung? (j/n): ").lower()

        if answer != "j":
            break

    notes = input("\n📝 Notizen zum Training: ").strip()

    add_workout_to_db(
        date,
        workout_type,
        notes,
        exercises
    )

    print("\n✅ Training wurde gespeichert!")
    print(f"📅 Datum: {date}")
    print(f"🏷️ Art: {workout_type}")
    print(f"🏋️ Übungen: {len(exercises)}")

    if notes:
        print(f"📝 Notiz: {notes}")
