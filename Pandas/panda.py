# import numpy as np
# import pandas as pd
# import matplotlib


import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('profile.csv')

profile = ProfileReport(df)
print(profile)