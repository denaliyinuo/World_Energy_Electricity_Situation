import pandas as pd
import matplotlib.pyplot as plt

file = '/Users/nathanoliver/Desktop/World_Energy.csv'
data = pd.read_csv(file)
df = pd.DataFrame(data)

file = '/Users/nathanoliver/Desktop/World_Energy_2019.csv'
data = pd.read_csv(file)
df2019 = pd.DataFrame(data)

df = df.fillna(0)
df2019 = df2019.fillna(0)
pd.set_option('display.max_columns',100)

df_2019 = df.copy()

df_2019 = df_2019[df_2019['Year'] == 2019]
def string_creator(lst,string):
    col = []
    for i in lst:
        str1 = i + string
        col.append(str1)
    return col

lst_elect = ['Coal','Gas','Oil','Hydro','Nuclear','Wind','Solar','Other Renewables']

lst_energy = ['Coal','Gas','Oil','Hydro','Nuclear','Wind','Solar','Biofuels','Other']

a, b=[plt.cm.Reds, plt.cm.Greens]

colors_elect = [b(0.9), b(0.75), b(0.6), b(0.45), b(0.3),a(0.8), a(0.6), a(0.4)]
colors_elect = colors_elect[::-1]

colors_energy = [b(0.9), b(0.75), b(0.60), b(0.45), b(0.30), b(0.15),a(0.8), a(0.6), a(0.4)]
colors_energy = colors_energy[::-1]
def energy_graph(entity):
    filt = df['Year'] >= 1985
    df_1985 = df[filt]

    filt = (df_1985['Entity'] == entity)
    df_1985_new = df_1985[filt]

    string = ' Energy Share (%)'

    col = string_creator(lst_energy,string)

    fig = plt.figure(figsize = (15, 10))

    leg_tags = []
    colors = []
    tract = []
    j = 0

    for i in col:
        if df_1985_new[i].sum() == 0:
            pass
        else:
            leg_tags.append(lst_energy[j])
            colors.append(colors_energy[j])
            tract.append(df_1985_new[i]*100)
        j = j + 1

    a, b=[plt.cm.Reds, plt.cm.Greens]

    tract = tract[::-1]
    colors = colors[::-1]
    leg_tags = leg_tags[::-1]

    plt.stackplot(df_1985_new['Year'],tract*100,colors=colors)
    plt.xlim(1985,2019)
    plt.ylim(0,100)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel('Year',size=15)
    plt.ylabel('Energy Share (%)',size=15)
    plt.title(entity+'\nEnergy Consumption Share (%) by Energy Source',size=20)
    plt.legend(leg_tags, prop={"size":13},loc='upper left')
    return plt.show()
def elect_graph_share(entity):
    filt = df['Year'] >= 1985
    df_1985 = df[filt]

    filt = (df_1985['Entity'] == entity)
    df_1985_new = df_1985[filt]

    string = ' Electricity Share (%)'

    col = string_creator(lst_elect,string)

    fig = plt.figure(figsize = (15, 10))

    leg_tags = []
    colors = []
    tract = []
    j = 0

    for i in col:
        if df_1985_new[i].sum() == 0:
            pass
        else:
            leg_tags.append(lst_elect[j])
            colors.append(colors_elect[j])
            tract.append(df_1985_new[i])
        j = j + 1

    tract = tract[::-1]
    colors = colors[::-1]
    leg_tags = leg_tags[::-1]

    plt.stackplot(df_1985_new['Year'],tract,colors=colors)
    plt.xlim(1985,2019)
    plt.ylim(0,100)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel('Year',size=15)
    plt.ylabel('Electricity Generated (TWh)',size=15)
    plt.title(entity+'\nElectricity Generation Share (%) by Energy Source',size=20)
    plt.legend(leg_tags, prop={"size":13},loc='upper left')
    return plt.show()
def elect_graph(entity):
    filt = df['Year'] >= 1985
    df_1985 = df[filt]

    filt = (df_1985['Entity'] == entity)
    df_1985_new = df_1985[filt]

    string = ' Electricity Share (%)'

    col = string_creator(lst_elect,string)

    fig = plt.figure(figsize = (15, 10))

    leg_tags = []
    colors = []
    tract = []
    j = 0

    for i in col:
        if df_1985_new[i].sum() == 0:
            pass
        else:
            leg_tags.append(lst_elect[j])
            colors.append(colors_elect[j])
            tract.append(df_1985_new[i]*100)
        j = j + 1

    a, b=[plt.cm.Reds, plt.cm.Greens]

    tract = tract[::-1]
    colors = colors[::-1]
    leg_tags = leg_tags[::-1]

    plt.stackplot(df_1985_new['Year'],tract*100,colors=colors)
    plt.xlim(1985,2019)
    plt.ylim(0,100)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel('Year',size=15)
    plt.ylabel('Electricity Share (%)',size=15)
    plt.title(entity+'\nElectricity Generation Share (%) by Energy Source',size=20)
    plt.legend(leg_tags, prop={"size":13},loc='upper left')
    return plt.show()
