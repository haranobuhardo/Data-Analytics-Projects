import pandas as pd
import numpy as np

s1 = ['a', 'b', np.nan]
df = pd.DataFrame(s1)

print(df)

print(s1)
print(pd.get_dummies(s1))