import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(5,4), columns=["A","B","C","D"])
print(df)

print(df.iloc[1:2,3])