print(elect_graph('World'))
plt.show()

None
print(energy_graph('World'))
plt.show()

None
comp_col = ['United States','Europe','China']

for col in comp_col:
    print(elect_graph(col))
    plt.show()

    print(energy_graph(col))
    plt.show()

None

None

None

None

None

None
drop_val = ['Africa','Europe','North America','World']

for i in drop_val:
    df_2019 = df_2019[df_2019['Entity'] != i]
filt = df['Year'] >= 1985
df_1985 = df[filt]

filt = (df_1985['Entity'] == 'Costa Rica')
df_1985 = df_1985[filt]

string = ' Electricity Share (%)'

col = string_creator(lst_elect,string)

fig = plt.figure(figsize = (15, 10))

blah = ['Other Renewables','Solar','Wind','Nuclear','Hydro','Oil','Gas','Coal']

a, b=[plt.cm.Reds, plt.cm.Greens]

plt.stackplot(df_1985['Year'],df_1985[col[7]]*100,df_1985[col[6]]*100,df_1985[col[5]]*100,df_1985[col[4]]*100,df_1985[col[3]],df_1985[col[2]],df_1985[col[1]],df_1985[col[0]],colors=[b(0.7), b(0.6), b(0.5), b(0.4), b(0.3), b(0.2),a(0.5), a(0.4), a(0.3)])
plt.xlim(1985,2019)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel('Year',size=15)
plt.ylabel('Electricity Generated (TWh)',size=15)
plt.title('World Electrical Grid Energy Source',size=20)
plt.title('Global Electricity Generation (TWh) by Energy Source',size=20)
plt.legend(blah, prop={"size":13},loc='upper left')
plt.show()

drop_val = ['Africa','Europe','North America','World']

for i in drop_val:
    df = df[df['Entity'] != i]
fig = plt.figure(figsize = (15, 10))

place = df_2019.sort_values('Total Energy',ascending=False)

x = place[:10]

other = x['Other Energy Share (%)']*100
biofuels = x['Biofuels Energy Share (%)']*100
solar = x['Solar Energy Share (%)']*100
wind = x['Wind Energy Share (%)']*100
hydro = x['Hydro Energy Share (%)']*100
nuclear = x['Nuclear Energy Share (%)']*100
oil = x['Oil Energy Share (%)']*100
gas = x['Gas Energy Share (%)']*100
coal = x['Coal Energy Share (%)']*100

y = x['Total Energy']/x['Total Energy'].max()

t1 = other
t2 = other + biofuels
t3 = other + biofuels + solar
t4 = other + biofuels + solar + wind
t5 = other + biofuels + solar + wind + hydro
t6 = other + biofuels + solar + wind + hydro + nuclear
t7 = other + biofuels + solar + wind + hydro + nuclear + oil
t8 = other + biofuels + solar + wind + hydro + nuclear + oil + gas

plt.bar(x['Entity'],other,color=colors_energy[8])
plt.bar(x['Entity'],biofuels,bottom=t1,color=colors_energy[7])
plt.bar(x['Entity'],solar,bottom=t2,color=colors_energy[6])
plt.bar(x['Entity'],wind,bottom=t3,color=colors_energy[5])
plt.bar(x['Entity'],hydro,bottom=t4,color=colors_energy[4])
plt.bar(x['Entity'],nuclear,bottom=t5,color=colors_energy[3])
plt.bar(x['Entity'],oil,bottom=t6,color=colors_energy[2])
plt.bar(x['Entity'],gas,bottom=t7,color=colors_energy[1])
plt.bar(x['Entity'],coal,bottom=t8,color=colors_energy[0])
# plt.plot(x['Entity'],y,color='black')

plt.legend(('Other','Biofuels','Solar','Wind','Hydro','Nuclear','Oil','Gas','Coal'),loc=(0.9,0.5),prop={'size': 12})

plt.title('Top 10 Energy Consuming Countries\nEnergy Source Breakdown',fontsize=20)
plt.ylabel('Percentage (%)',size=15)
plt.ylim(0,100)
plt.xticks(size=13)
plt.yticks(size=13)
plt.show()

fig = plt.figure(figsize = (15, 10))

place = df_2019.sort_values('Total Sustainable Energy Share (%)',ascending=False)

x = place[:10]

other = x['Other Energy Share (%)']*100
biofuels = x['Biofuels Energy Share (%)']*100
solar = x['Solar Energy Share (%)']*100
wind = x['Wind Energy Share (%)']*100
hydro = x['Hydro Energy Share (%)']*100
nuclear = x['Nuclear Energy Share (%)']*100
oil = x['Oil Energy Share (%)']*100
gas = x['Gas Energy Share (%)']*100
coal = x['Coal Energy Share (%)']*100

