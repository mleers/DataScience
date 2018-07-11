import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('PublicSchools.csv')		#source: https://vincentarelbundock.github.io/Rdatasets/doc/sandwich/PublicSchools.html
	
states = data.loc[:, 'State']
y1 = data.loc[:, 'Per Capita Expenditure']
y2 = data.loc[:, 'Per Capita Income']

index = np.arange(len(states))
width = .35

plt.bar(index, y1, width, label = 'Per Capita Expenditure')
plt.bar(index + width, y2, width, label = 'Per Capita Income')	#index + width to "move" 2nd bar past first bar

plt.xlabel('State', fontsize = 10)
plt.ylabel('USD', fontsize = 10)
plt.title('Per Capita Expenditure vs Income by State in 1979', fontsize = 15)

plt.xticks(index, states, fontsize = 5, rotation = 60)
plt.legend(loc = "best")

plt.show()



