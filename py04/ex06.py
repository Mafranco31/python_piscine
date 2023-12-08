import matplotlib.pyplot as plt
import pandas as pd
import scipy

class MyPlotLib:
    def histogram(self, data, features):
        if isinstance(features, str):
            data[features].hist()
            plt.title(features)
            plt.show()
        elif isinstance(features, list) or isinstance(features, tuple):
            for i in features:
                data[i].hist()
                plt.title(i)
                plt.show()
        else:
            print("Format not accepted for histogram")
        return
    def density(self, data, features):
        if isinstance(features, str):
            data[features].plot.density()
            plt.title(features)
            plt.show()
        elif isinstance(features, list) or isinstance(features, tuple):
            for i in features:
                data[i].plot.density(x=i)
            plt.legend()
            plt.title(features)
            plt.show()
        else:
            print("Format not accepter for density plot")
        return
    def pair_plot(self, data, features):
        df = data.loc[:, features]          # [:, features] --> : mean all rows, features mean all features columns
        if isinstance(features, tuple):
            pd.plotting.scatter_matrix(df)
            plt.show()
        else:
            print("Pair plot needs a tuple of features")
        return 
    def box_plot(self, data, features):
        #df = data.loc[:, features]
        #df.boxplot()
        data.boxplot(column=list(features))
        plt.show()
        return 