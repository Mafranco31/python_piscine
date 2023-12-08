import pandas as pd

class Fileloader:
    def __init__(self):
        pass

    def load(self, path):
        if path.endswith(".csv"):
            df = pd.read_csv(path)
            print("test")
        elif path.endswith(".json"):
            df = pd.read_json(path)
        elif path.endswith(".xlsx"):
            df = pd.read_excel(path)
        elif path.endswith(".html"):
            df = pd.read_html(path)
        elif path.endswith(".xml"):
            df = pd.read_xml(path)
        else:
            print("Format accepted: csv, json, xlsx, html, xml")
            return None
        print("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1]))
        return df

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
        else:
            print("n must be a non-null integer")

from ex01_filter_get_value import youngest_fellah
from ex02_proportion_drop import proportion_by_sport
from ex03_sort_iloc_id import how_many_medals
from ex04_find_value_with_anther import SpatioTemporalData
from ex05_medals_per_country import how_many_medals_by_country
from ex06 import MyPlotLib
from ex07 import Komparator

if __name__ == "__main__":
    fl = Fileloader()
    data = fl.load("athlete_events.csv")
    print(youngest_fellah(data, 2004))
    print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
    print(how_many_medals(data, 'Kjetil Andr Aamodt'))
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
    mpl = MyPlotLib()
    #mpl.histogram(data[data['Sex']=='M'], 'Height')
    #mpl.histogram(data, ('Weight', 'Height'))
    #mpl.density(data, ('Weight', 'Height'))
    #mpl.pair_plot(data, ('Weight', 'Height'))
    #mpl.box_plot(data, ('Weight', 'Height', 'Age'))
    kp = Komparator(data)
    #kp.compare_box_plots('Sex', 'Weight')
    #kp.density('Sex', 'Weight')
    kp.compare_histograms('Sex', 'Weight')
    #print(how_many_medals_by_country(data, 'France'))
    #fl.display(data, 5)