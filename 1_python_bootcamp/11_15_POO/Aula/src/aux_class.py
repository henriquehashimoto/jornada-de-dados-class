import pandas as pd

# Creating a class 
class csv_processor:
    
    # Initiating with the parameters that will pass to all functions
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.df = None
    
    # Reading file
    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    #  Return filtered df 
    def filter_df(self, column, attribute):
        return self.df[self.df[column] == attribute]

