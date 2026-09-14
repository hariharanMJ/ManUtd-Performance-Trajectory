#Pandas replaced my average_position and count_by_field and toptier_season functions in a one liner. Pandas combined
# with functions is really powerfull way to call the simpler pandas code everywhere.

import pandas as pd
df = pd.read_csv("manutd_seasons.csv")

print(df.head())
print(df.shape)
print(df.dtypes)

print(df["position"].mean())

top_tier = df[df["position"]<=4]

print(top_tier["season"].tolist())
print(df.groupby("manager").size())

sorted_df = df.sort_values("position", ascending=False)
print(sorted_df.head(1))
