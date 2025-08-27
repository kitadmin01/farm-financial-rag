#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('finbin_farm_data.db')
cursor = conn.cursor()

print("fm_guide table schema:")
cursor.execute('PRAGMA table_info(fm_guide)')
columns = cursor.fetchall()

for i, col in enumerate(columns):
    print(f"{i}: {col[1]} ({col[2]})")

print(f"\nTotal columns: {len(columns)}")

conn.close()
