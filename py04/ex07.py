import matplotlib.pyplot as plt
import pandas as pd
import scipy

class Komparator():
    def __init__(self, data):
        self.data = data
    
    def compare_box_plots(self, categorical_var, numerical_var):
        df = self.data.loc[:, (numerical_var, categorical_var)]
        df.boxplot(column=numerical_var, by=categorical_var)
        plt.show()

    def density(self, categorical_var, numerical_var):
        df = self.data.loc[:, (numerical_var, categorical_var)]
        for i in df[categorical_var].unique():
            temp = df[df[categorical_var] == i]
            temp[numerical_var].plot.density(label=f"{numerical_var} for {categorical_var} = {i}")
        plt.legend()
        plt.show()
    
    def compare_histograms(self, categorical_var, numerical_var):
        df = self.data.loc[:, (numerical_var, categorical_var)]
        for i in df[categorical_var].unique():
            temp = df[df[categorical_var] == i]
            temp[numerical_var].hist(label=f"{numerical_var} for {categorical_var} = {i}")
        plt.legend()
        plt.show()