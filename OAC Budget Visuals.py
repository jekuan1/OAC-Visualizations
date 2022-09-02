import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

ax = plt.figure().add_subplot(111)
ticklabels = [
    "August",
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
]

ax.set_xticks(np.arange(len(ticklabels)))
ax.set_xticklabels(ticklabels)

trip_profit = [197.09, 256, 70, 227.21, 144.65, 105, 436.42, 640.37, 107, 105, 0, 0]

party_net = [
    -38.2,
    1376.21,
    116.25,
    0,
    -326.46,
    -62,
    0,
    -381.43,
    -957.93,
    -484.17,
    0,
    0,
]

gear_purhcases = [0, -67, -781.6, -77.5, 0, 54, -37, -3220, 0, 0, -848, 0]

total = [
    6222.89,
    7788.1,
    7192.75,
    7342.46,
    7160.65,
    7257.65,
    7657.07,
    4696.01,
    3845.08,
    3465.91,
    2617.91,
    2617.91,
]

print(total)

ax.plot(trip_profit, color="green")
ax.plot(party_net, color="purple")
ax.plot(gear_purhcases, color="pink")
ax.plot(total, linewidth=5)
plt.title("Profits/Losses Each Month Aug 2021 - July 2022")

green_patch = mpatches.Patch(color="green", label="Trips")
purple_patch = mpatches.Patch(color="purple", label="Parties")
pink_patch = mpatches.Patch(color="pink", label="Gear")
blue_patch = mpatches.Patch(label="Total Balance")
ax.legend(handles=[green_patch, purple_patch, pink_patch, blue_patch])
# TODO ax.legend()

# revenue pie chart
fig1, ax1 = plt.subplots()
labels = (
    "Big Trips",
    "Trips",
    "Parties",
    "Shirts + 1 Pack sold",
)  # some shirts/pack selling
revenue = [19390, 12346.5, 2202.25, 902]
ax1.pie(revenue, labels=labels, autopct="%1.1f%%", startangle=90, pctdistance=0.8)
ax1.axis("equal")
plt.title("Percentage Breakdown\nof OAC Revenue", loc="left")

# expenses pie chart
fig2, ax2 = plt.subplots()
labels2 = "Big Trips", "Trips", "Parties", "Gear", "Philanthropy", "Shirts", "Murphys"
expenses = [18573.4, 10874.36, 1100.59, 963.1, 1500, 1720, 1859.39]
ax2.pie(expenses, labels=labels2, autopct="%1.1f%%", startangle=90, pctdistance=0.8)
ax2.axis("equal")
plt.title("Percentage Breakdown\nof OAC Expenses", loc="left")

# stacked bar chart

labels = "Revenue", "Expenses"
big_trips = 19390, 18573.4
trips = 12346.5, 10874.36
parties = 2202.25, 1100.59
shirts = 848, 1720
other = 54, 0  # pack
gear = 0, 963.1
philanthropy = 0, 1500
murphys = 0, 1859.39

fig3, ax3 = plt.subplots()

ax3.bar(labels, big_trips, label="Big Trips")
ax3.bar(labels, trips, label="Trips", bottom=big_trips)
ax3.bar(labels, parties, label="Parties", bottom=np.array(big_trips) + np.array(trips))
ax3.bar(
    labels,
    shirts,
    label="Shirts",
    bottom=np.array(big_trips) + np.array(trips) + np.array(parties),
)
ax3.bar(
    labels,
    philanthropy,
    label="Philanthropy",
    bottom=np.array(big_trips) + np.array(trips) + np.array(parties) + np.array(shirts),
)
ax3.bar(
    labels,
    other,
    label="Other",
    bottom=np.array(big_trips)
    + np.array(trips)
    + np.array(parties)
    + np.array(shirts)
    + np.array(philanthropy),
)
ax3.bar(
    labels,
    gear,
    label="Gear",
    bottom=np.array(big_trips)
    + np.array(trips)
    + np.array(parties)
    + np.array(shirts)
    + np.array(philanthropy)
    + np.array(other),
)

ax3.bar(
    labels,
    murphys,
    label="Murphys",
    bottom=np.array(big_trips)
    + np.array(trips)
    + np.array(parties)
    + np.array(shirts)
    + np.array(philanthropy)
    + np.array(other)
    + np.array(gear),
)
ax3.set_ylabel("$$$")
ax3.set_title("Revenue and Expenses Bar Chart")
ax3.legend()


# TODO separate cost of murphys


plt.show()
