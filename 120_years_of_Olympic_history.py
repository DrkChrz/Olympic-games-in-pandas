import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
this method is making 2 spaces, helps make output more readable
"""
def make_space(num):
    for x in range(num):
        print()


"""
setting display options to see whole dataframe
"""
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 20)
#pd.set_option('display.max_rows', 100)

"""
reading '.csv' file into dataframe
"""
df = pd.read_csv("athlete_events.csv", encoding="UTF-8")
df_noc_regions = pd.read_csv("noc_regions.csv", encoding="UTF-8")

"""
finding unique regions in dataframe
"""
df_noc_regions = df_noc_regions["region"]
teams = pd.Series(df["Team"].unique())


"""
creating separate dataframes for summer and winter olympic games
"""
summer_olympics_df = df[df["Season"] == "Summer"]
winter_olympics_df = df[df["Season"] == "Winter"]

"""
sorting dataframes by year and extracting unique years in which olympics took place. Used for medals comparison
"""
summer_olympics_df = summer_olympics_df.sort_values("Year")
summer_olympics = pd.Series(summer_olympics_df["Year"].unique())

winter_olympics_df = winter_olympics_df.sort_values("Year")
winter_olympics = pd.Series(winter_olympics_df["Year"].unique())

"""
creating dataframes for different teams
"""
#Russia URS RUS
team = "USA"
#team  = "China"
team_olympic_df = df[df["NOC"] == "USA"]

#team_olympic_df = df[(df["NOC"] == "RUS") | (df["NOC"] == "URS")]
#team_olympic_df = df[df["Team"] == team]
"""
setting index to 'year', dropping 'ID' column and filling 'NA' values with '-', than soring dataframe by year
"""
team_olympic_df = team_olympic_df.set_index("Year")
team_olympic_df.drop(["ID"], axis=1, inplace=True)
team_olympic_df.fillna("-", inplace=True)
team_olympic_df.sort_values("Year", inplace=True)

#volleyball_players = df[(df["Sport"] == "Volleyball") & (df["NOC"] == "RUS") | (df["NOC"] == "URS")]
volleyball_players = df[(df["Sport"] == "Volleyball") & (df["NOC"] == "USA")]

"""
sorting volleyball players and grouping them by yea rand sex
"""
volleyball_players = volleyball_players.set_index("Year")
volleyball_players.drop(["ID"], axis=1, inplace=True)
volleyball_players.sort_values("Year", inplace=True)
volleyball_players_grouped = volleyball_players.groupby(["Year", "Sex"])

all_volleyball_df = df[df["Sport"] == "Volleyball"]
all_volleyball_df = all_volleyball_df.set_index("Year")
all_volleyball_df.drop(["ID"], axis=1, inplace=True)

all_volleyball_years = all_volleyball_df
all_volleyball_years.sort_values("Year", inplace=True)

all_volleyball_df_grouped = all_volleyball_df.groupby(["Year", "Sex"])

df_grouped_year_season = team_olympic_df.groupby(["Year", "Season"])


year_tab = df["Year"].unique()

year_tab_series = pd.Series(year_tab)
year_tab_series = year_tab_series.sort_values()
year_tab_df = year_tab_series.reset_index()
year_tab_df.drop(axis=1, labels="index", inplace=True)
year_tab_df.rename(columns={0: "Year"}, inplace=True)


make_space(2)

"""
initiating new dataframe to hold medals count for each year
"""
summer_olympics_performance = pd.DataFrame()

"""
initiating variables to count medals, initiating lists to keep medals count
"""
summer_gold_medals_men_count = 0
summer_silver_medals_men_count = 0
summer_bronze_medals_men_count = 0

summer_gold_medals_fem_count = 0
summer_silver_medals_fem_count = 0
summer_bronze_medals_fem_count = 0

summer_gold_medals_men_tab = []
summer_silver_medals_men_tab = []
summer_bronze_medals_men_tab = []

summer_gold_medals_fem_tab = []
summer_silver_medals_fem_tab = []
summer_bronze_medals_fem_tab = []

season_tab = []
summer_year_count = []

season = "Summer"

"""
summer olympics
iterating years to get each medal count for unique discipline
"""
for year in summer_olympics:
    try:
        summer_gold_medals_men = df_grouped_year_season.get_group((year, season))

        summer_gold_medals_men = summer_gold_medals_men[(summer_gold_medals_men["Sex"] == "M") & (summer_gold_medals_men["Medal"] == "Gold")][
            "Event"]
        summer_gold_medals_men_disciplines = summer_gold_medals_men.unique()
        summer_gold_medals_men_count = summer_gold_medals_men.nunique()
    except KeyError:
        summer_gold_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        summer_silver_medals_men = df_grouped_year_season.get_group((year, season))
        summer_silver_medals_men = summer_silver_medals_men[(summer_silver_medals_men["Sex"] == "M") & (
                summer_silver_medals_men["Medal"] == "Silver")]["Event"]
        summer_silver_medals_men_disciplines = summer_silver_medals_men.unique()
        summer_silver_medals_men_count = summer_silver_medals_men.nunique()

    except KeyError:
        summer_silver_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        summer_bronze_medals_men = df_grouped_year_season.get_group((year, season))
        summer_bronze_medals_men = summer_bronze_medals_men[(summer_bronze_medals_men["Sex"] == "M") & (summer_bronze_medals_men["Medal"] == "Bronze")][
        "Event"]
        summer_bronze_medals_men_disciplines = summer_bronze_medals_men.unique()
        summer_bronze_medals_men_count = summer_bronze_medals_men.nunique()
    except KeyError:
        summer_bronze_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        summer_gold_medals_fem = df_grouped_year_season.get_group((year, season))
        summer_gold_medals_fem = summer_gold_medals_fem[(summer_gold_medals_fem["Sex"] == "F") & (summer_gold_medals_fem["Medal"] == "Gold")]["Event"]
        summer_gold_medals_fem_disciplines = summer_gold_medals_fem.unique()
        summer_gold_medals_fem_count = summer_gold_medals_fem.nunique()
    except KeyError:
        summer_gold_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        summer_silver_medals_fem = df_grouped_year_season.get_group((year, season))
        summer_silver_medals_fem = summer_silver_medals_fem[(summer_silver_medals_fem["Sex"] == "F") & (summer_silver_medals_fem["Medal"] == "Silver")][
        "Event"]
        summer_silver_medals_fem_disciplines = summer_silver_medals_fem.unique()
        summer_silver_medals_fem_count = summer_silver_medals_fem.nunique()
    except KeyError:
        summer_silver_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        summer_bronze_medals_fem = df_grouped_year_season.get_group((year, season))
        summer_bronze_medals_fem = summer_bronze_medals_fem[(summer_bronze_medals_fem["Sex"] == "F") & (summer_bronze_medals_fem["Medal"] == "Bronze")][
        "Event"]
        summer_bronze_medals_fem_disciplines = summer_bronze_medals_fem.unique()
        summer_bronze_medals_fem_count = summer_bronze_medals_fem.nunique()
    except KeyError:
        summer_bronze_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    summer_gold_medals_men_tab.append(summer_gold_medals_men_count)
    summer_silver_medals_men_tab.append(summer_silver_medals_men_count)
    summer_bronze_medals_men_tab.append(summer_bronze_medals_men_count)

    summer_gold_medals_fem_tab.append(summer_gold_medals_fem_count)
    summer_silver_medals_fem_tab.append(summer_silver_medals_fem_count)
    summer_bronze_medals_fem_tab.append(summer_bronze_medals_fem_count)

    summer_year_count.append(year)

"""
filling dataframe with results
"""
summer_olympics_performance["Year"] = summer_year_count
summer_olympics_performance["Gold medals women"] = summer_gold_medals_fem_tab
summer_olympics_performance["Gold medals men"] = summer_gold_medals_men_tab
summer_olympics_performance["Silver medals women"] = summer_silver_medals_fem_tab
summer_olympics_performance["Silver medals men"] = summer_silver_medals_men_tab
summer_olympics_performance["Bronze medals women"] = summer_bronze_medals_fem_tab
summer_olympics_performance["Bronze medals men"] = summer_bronze_medals_men_tab
summer_olympics_performance["Total gold medals sum"] = summer_olympics_performance["Gold medals women"] + summer_olympics_performance["Gold medals men"]
summer_olympics_performance["Total silver medals sum"] = summer_olympics_performance["Silver medals women"] + summer_olympics_performance["Silver medals men"]
summer_olympics_performance["Total bronze medals sum"] = summer_olympics_performance["Bronze medals women"] + summer_olympics_performance["Bronze medals men"]
summer_olympics_performance["Total medals sum"] = summer_olympics_performance["Total gold medals sum"] + summer_olympics_performance["Total silver medals sum"] + summer_olympics_performance["Total bronze medals sum"]

summer_olympics_performance.set_index("Year", inplace=True)
#print(summer_olympics_performance)

"""
initiating new dataframe to hold medals count for each year
"""
winter_olympics_performance = pd.DataFrame()

"""
initiating variables to count medals, initiating lists to keep medals count
"""
winter_gold_medals_men_count = 0
winter_silver_medals_men_count = 0
winter_bronze_medals_men_count = 0

winter_gold_medals_fem_count = 0
winter_silver_medals_fem_count = 0
winter_bronze_medals_fem_count = 0

winter_gold_medals_men_tab = []
winter_silver_medals_men_tab = []
winter_bronze_medals_men_tab = []

winter_gold_medals_fem_tab = []
winter_silver_medals_fem_tab = []
winter_bronze_medals_fem_tab = []

season_tab = []
winter_year_count = []

season = "Winter"

"""
winter olympics
iterating years to get each medal count for unique discipline
"""
for year in winter_olympics:

    try:
        winter_gold_medals_men = df_grouped_year_season.get_group((year, season))

        winter_gold_medals_men = winter_gold_medals_men[(winter_gold_medals_men["Sex"] == "M") & (winter_gold_medals_men["Medal"] == "Gold")][
            "Event"]
        winter_gold_medals_men = pd.Series(winter_gold_medals_men.unique())
        winter_gold_medals_men_count = winter_gold_medals_men.count()

    except KeyError:
        winter_gold_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        winter_silver_medals_men = df_grouped_year_season.get_group((year, season))
        winter_silver_medals_men = winter_silver_medals_men[(winter_silver_medals_men["Sex"] == "M") & (
                winter_silver_medals_men["Medal"] == "Silver")]["Event"]
        winter_silver_medals_men = pd.Series(winter_silver_medals_men.unique())
        winter_silver_medals_men_count = winter_silver_medals_men.count()
    except KeyError:
        winter_silver_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        winter_bronze_medals_men = df_grouped_year_season.get_group((year, season))
        winter_bronze_medals_men = winter_bronze_medals_men[(winter_bronze_medals_men["Sex"] == "M") & (winter_bronze_medals_men["Medal"] == "Bronze")][
        "Event"]
        winter_bronze_medals_men = pd.Series(winter_bronze_medals_men.unique())
        winter_bronze_medals_men_count = winter_bronze_medals_men.count()
    except KeyError:
        winter_bronze_medals_men_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        winter_gold_medals_fem = df_grouped_year_season.get_group((year, season))
        winter_gold_medals_fem = winter_gold_medals_fem[(winter_gold_medals_fem["Sex"] == "F") & (winter_gold_medals_fem["Medal"] == "Gold")]["Event"]
        winter_gold_medals_fem = pd.Series(winter_gold_medals_fem.unique())
        winter_gold_medals_fem_count = winter_gold_medals_fem.count()
    except KeyError:
        winter_gold_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        winter_silver_medals_fem = df_grouped_year_season.get_group((year, season))
        winter_silver_medals_fem = winter_silver_medals_fem[(winter_silver_medals_fem["Sex"] == "F") & (winter_silver_medals_fem["Medal"] == "Silver")][
        "Event"]
        winter_silver_medals_fem = pd.Series(winter_silver_medals_fem.unique())
        winter_silver_medals_fem_count = winter_silver_medals_fem.count()
    except KeyError:
        winter_silver_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    try:
        winter_bronze_medals_fem = df_grouped_year_season.get_group((year, season))
        winter_bronze_medals_fem = winter_bronze_medals_fem[(winter_bronze_medals_fem["Sex"] == "F") & (winter_bronze_medals_fem["Medal"] == "Bronze")][
        "Event"]
        winter_bronze_medals_fem = pd.Series(winter_bronze_medals_fem.unique())
        winter_bronze_medals_fem_count = winter_bronze_medals_fem.count()
    except KeyError:
        winter_bronze_medals_fem_count = 0
    except Exception as e:
        print("Other exception", e)

    winter_gold_medals_men_tab.append(winter_gold_medals_men_count)
    winter_silver_medals_men_tab.append(winter_silver_medals_men_count)
    winter_bronze_medals_men_tab.append(winter_bronze_medals_men_count)

    winter_gold_medals_fem_tab.append(winter_gold_medals_fem_count)
    winter_silver_medals_fem_tab.append(winter_silver_medals_fem_count)
    winter_bronze_medals_fem_tab.append(winter_bronze_medals_fem_count)

    winter_year_count.append(year)

"""
filling dataframe with results
"""
winter_olympics_performance["Year"] = winter_year_count
winter_olympics_performance["Gold medals women"] = winter_gold_medals_fem_tab
winter_olympics_performance["Gold medals men"] = winter_gold_medals_men_tab
winter_olympics_performance["Silver medals women"] = winter_silver_medals_fem_tab
winter_olympics_performance["Silver medals men"] = winter_silver_medals_men_tab
winter_olympics_performance["Bronze medals women"] = winter_bronze_medals_fem_tab
winter_olympics_performance["Bronze medals men"] = winter_bronze_medals_men_tab
winter_olympics_performance["Total gold medals sum"] = winter_olympics_performance["Gold medals women"] + winter_olympics_performance["Gold medals men"]
winter_olympics_performance["Total silver medals sum"] = winter_olympics_performance["Silver medals women"] + winter_olympics_performance["Silver medals men"]
winter_olympics_performance["Total bronze medals sum"] = winter_olympics_performance["Bronze medals women"] + winter_olympics_performance["Bronze medals men"]
winter_olympics_performance["Total medals sum"] = winter_olympics_performance["Total gold medals sum"] + winter_olympics_performance["Total silver medals sum"] + winter_olympics_performance["Total bronze medals sum"]

"""
setting index to year
"""
winter_olympics_performance.set_index("Year", inplace=True)

"""
finding max medals count and corresponding year
"""
summer_total_medals_max = summer_olympics_performance["Total medals sum"].max()
summer_min_year = summer_olympics_performance.index.min()
summer_max_year = summer_olympics_performance.index.max()
year_max_total_medals = summer_olympics_performance["Total medals sum"].idxmax()
summer_max_total_medals = summer_olympics_performance.loc[year_max_total_medals, "Total medals sum"]

#print(winter_olympics_performance)

"""
ploting graphs
"""
fig, new = plt.subplots(nrows=3, ncols=2, figsize=(14, 7))
fig.tight_layout(pad=2)

new[0][0].plot(summer_olympics_performance["Total medals sum"], label=f"Summer olympics total medals {team}", marker="o", markersize=4, color="orange")
new[0][0].plot(winter_olympics_performance["Total medals sum"], label=f"Winter olympics total medals {team}", marker="o", markersize=4, color="blue")
new[0][0].legend(fontsize="small", loc="best")
new[0][0].grid(True)
new[0][0].set_yticks(np.arange(0, summer_total_medals_max, np.rint(summer_total_medals_max/5)))
new[0][0].set_xticks(np.arange(summer_min_year, summer_max_year+2, 8))
new[0][0].set_xlim([summer_min_year, summer_max_year+1])
new[0][0].set_ylim([0, summer_total_medals_max+summer_total_medals_max/10])
new[0][0].set_title("Total gold medals on summer and winter olympic games")

new[0][0].annotate(f"max medals - {summer_max_total_medals} in {year_max_total_medals}", xy=(year_max_total_medals, summer_max_total_medals), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_total_medals+10, summer_max_total_medals-summer_max_total_medals/3))

summer_gold_medals_fem_max = summer_olympics_performance["Gold medals women"].max()
summer_gold_medals_men_max = summer_olympics_performance["Gold medals men"].max()

year_max_gold_medals_women = summer_olympics_performance["Gold medals women"].idxmax()
year_max_gold_medals_men = summer_olympics_performance["Gold medals men"].idxmax()

summer_max_gold_medals_women = summer_olympics_performance.loc[year_max_gold_medals_women, "Gold medals women"]
summer_max_gold_medals_men = summer_olympics_performance.loc[year_max_gold_medals_men, "Gold medals men"]

new[0][1].plot(summer_olympics_performance["Gold medals women"], label=f"Summer olympics gold medals women {team}", marker="o", markersize=4, color="tab:red")
new[0][1].plot(summer_olympics_performance["Gold medals men"], label=f"Summer olympics gold medals men {team}", marker="o", markersize=4, color="tab:green")
new[0][1].legend(fontsize="small", loc="best")
new[0][1].grid(True)
new[0][1].set_yticks(np.arange(0, summer_max_gold_medals_men+1, np.rint(summer_max_gold_medals_men/5)))
new[0][1].set_xticks(np.arange(summer_min_year, summer_max_year+2, 8))
new[0][1].set_xlim([summer_min_year, summer_max_year+1])
new[0][1].set_ylim([0, summer_max_gold_medals_men+summer_max_gold_medals_men/10])
new[0][1].set_title("Men and women gold medals on summer olympic games")

new[0][1].annotate(f"max gold medals women - {summer_max_gold_medals_women} in {year_max_gold_medals_women}", xy=(year_max_gold_medals_women, summer_max_gold_medals_women), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_gold_medals_women+10, summer_max_gold_medals_women-summer_max_gold_medals_women/3))
new[0][1].annotate(f"max gold medals men - {summer_max_gold_medals_men} in {year_max_gold_medals_men}", xy=(year_max_gold_medals_men, summer_max_gold_medals_men), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_gold_medals_men+10, summer_max_gold_medals_men-summer_max_gold_medals_men/3))

summer_silver_medals_fem_max = summer_olympics_performance["Silver medals women"].max()
summer_silver_medals_men_max = summer_olympics_performance["Silver medals men"].max()

year_max_silver_medals_women = summer_olympics_performance["Silver medals women"].idxmax()
year_max_silver_medals_men = summer_olympics_performance["Silver medals men"].idxmax()

summer_max_silver_medals_women = summer_olympics_performance.loc[year_max_silver_medals_women, "Silver medals women"]
summer_max_silver_medals_men = summer_olympics_performance.loc[year_max_silver_medals_men, "Silver medals men"]

new[1][0].plot(summer_olympics_performance["Silver medals women"], label=f"Summer olympics silver medals women {team}", marker="o", markersize=4, color="tab:red")
new[1][0].plot(summer_olympics_performance["Silver medals men"], label=f"Summer olympics silver medals men {team}", marker="o", markersize=4, color="tab:green")
new[1][0].legend(fontsize="small", loc="best")
new[1][0].grid(True)
new[1][0].set_yticks(np.arange(0, summer_max_silver_medals_men, np.rint(summer_max_silver_medals_men/5)))
new[1][0].set_xticks(np.arange(summer_min_year, summer_max_year+2, 8))
new[1][0].set_xlim([summer_min_year, summer_max_year+1])
new[1][0].set_ylim([0, summer_max_silver_medals_men+summer_max_silver_medals_men/10])
new[1][0].set_title("Men and women silver medals on summer olympic games")

new[1][0].annotate(f"max silver medals women - {summer_max_silver_medals_women} in {year_max_silver_medals_women}", xy=(year_max_silver_medals_women, summer_max_silver_medals_women), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_silver_medals_women+10, summer_max_silver_medals_women-summer_max_silver_medals_women/3))
new[1][0].annotate(f"max silver medals men - {summer_max_silver_medals_men} in {year_max_silver_medals_men}", xy=(year_max_silver_medals_men, summer_max_silver_medals_men), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_silver_medals_men+10, summer_max_silver_medals_men-summer_max_silver_medals_men/3))

summer_bronze_medals_fem_max = summer_olympics_performance["Bronze medals women"].max()
summer_silver_medals_men_max = summer_olympics_performance["Bronze medals men"].max()

year_max_bronze_medals_women = summer_olympics_performance["Bronze medals women"].idxmax()
year_max_bronze_medals_men = summer_olympics_performance["Bronze medals men"].idxmax()

summer_max_bronze_medals_women = summer_olympics_performance.loc[year_max_bronze_medals_women, "Bronze medals women"]
summer_max_bronze_medals_men = summer_olympics_performance.loc[year_max_bronze_medals_men, "Bronze medals men"]

new[1][1].plot(summer_olympics_performance["Bronze medals women"], label=f"Summer olympics bronze medals women {team}", marker="o", markersize=4, color="tab:red")
new[1][1].plot(summer_olympics_performance["Bronze medals men"], label=f"Summer olympics bronze medals men {team}", marker="o", markersize=4, color="tab:green")
new[1][1].legend(fontsize="small", loc="best")
new[1][1].grid(True)
new[1][1].set_yticks(np.arange(0, summer_max_bronze_medals_men, np.rint(summer_max_bronze_medals_men/5)))
new[1][1].set_xticks(np.arange(summer_min_year, summer_max_year+2, 8))
new[1][1].set_xlim([summer_min_year, summer_max_year+1])
new[1][1].set_ylim([0, summer_max_bronze_medals_men+summer_max_bronze_medals_men/10])
new[1][1].set_title("Men and women bronze medals on summer olympic games")

new[1][1].annotate(f"max silver medals women - {summer_max_bronze_medals_women} in {year_max_bronze_medals_women}", xy=(year_max_bronze_medals_women, summer_max_bronze_medals_women), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_bronze_medals_women+10, summer_max_bronze_medals_women-summer_max_bronze_medals_women/3))
new[1][1].annotate(f"max silver medals men - {summer_max_bronze_medals_men} in {year_max_bronze_medals_men}", xy=(year_max_bronze_medals_men, summer_max_bronze_medals_men), horizontalalignment="center", arrowprops=dict(facecolor="black", arrowstyle="->"), xytext=(year_max_bronze_medals_men+10, summer_max_bronze_medals_men-summer_max_bronze_medals_men/3))

all_volleyball_years = pd.Series(all_volleyball_years.index.unique())
mean_men_volleyball_player = []
mean_women_volleyball_player = []

mean_volleyball_men_all = []
mean_volleyball_women_all = []

"""
iterating through years to get mean values for men and women"""
for year in all_volleyball_years:
    try:
        volleyball_men = volleyball_players_grouped.get_group((year, "M"))
        mean_men_volleyball_player.append(volleyball_men.mean())
    except KeyError:
        mean_men_volleyball_player.append(pd.Series([0, 0, 0]))
    except Exception as e:
        print("Other exception:", e)

    try:
        volleyball_women = volleyball_players_grouped.get_group((year, "F"))
        mean_women_volleyball_player.append(volleyball_women.mean())
    except KeyError:
        mean_women_volleyball_player.append(pd.Series([0, 0, 0]))
    except Exception as e:
        print("Other exception:", e)

    try:
        volleyball_men_all = all_volleyball_df_grouped.get_group((year, "M"))
        mean_volleyball_men_all.append(volleyball_men_all.mean())
    except KeyError:
        mean_volleyball_men_all.append(pd.Series([0, 0, 0]))
    except Exception as e:
        print("Other exception:", e)

    try:
        volleyball_women_all = all_volleyball_df_grouped.get_group((year, "F"))
        mean_volleyball_women_all.append(volleyball_women_all.mean())
    except KeyError:
        mean_volleyball_women_all.append(pd.Series([0, 0, 0]))
    except Exception as e:
        print("Other exception:", e)

"""
initiating lists to hold values
"""
men_volleyball_age = []
men_volleyball_height = []
men_volleyball_weight = []

women_volleyball_age = []
women_volleyball_height = []
women_volleyball_weight = []

all_men_volleyball_age = []
all_men_volleyball_height = []
all_men_volleyball_weight = []

all_women_volleyball_age = []
all_women_volleyball_height = []
all_women_volleyball_weight = []


for x in mean_men_volleyball_player:
    men_volleyball_age.append(np.round(x[0], decimals=2))
    men_volleyball_height.append(np.round(x[1], decimals=2))
    men_volleyball_weight.append(np.round(x[2], decimals=2))

for x in mean_women_volleyball_player:
    women_volleyball_age.append(np.round(x[0], decimals=2))
    women_volleyball_height.append(np.round(x[1], decimals=2))
    women_volleyball_weight.append(np.round(x[2], decimals=2))

for x in mean_volleyball_men_all:
    all_men_volleyball_age.append(np.round(x[0], decimals=2))
    all_men_volleyball_height.append(np.round(x[1], decimals=2))
    all_men_volleyball_weight.append(np.round(x[2], decimals=2))

for x in mean_volleyball_women_all:
    all_women_volleyball_age.append(np.round(x[0], decimals=2))
    all_women_volleyball_height.append(np.round(x[1], decimals=2))
    all_women_volleyball_weight.append(np.round(x[2], decimals=2))

volleyball_df = pd.DataFrame()
volleyball_df["Year"] = all_volleyball_years
volleyball_df["men_volleyball_age"] = men_volleyball_age
volleyball_df["men_volleyball_height"] = men_volleyball_height
volleyball_df["men_volleyball_weight"] = men_volleyball_weight

volleyball_df["women_volleyball_age"] = women_volleyball_age
volleyball_df["women_volleyball_height"] = women_volleyball_height
volleyball_df["women_volleyball_weight"] = women_volleyball_weight

volleyball_df["all_men_volleyball_age"] = all_men_volleyball_age
volleyball_df["all_men_volleyball_height"] = all_men_volleyball_height
volleyball_df["all_men_volleyball_weight"] = all_men_volleyball_weight

volleyball_df["all_women_volleyball_age"] = all_women_volleyball_age
volleyball_df["all_women_volleyball_height"] = all_women_volleyball_height
volleyball_df["all_women_volleyball_weight"] = all_women_volleyball_weight

volleyball_df = volleyball_df.set_index("Year")
#print(volleyball_df)
"""
plotting olympic volleybal mean height, age and weight
"""
new[2][0].plot(volleyball_df["men_volleyball_age"], label=f"{team} men avg age", marker="o", markersize=4, color="tab:red")
new[2][0].plot(volleyball_df["women_volleyball_age"], label=f"{team} women avg age", marker="o", markersize=4, color="tab:green")
new[2][0].plot(volleyball_df["all_men_volleyball_age"], label=f"All men avg age", marker="o", markersize=4, color="black")
new[2][0].plot(volleyball_df["all_women_volleyball_age"], label=f"All women avg age", marker="o", markersize=4, color="blue")

new[2][0].legend(fontsize="small", loc="best")
new[2][0].grid(True)
new[2][0].set_yticks(np.arange(21, 30+1, 1))
new[2][0].set_xticks(np.arange(volleyball_df.index.min(), volleyball_df.index.max()+2, 4))
new[2][0].set_xlim([volleyball_df.index.min()-2, volleyball_df.index.max()+2])
new[2][0].set_ylim([21, 30])
new[2][0].set_title("Olympic games volleyball avg age")


new[2][1].plot(volleyball_df["men_volleyball_height"], label=f"{team} men avg height", marker="o", markersize=4, color="tab:red")
new[2][1].plot(volleyball_df["women_volleyball_height"], label=f"{team} women avg height", marker="o", markersize=4, color="tab:green")
new[2][1].plot(volleyball_df["all_men_volleyball_height"], label=f"All men avg height", marker="o", markersize=4, color="black")
new[2][1].plot(volleyball_df["all_women_volleyball_height"], label=f"All women avg height", marker="o", markersize=4, color="blue")

new[2][1].legend(fontsize="small", loc="best")
new[2][1].grid(True)
new[2][1].set_yticks(np.arange(165, 205+2, 10))
new[2][1].set_xticks(np.arange(volleyball_df.index.min(), volleyball_df.index.max()+2, 4))
new[2][1].set_xlim([volleyball_df.index.min()-2, volleyball_df.index.max()+2])
new[2][1].set_ylim([165, 205])
new[2][1].set_title("Olympic games volleyball avg height")

plt.show()
