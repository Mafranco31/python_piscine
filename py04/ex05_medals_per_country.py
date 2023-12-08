def how_many_medals_by_country(df, country):
    id = df[df['Team'] == country]
    id.sort_values(by=['Year'])
    dict = {}
    event = {}
    for i in range(len(id)):
        if id.iloc[i]['Year'] not in dict:
            dict[id.iloc[i]['Year']] = {'G': 0, 'S': 0, 'B': 0}
            event[id.iloc[i]['Year']] = {id.iloc[i]['Year']: 0}
        if id.iloc[i]['Event'] not in event[id.iloc[i]['Year']]:
            event[id.iloc[i]['Year']][id.iloc[i]['Event']] = {'G': 0, 'S': 0, 'B': 0}
        if id.iloc[i]['Medal'] == 'Gold':
            if event[id.iloc[i]['Year']][id.iloc[i]['Event']]['G'] == 0:
                dict[id.iloc[i]['Year']]['G']+= 1
                event[id.iloc[i]['Year']][id.iloc[i]['Event']]['G'] = 1
        elif id.iloc[i]['Medal'] == 'Silver':
            if event[id.iloc[i]['Year']][id.iloc[i]['Event']]['S'] == 0:
                dict[id.iloc[i]['Year']]['S'] += 1
                event[id.iloc[i]['Year']][id.iloc[i]['Event']]['S'] = 1
        elif id.iloc[i]['Medal'] == 'Bronze':
            if event[id.iloc[i]['Year']][id.iloc[i]['Event']]['B'] == 0:
                dict[id.iloc[i]['Year']]['B'] += 1
                event[id.iloc[i]['Year']][id.iloc[i]['Event']]['B'] = 1
    return dict