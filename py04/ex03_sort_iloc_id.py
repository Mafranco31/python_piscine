def how_many_medals(df, name):
    id = df[df['Name'] == name]
    id.sort_values(by=['Year'])
    dict = {}
    for i in range(len(id)):
        if id.iloc[i]['Year'] not in dict:
            dict[id.iloc[i]['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if id.iloc[i]['Medal'] == 'Gold':
            dict[id.iloc[i]['Year']]['G']+= 1
        elif id.iloc[i]['Medal'] == 'Silver':
            dict[id.iloc[i]['Year']]['S'] += 1
        elif id.iloc[i]['Medal'] == 'Bronze':
            dict[id.iloc[i]['Year']]['B'] += 1
    return dict