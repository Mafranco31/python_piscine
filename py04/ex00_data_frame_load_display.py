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

if __name__ == "__main__":
    fl = Fileloader()
    data = fl.load("athlete_events.csv")
    fl.display(data, 5)