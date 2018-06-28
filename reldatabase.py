from sqlalchemy import create_engine
import pandas as pd

data = pd.read_csv('CSV FILE') #company_forces.csv 

dengine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', dengine)

data1 = pd.read_sql_query('SELECT * FROM data_table', dengine)
print('Data set 1')
print(data1)
print('')

data2 = pd.read_sql_query('SELECT dept, sum(number) FROM data_table group by dept', dengine)
print('Data set 2')
print(data2)

