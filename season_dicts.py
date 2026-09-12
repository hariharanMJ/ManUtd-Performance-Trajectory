
season_data = [
    {"season":"2010-11", "position":"1", "Manager":"Ferguson"},
    {"season":"2011-12", "position":"2", "Manager":"Ferguson"},
    {"season":"2012-13", "position":"1", "Manager":"Ferguson"},
    {"season":"2013-14", "position":"7", "Manager":"Moyes"},
    {"season":"2014-15", "position":"4", "Manager":"Van Gaal"},
    {"season":"2015-16", "position":"5", "Manager":"Van Gaal"},
    {"season":"2016-17", "position":"6", "Manager":"Mourinho"},
    {"season":"2017-18", "position":"2", "Manager":"Mourinho"}
]

top4_finish = 0
outside_top4 = 0


for row in season_data:
    if row["position"] <= "4":
        top4_finish += 1
        print(row["season"],":", row["position"])

    else:
        outside_top4 += 1
        print(row["season"],":", row["position"])
print("Top 4 Finish: ",top4_finish)
print("Outside of top 4: ", outside_top4)

def count_by_managers(season_data):
    manager_counts = {}
    for row in season_data:
        manager = row["Manager"]
        manager_counts[manager] = manager_counts.get(manager, 0) + 1
        '''if manager in manager_counts:
            manager_counts[manager] = manager_counts[manager] + 1
        else:
            manager_counts[manager] = 1'''
    return manager_counts
    
results = count_by_managers(season_data)
for manager, count in results.items():
        label = "season" if count == 1 else "seasons"
        print(f"{manager} : {count} {label}")