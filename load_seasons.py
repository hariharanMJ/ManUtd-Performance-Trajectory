import csv
import json
from season_dicts import average_position, top_tier_seasons

with open("manutd_seasons.csv", "r") as file:
    reader = csv.DictReader(file)
    season_data = list(reader)
##print(type(season_data[0]["position"]))

for row in season_data:
    row["position"] = int(row["position"])
    row["manager"] =  row["manager"].strip()
    #print(type(row["position"]))

print(type(season_data[0]["position"]))

print(average_position(season_data))
print(top_tier_seasons(season_data))

with open("season_data.json", "w") as file:
    json.dump(season_data, file, indent=2)