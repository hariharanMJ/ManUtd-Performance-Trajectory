import sqlite3
import csv

conn = sqlite3.connect("manutd.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS seasons(
        season TEXT,
        position INTEGER,
        manager TEXT
    )
""")
conn.commit()

with open("manutd_seasons.csv", "r") as file:
    reader = csv.DictReader(file)
    season_data = list(reader)

'''for row in season_data:
    cursor.execute("INSERT INTO seasons(season, position, manager) Values(?, ?, ?)",
    (row["season"], int(row["position"]), row["manager"]))

conn.commit()'''

cursor.execute("SELECT * FROM seasons")
results = cursor.fetchall()
for row in results:
    print(row)

print(f"Total records:  {len(results)}")

cursor.execute("SELECT * FROM seasons where position<=4")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM seasons ORDER BY position ASC")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM seasons ORDER BY position DESC LIMIT 1")
for row in cursor.fetchall():
    print(row)