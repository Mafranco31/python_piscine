def proportion_by_sport(df, year, sport, gender):
    new = df.drop_duplicates(subset=['ID'])
    filter1 = (new['Year'] == year) & (new['Sport'] == sport) & (new['Sex'] == gender)
    filter2 = (new['Year'] == year) & (new['Sex'] == gender)
    c1_count = new[filter1]['ID'].count()
    c2_count = new[filter2]['ID'].count()
    print(c1_count /c2_count)
    return 
