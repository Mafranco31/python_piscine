class SpatioTemporalData:
    def __init__(self, data):
        self.df = data

    def when(self, location):
        return self.df[self.df['City'] == location]['Year'].unique()
    def where(self, date):
        return self.df[self.df['Year'] == date]['City'].unique()
    