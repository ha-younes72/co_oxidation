import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data_random_simularion1.dat',
        delim_whitespace=True,
        usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        names=["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "production"])

print(df.head())


