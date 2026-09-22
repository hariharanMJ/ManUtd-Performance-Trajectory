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



cursor.execute("SELECT COUNT(*) FROM seasons")
total_season = cursor.fetchone()[0]

cursor.execute("SELECT AVG(position) FROM seasons")
avg_pos = cursor.fetchone()[0]

cursor.execute("SELECT MIN(position) FROM seasons")
min_pos = cursor.fetchone()[0]

cursor.execute("SELECT MAX(position) FROM seasons")
max_pos = cursor.fetchone()[0]

if __name__ == "__main__":
    cursor.execute("SELECT * FROM seasons")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.execute("SELECT * FROM seasons where position<=4")
    for top_4_seasons in cursor.fetchall():
        print(top_4_seasons)

    cursor.execute("SELECT * FROM seasons ORDER BY position ASC")
    for best_seasons in cursor.fetchall():
        print(best_seasons)

    cursor.execute("SELECT * FROM seasons ORDER BY position DESC LIMIT 1")
    for worst_season in cursor.fetchall():
        print(worst_season)
    print(f"Total records:  {len(results)}")
    print(avg_pos)
    print(min_pos)
    print(max_pos)

