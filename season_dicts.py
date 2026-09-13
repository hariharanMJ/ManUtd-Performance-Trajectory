
season_data = [
    {"season":"2010-11", "position":1, "Manager":"Ferguson"},
    {"season":"2011-12", "position":2, "Manager":"Ferguson"},
    {"season":"2012-13", "position":1, "Manager":"Ferguson"},
    {"season":"2013-14", "position":7, "Manager":"Moyes"},
    {"season":"2014-15", "position":4, "Manager":"Van Gaal"},
    {"season":"2015-16", "position":5, "Manager":"Van Gaal"},
    {"season":"2016-17", "position":6, "Manager":"Mourinho"},
    {"season":"2017-18", "position":2, "Manager":"Mourinho"}
]

top4_finish = 0
outside_top4 = 0


for row in season_data:
    if row["position"] <= 4:
        top4_finish += 1
        

    else:
        outside_top4 += 1
        


def count_by_managers(season_data):
    manager_counts = {}
    for row in season_data:
        manager = row["Manager"]
        manager_counts[manager] = manager_counts.get(manager, 0) + 1
    return manager_counts
    
'''results = count_by_managers(season_data)
for manager, count in results.items():
        label = "season" if count == 1 else "seasons"
        print(f"{manager} : {count} {label}")'''

#Refactor count_by_managers function.
def count_by_field(season_data, field_name):
    field_counts = {}
    for row in season_data:
          field = row[field_name]
          field_counts[field] = field_counts.get(field, 0) + 1

    return field_counts

def print_counts(results, label):
     for key, count in results.items():
         unit = "season" if count == 1 else "seasons"
         print(f"{label} {key} : {count} {unit}")


manager_results = count_by_field(season_data, "Manager")

position_results = count_by_field(season_data, "position")


#Average Position Calculation
def average_position(season_data):
    season_counter = 0
    position_counter = 0
    for row in season_data:
         position_counter = position_counter + row["position"]
         season_counter = season_counter + 1 
    avg = position_counter / season_counter
    return avg


#top tier seasons
def top_tier_seasons(season_data, threshold = 4):
    top_seasons = []
    for row in season_data:
        if row["position"] <= threshold:
            top_seasons.append(row["season"])
    return top_seasons     
     


#importing functions elsewhere without spamming output.
if __name__ == "__main__":
    print(row["season"],":", row["position"])
    print(row["season"],":", row["position"])
    print("Top 4 Finish: ",top4_finish)
    print("Outside of top 4: ", outside_top4)
    print_counts(manager_results, "Manager")
    print_counts(position_results, "position")
    print(average_position(season_data))
    print(top_tier_seasons(season_data))
    print(top_tier_seasons(season_data,6))