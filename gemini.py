import os

from database import get_ai_data

def analyze_with_gemini():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("\n❌ Kein Gemini API-Key gefunden.")
        print("Lege eine .env-Datei an und füge")
        print("GEMINI_API_KEY=DEIN_KEY")
        print("ein.")
        return

    data = get_ai_data()

    if not data:
        print("\n❌ Noch keine Trainingsdaten vorhanden.")
        return

    try:
        from google import genai

        client = genai.Client(api_key=api_key)

        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

        training_text = ""

        for row in data:
            date, workout_type, notes, name, sets, reps, weight = row

            training_text += (
                f"Datum: {date} | Art: {workout_type} | "
                f"Übung: {name} | Sätze: {sets} | "
                f"Wiederholungen: {reps} | Gewicht: {weight} kg | "
                f"Notiz: {notes or '-'}\n"
            )

        prompt = f"""
Du bist ein hilfreicher Trainingsdaten-Analyst.

Analysiere die folgenden Trainingsdaten sachlich.

Gib eine übersichtliche Analyse mit:
1. Trainingshäufigkeit
2. häufigsten Übungen
3. Entwicklung des Trainingsvolumens
4. auffälligen Veränderungen
5. möglichen Ideen für die zukünftige Trainingsplanung

Keine medizinischen Diagnosen.
Keine extremen Trainings- oder Ernährungsempfehlungen.
Schreibe verständlich auf Deutsch.

TRAININGSDATEN:
{training_text}
"""

        print("\n🤖 Gemini analysiert deine Trainingsdaten...")
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        print("\n" + "=" * 60)
        print("                  GEMINI-ANALYSE")
        print("=" * 60)
        print(response.text)

    except ImportError:
        print("\n❌ Das Paket 'google-genai' fehlt.")
        print("Installiere die Abhängigkeiten mit:")
        print("pip install -r requirements.txt")

    except Exception as error:
        print("\n❌ Fehler bei der Gemini-Anfrage:")
        print(error)
