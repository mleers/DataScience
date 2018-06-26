import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3), index = ['a', 'b', 'd', 'f', 'g'], columns = ['col1', 'col2', 'col3'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])	#reindex substitutes missing data with NaN

print(df)
print('\n')
print(df['col1'].isnull())	#checks if data is missing in first column
