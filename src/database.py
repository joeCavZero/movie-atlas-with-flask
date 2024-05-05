import pandas as pd
import numpy as np

class database :

    def __init__(self):
        self._dataFrame = pd.read_csv( 'data/Movies_dataset.csv' , sep=';' , encoding='utf-8' )
    
    def getMovieById( self , id:int ) -> dict:
        return self._dataFrame.iloc[id].to_dict()
    
    def getIdByTitle( df:pd.DataFrame , title:str) -> int:
        for i in np.arange( df.shape[0] ):
            if title in df.iloc[i]['Movie_Name']:
                return i
    
    def getRandomId(self) -> int:
        return np.random.randint( 0 , self._dataFrame.shape[0] )