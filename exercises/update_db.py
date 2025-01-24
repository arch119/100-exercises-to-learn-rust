#!/usr/bin/env python3

import sqlite3

def main():
    conn = sqlite3.connect("progress.db")
    cursor = conn.cursor()

    # List all (folder, exercise) pairs
    exercises_to_complete = [
        # 01_intro
        ("01_intro", "00_welcome"),
        ("01_intro", "01_syntax"),
        
        # 02_basic_calculator
        ("02_basic_calculator", "00_intro"),
        ("02_basic_calculator", "01_integers"),
        ("02_basic_calculator", "02_variables"),
        ("02_basic_calculator", "03_if_else"),
        ("02_basic_calculator", "04_panics"),
        ("02_basic_calculator", "05_factorial"),
        ("02_basic_calculator", "06_while"),
        ("02_basic_calculator", "07_for"),
        ("02_basic_calculator", "08_overflow"),
        ("02_basic_calculator", "09_saturating"),
        ("02_basic_calculator", "10_as_casting"),

        # 03_ticket_v1
        ("03_ticket_v1", "00_intro"),
        ("03_ticket_v1", "01_struct"),
        ("03_ticket_v1", "02_validation"),
        ("03_ticket_v1", "03_modules"),
        ("03_ticket_v1", "04_visibility"),
        ("03_ticket_v1", "05_encapsulation"),
        ("03_ticket_v1", "06_ownership"),
        ("03_ticket_v1", "07_setters"),
        ("03_ticket_v1", "08_stack"),
        ("03_ticket_v1", "09_heap"),
        ("03_ticket_v1", "10_references_in_memory"),
        ("03_ticket_v1", "11_destructor"),
        ("03_ticket_v1", "12_outro"),
    ]

    # Upsert statement using ON CONFLICT
    upsert_sql = """
    INSERT INTO open_exercises (chapter, exercise, solved)
    VALUES (?, ?, 1)
    ON CONFLICT(chapter, exercise)
    DO UPDATE SET solved = excluded.solved
    """

    for chapter, exercise_name in exercises_to_complete:
        cursor.execute(upsert_sql, (chapter, exercise_name))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

