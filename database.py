import sqlite3
from datetime import datetime
from pathlib import Path

DB_FILE = Path("workout.db")

def connect():
    return sqlite3.connect(DB_FILE)

def init_db():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            workout_type TEXT NOT NULL,
            notes TEXT,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            weight REAL DEFAULT 0,
            FOREIGN KEY (workout_id) REFERENCES workouts(id)
        )
    """)

    connection.commit()
    connection.close()

def add_workout_to_db(date, workout_type, notes, exercises):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO workouts (date, workout_type, notes, created_at)
        VALUES (?, ?, ?, ?)
    """, (date, workout_type, notes, datetime.now().isoformat()))

    workout_id = cursor.lastrowid

    for exercise in exercises:
        cursor.execute("""
            INSERT INTO exercises
            (workout_id, name, sets, reps, weight)
            VALUES (?, ?, ?, ?, ?)
        """, (
            workout_id,
            exercise["name"],
            exercise["sets"],
            exercise["reps"],
            exercise["weight"]
        ))

    connection.commit()
    connection.close()

def workout_exists_today():
    today = datetime.now().strftime("%Y-%m-%d")

    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM workouts WHERE date = ? LIMIT 1",
        (today,)
    )

    result = cursor.fetchone()
    connection.close()

    return result is not None

def get_history():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            w.id,
            w.date,
            w.workout_type,
            w.notes,
            e.name,
            e.sets,
            e.reps,
            e.weight
        FROM workouts w
        LEFT JOIN exercises e ON w.id = e.workout_id
        ORDER BY w.date DESC, w.id DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows

def get_stats():
    connection = connect()
    cursor = connection.cursor()

    queries = {
        "workouts": "SELECT COUNT(*) FROM workouts",
        "exercises": "SELECT COUNT(*) FROM exercises",
        "volume": """
            SELECT COALESCE(SUM(sets * reps * weight), 0)
            FROM exercises
        """,
        "average_volume": """
            SELECT COALESCE(AVG(workout_volume), 0)
            FROM (
                SELECT workout_id, SUM(sets * reps * weight) AS workout_volume
                FROM exercises
                GROUP BY workout_id
            )
        """
    }

    results = {}

    for name, query in queries.items():
        cursor.execute(query)
        results[name] = cursor.fetchone()[0]

    cursor.execute("""
        SELECT name, SUM(sets * reps * weight) AS volume
        FROM exercises
        GROUP BY name
        ORDER BY volume DESC
        LIMIT 5
    """)
    results["top_exercises"] = cursor.fetchall()

    cursor.execute("""
        SELECT date, SUM(sets * reps * weight) AS volume
        FROM workouts
        JOIN exercises ON workouts.id = exercises.workout_id
        GROUP BY date
        ORDER BY date
    """)
    results["daily_volume"] = cursor.fetchall()

    connection.close()
    return results

def get_ai_data():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            w.date,
            w.workout_type,
            w.notes,
            e.name,
            e.sets,
            e.reps,
            e.weight
        FROM workouts w
        LEFT JOIN exercises e ON w.id = e.workout_id
        ORDER BY w.date ASC
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows
