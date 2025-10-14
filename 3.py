import pandas as pd
import numpy as np


def getrn():
    return np.random.randint(1, 5, 1)

def getNoten():
    return  pd.Series([getrn(),getrn(),getrn(),getrn(),5],index=["KI","Datananalyse","SoftwareTechnick","Mathe3","Wissensch"])

if __name__ == '__main__':
    #s = pd.Series([1, 2, 3], index=["a", "b", "c"])
    #s["a"]  # Zugriff über Index
    #s[0]  # Zugriff über Position
    #np.random.randint(start, stop, size)

    #print(s["a"])
    #print(s[2])
    series1 = getNoten()
    series2 = getNoten()
    series3 = (series1+series2)/2
    print(series1)
    print(series2)
    print(series3)
