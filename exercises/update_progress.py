#!/usr/bin/env python3

import sqlite3

def main():
    conn = sqlite3.connect("progress.db")
    cursor = conn.cursor()

    # List all (folder, exercise) pairs
    exercises_to_complete = [
        # 04_traits
        ("04_traits", "00_intro"),
        ("04_traits", "01_trait"),
        ("04_traits", "02_orphan_rule"),
        ("04_traits", "03_operator_overloading"),
        ("04_traits", "04_derive"),
    ]

    # Upsert statement using ON CONFLICT
    upsert_sql = """
    INSERT INTO open_exercises (chapter, exercise, solved)
    VALUES (?, ?, 1)
    ON CONFLICT(chapter, exercise)
    DO UPDATE SET solved = excluded.solved
    """

    # For each exercise in the list, upsert
    for folder_name, exercise_name in exercises_to_complete:
        cursor.execute(upsert_sql, (folder_name, exercise_name))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
