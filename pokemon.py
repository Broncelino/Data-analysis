import pandas as pd
df = pd.read_csv('./Pokemon.csv')
pd.set_option('display.max_rows', 20)
#print(df.columns)
#print(df['Name'][0:5]) just names of index 1-5
#print(df.iloc[1,2]) the second value in index 1
#print(df)

df['BST'] = df.iloc[:, 4:10].sum(axis=1) #adds another column called BST (Base stat total) that is the sum of columns 4-9 (4:10 is exclusive so 10 is not included) 

#average stats among all the pokemon
def avgStats():
    avgHP = 0
    avgATK = 0
    avgDEF = 0
    avgSPAT = 0
    avgSPDEF = 0
    avgSPD = 0
    count = 0
    for index, row in df.iterrows():
        avgHP += row['HP']
        avgATK += row['Attack']
        avgDEF += row['Defense']
        avgSPAT += row['Sp. Atk']
        avgSPDEF += row['Sp. Def']
        avgSPD += row['Speed']
        count += 1

    avgHP = round(avgHP / count,2)
    avgATK = round(avgATK / count,2)
    avgDEF = round(avgDEF / count,2)
    avgSPAT = round(avgSPAT / count,2)
    avgSPDEF = round(avgSPDEF / count,2)
    avgSPD = round(avgSPD / count,2)

    print(avgHP,avgATK,avgDEF,avgSPAT,avgSPDEF,avgSPD)
    print(round(df['HP'].mean(),2),round(df['Attack'].mean(),2),round(df['Defense'].mean(),2),round(df['Sp. Atk'].mean(),2),round(df['Sp. Def'].mean(),2),round(df['Speed'].mean(),2))#from 20 lines of code to 1

#displays number of legendaries per generation
def mostLegendaries():
    legendaries = {'gen1': 0, 'gen2': 0, 'gen3': 0, 'gen4': 0, 'gen5': 0, 'gen6': 0}
    for index, row in df.iterrows():
        if row['Legendary']:
            #print(row['Generation'])
            gen = 'gen' + str(row['Generation'])
            legendaries[gen] += 1
    print(legendaries)

#displays number of pokemon per generation
def mostpokemon():
    pokemon = {'gen1': 0, 'gen2': 0, 'gen3': 0, 'gen4': 0, 'gen5': 0, 'gen6': 0}
    for index, row in df.iterrows():
            #print(row['Generation'])
            gen = 'gen' + str(row['Generation'])
            pokemon[gen] += 1
    print(pokemon)

#displays the average BST for each type
def typeTotals():
    totals = {}
    for index, row in df.iterrows():
        if row['Type 1'] in totals:
            totals[row['Type 1']][0] += row['BST']
            totals[row['Type 1']][1] += 1
        else:
            totals[row['Type 1']] = [row['BST'],1]
        if row['Type 2'] in totals:
            totals[row['Type 2']][0] += row['BST']
            totals[row['Type 2']][1] += 1
        else:
            totals[row['Type 2']] = [row['BST'],1]
    for i in totals:
        avg = round(totals[i][0] / totals[i][1],1)
        print("{0} Type: {1}".format(i,avg))

#displays the average BST for each generation
def genTotals():
    totals = {}
    for index, row in df.iterrows():
        if row['Generation'] in totals:
            totals[row['Generation']][0] += row['BST']
            totals[row['Generation']][1] += 1
        else:
            totals[row['Generation']] = [row['BST'],1]
    for i in totals:
        avg = round(totals[i][0] / totals[i][1],1)
        print("Gen {0}: {1}".format(i,avg))

#print(df)
#avgStats()
#mostLegendaries()
#mostpokemon()
#typeTotals()
#genTotals()

print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Grass')])
#df['BST'] = df.iloc[:, 4:10].sum(axis=1)
#print(round(df['BST'].mean(),2))