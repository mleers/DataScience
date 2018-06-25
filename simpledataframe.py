import pandas as pd	#pandas library for data analysis

data = {'Name':['Mike', 'Tony', 'Saul', 'Jerry'],'Age':[20,34,31,29]}	#defines data
df = pd.DataFrame(data, index=['entry1','entry2','entry3','entry4'])	#defines index 
print(df)
