# Data analysis and visualization

import pandas as pd
import matplotlib.pyplot as plt

data={
    'Year' : [2019,2020,2021,2022,2023],
    'Sales' : [1500,1800,2000,2200,2500]
}

df=pd.DataFrame(data)

plt.plot(df['Year'],df['Sales'],marker='o',linestyle='-',color='b')
plt.title('Annual Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()