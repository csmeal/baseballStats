from pybaseball import batting_stats
import pandas as pd

# retrieve data on only players who have 35+ plate appearances this year
data = batting_stats(1900, qual=35)

# for key, val in data.items():
#     print(key)

df = pd.DataFrame(data)

total_df = df[df['H']==0]
print(total_df)

for year in range(2024, 1901, -1):
    # retrieve data on only players who have 50+ plate appearances this year
    data = batting_stats(year, qual=27)

    df = pd.DataFrame(data)
    filtered_df = df[df['H']==0]
    print(year)
    print(filtered_df.count())
    total_df = pd.concat([filtered_df, total_df])
total_df.to_csv('hitless_data.csv', index=False)


