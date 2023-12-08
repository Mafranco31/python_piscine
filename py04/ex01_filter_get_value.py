def youngest_fellah(data, year):
    """
    Return the youngest fellah in the given year.
    """
    filter1 = data['Year'] == year
    filter2 = data['Sex'] == 'F'
    filter3 = data['Sex'] == 'M'
    ret = {'f': data[filter1 & filter2]['Age'].min(), 'm': data[filter1 & filter3]['Age'].min()}
    return ret