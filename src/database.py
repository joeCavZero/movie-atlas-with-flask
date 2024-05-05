import pandas as pd
import numpy as np

class database :

    def __init__(self):
        self._dataFrame = pd.read_csv( 'data/Movies_dataset.csv' , sep=',' , encoding='utf-8' )
    
    def getMovieById( self , id:int ) -> dict:
        print( self._dataFrame.iloc[id] )
        return self._dataFrame.iloc[id].to_dict()
    
    def getIdByTitle(self , title:str) -> int:
        for i in np.arange( self._dataFrame.shape[0] ):
            if title in self._dataFrame.iloc[i]['Movie_Name']:
                return i
        return 0
    
    def getRandomId(self) -> int:
        return np.random.randint( 0 , self._dataFrame.shape[0] )