import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt

from database import get_history, get_stats

def show_statistics(history_only=False):
    rows = get_history()

    if not rows:
        print("\nNoch keine Trainings gespeichert.")
        return

    if history_only:
        print("\n" + "=" * 60)
        print("                 TRAININGSHISTORIE")
        print("=" * 60)

        current_workout = None

        for row in rows:
            workout_id, date, workout_type, notes, name, sets, reps, weight = row

            if workout_id != current_workout:
                current_workout = workout_id

                print(f"\n📅 {date} | {workout_type}")

                if notes:
                    print(f"📝 {notes}")

            if name:
                print(
                    f"   • {name}: "
                    f"{sets} Sätze × {reps} Wdh. × {weight:g} kg"
                )

        return

    stats = get_stats()

    print("\n" + "=" * 45)
    print("                 STATISTIKEN")
    print("=" * 45)

    print(f"🏋️ Trainings: {stats['workouts']}")
    print(f"💪 Übungen: {stats['exercises']}")
    print(f"📦 Gesamtvolumen: {stats['volume']:,.0f} kg")
    print(f"📊 Durchschnittliches Volumen/Training: "
          f"{stats['average_volume']:,.0f} kg")

    print("\n🔥 Übungen mit dem meisten Volumen:")

    for index, (name, volume) in enumerate(stats["top_exercises"], 1):
        print(f"{index}. {name}: {volume:,.0f} kg")

def create_charts():
    stats = get_stats()

    if not stats["daily_volume"]:
        print("\n❌ Noch nicht genug Daten für Diagramme.")
        return

    dates = [item[0] for item in stats["daily_volume"]]
    volumes = [item[1] for item in stats["daily_volume"]]

    Path("charts").mkdir(exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.bar(dates, volumes)
    plt.title("Trainingsvolumen pro Tag")
    plt.xlabel("Datum")
    plt.ylabel("Volumen in kg")
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = "charts/trainingsvolumen.png"
    plt.savefig(filename)
    plt.show()

    print(f"\n✅ Diagramm gespeichert: {filename}")
