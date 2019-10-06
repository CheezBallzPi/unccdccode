import numpy as np
import retrieve_data

import pandas as pd
def factorize(df):
    filt2 =['party_cd','gender_code','race_code','birth_state',]

    #df = retrieve_data.getData("./data/ncvoter_Statewide.txt", "./data/ncvoter_Statewide.pickle", filt)
    #df = pd.read_csv('plswork2.csv')
    #cancer_data = np.genfromtxt(fname = 'plswork2.csv',delimiter=',',dtype=float)
    for i in filt2:
        labels, unique = pd.factorize(df[i])
        print(unique)
        df[i] = labels
    return df
        

#print(len(cancer_data))
#print(str(cancer_data))
#print(cancer_data.shape)

#cancer_data = df.delete(arr=cancer_data,obj=0,axis=1)

