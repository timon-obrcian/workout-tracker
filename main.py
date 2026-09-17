from datetime import datetime
from database import init_db, workout_exists_today
from workout import add_workout
from statistics import show_statistics, create_charts
from timer import start_timer
from gemini import analyze_with_gemini

def evening_check():
    """Ask for today's workout once the evening starts."""
    now = datetime.now()

    if now.hour >= 18 and not workout_exists_today():
        print("\n🌙 ABEND-CHECK")
        print("Du hast für heute noch kein Training eingetragen.")

        answer = input("Möchtest du dein heutiges Training jetzt eintragen? (j/n): ").lower()

        if answer == "j":
            add_workout()

def menu():
    while True:
        print("\n" + "=" * 45)
        print("       MY WORKOUT TRACKER")
        print("=" * 45)
        print("1. 🏋️ Training eintragen")
        print("2. 📋 Trainingshistorie")
        print("3. 📊 Statistiken")
        print("4. 📈 Diagramme erstellen")
        print("5. ⏱️ 3-Minuten-Timer")
        print("6. 🤖 Gemini-Analyse")
        print("0. ❌ Beenden")
        print("=" * 45)

        choice = input("Auswahl: ").strip()

        if choice == "1":
            add_workout()
        elif choice == "2":
            show_statistics(history_only=True)
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            create_charts()
        elif choice == "5":
            start_timer()
        elif choice == "6":
            analyze_with_gemini()
        elif choice == "0":
            print("\nBis zum nächsten Training! 💪")
            break
        else:
            print("❌ Ungültige Eingabe.")

if __name__ == "__main__":
    init_db()
    evening_check()
    menu()
