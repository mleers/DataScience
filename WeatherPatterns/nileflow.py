import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('Nile.csv')

slope, intercept, r_value, p_value, std_err = stats.linregress(df['time'],df['value'])          #linear regression params

ax1 = sns.regplot(x= 'time', y= 'value', data = df,line_kws={'label':'y={0:.1f}x+{1:.1f}'.format(slope,intercept)})

ax1.legend()
plt.title('Flow Over Time at Aswan Dam of Nile River')
plt.xlabel('Year')
plt.ylabel('Flow of Water in 10^8 m^3')

plt.show()