y = x['Total Energy']/x['Total Energy'].max()

t1 = other
t2 = other + biofuels
t3 = other + biofuels + solar
t4 = other + biofuels + solar + wind
t5 = other + biofuels + solar + wind + hydro
t6 = other + biofuels + solar + wind + hydro + nuclear
t7 = other + biofuels + solar + wind + hydro + nuclear + oil
t8 = other + biofuels + solar + wind + hydro + nuclear + oil + gas

plt.bar(x['Entity'],other,color=colors_energy[8])
plt.bar(x['Entity'],biofuels,bottom=t1,color=colors_energy[7])
plt.bar(x['Entity'],solar,bottom=t2,color=colors_energy[6])
plt.bar(x['Entity'],wind,bottom=t3,color=colors_energy[5])
plt.bar(x['Entity'],hydro,bottom=t4,color=colors_energy[4])
plt.bar(x['Entity'],nuclear,bottom=t5,color=colors_energy[3])
plt.bar(x['Entity'],oil,bottom=t6,color=colors_energy[2])
plt.bar(x['Entity'],gas,bottom=t7,color=colors_energy[1])
plt.bar(x['Entity'],coal,bottom=t8,color=colors_energy[0])
# plt.plot(x['Entity'],y,color='black')

plt.legend(('Other','Biofuels','Solar','Wind','Hydro','Nuclear','Oil','Gas','Coal'),loc=(0.9,0.5),prop={'size': 12})

plt.title('Top 10 Countries with the Highest Energy Share from Renewables and Nuclear\nEnergy Source Breakdown',fontsize=20)
plt.ylabel('Percentage (%)',size=15)
plt.ylim(0,100)
plt.xticks(size=13)
plt.yticks(size=13)
plt.show()

fig = plt.figure(figsize = (15, 10))

df_1985 = df[df['Year'] >= 1985]

cou = ['China','United States','Japan','Canada','Germany','Brazil','Iran']

for i in range(len(cou)):
    x1 = df_1985[df_1985['Entity'] == cou[i]]
    plt.plot(x1['Year'],x1['Total Sustainable Energy Share (%)']*100)
plt.legend(cou)
plt.show()

print(energy_graph('Switzerland'))
plt.show()

None
print(energy_graph('China'))
plt.show()

None
con = ['Africa','Asia','Europe','Oceania','North America','South America']

con2019 = []

for i in con:
    con2019.append(i+'2019')

con2019 = sorted(con2019)
print(con2019)
['Africa2019', 'Asia2019', 'Europe2019', 'North America2019', 'Oceania2019', 'South America2019']
x = df2019[df2019['Merge'].isin(con2019)]
fig = plt.figure(figsize = (15, 10))

x = df2019[df2019['Merge'].isin(con2019)]



other = x['Other Energy Share (%)']*100
biofuels = x['Biofuels Energy Share (%)']*100
solar = x['Solar Energy Share (%)']*100
wind = x['Wind Energy Share (%)']*100
hydro = x['Hydro Energy Share (%)']*100
nuclear = x['Nuclear Energy Share (%)']*100
oil = x['Oil Energy Share (%)']*100
gas = x['Gas Energy Share (%)']*100
coal = x['Coal Energy Share (%)']*100

# y = x['Total Energy']/x['Total Energy'].max()

t1 = other
t2 = other + biofuels
t3 = other + biofuels + solar
t4 = other + biofuels + solar + wind
t5 = other + biofuels + solar + wind + hydro
t6 = other + biofuels + solar + wind + hydro + nuclear
t7 = other + biofuels + solar + wind + hydro + nuclear + oil
t8 = other + biofuels + solar + wind + hydro + nuclear + oil + gas

plt.bar(x['Entity'],other,color=colors_energy[8])
plt.bar(x['Entity'],biofuels,bottom=t1,color=colors_energy[7])
plt.bar(x['Entity'],solar,bottom=t2,color=colors_energy[6])
plt.bar(x['Entity'],wind,bottom=t3,color=colors_energy[5])
plt.bar(x['Entity'],hydro,bottom=t4,color=colors_energy[4])
plt.bar(x['Entity'],nuclear,bottom=t5,color=colors_energy[3])
plt.bar(x['Entity'],oil,bottom=t6,color=colors_energy[2])
plt.bar(x['Entity'],gas,bottom=t7,color=colors_energy[1])
plt.bar(x['Entity'],coal,bottom=t8,color=colors_energy[0])
# plt.plot(x['Entity'],y,color='black')

plt.legend(('Other','Biofuels','Solar','Wind','Hydro','Nuclear','Oil','Gas','Coal'),loc='upper right',prop={'size': 12})

plt.title('Continent Energy Source Breakdown',fontsize=20)
plt.ylabel('Percentage (%)',size=15)
plt.ylim(0,100)
plt.xticks(size=13)
plt.yticks(size=13)
plt.show()
