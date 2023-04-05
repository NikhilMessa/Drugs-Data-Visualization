# -*- coding: utf-8 -*-
"""DV_Python (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E1vgGJdr2ezNSaj9sgnhm870oaJxywcz
"""

from google.colab import files
uploaded = files.upload()



import seaborn as sns
import pandas as pd
import numpy as np
import pandas as pd

# Create a dataset
df = pd.read_csv('Drug (2).csv')

# Default heatmap
p1 = sns.heatmap(df)

import pandas as pd

df = pd.read_csv('Drug (2).csv')
df.head()
df.info()

import numpy as np; 
import pandas as pd
np.random.seed(0)
import seaborn as sns; 
df = pd.read_csv('Drug (2).csv')
sns.set_theme()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(data=df)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('Drug (2).csv')


sns.histplot(df['Population'], kde = True, color = 'red')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

x = df['Population']
y = df['Death']

plt.scatter(x,y,alpha=0.4, c = "yellow",linewidth = 1.5,marker = "D", edgecolor = "Red",label=f'y.correlation{np.corrcoef(x,y)}')
plt.xlabel('Population')
plt.ylabel('Death')
plt.title('Death')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")
df = pd.read_csv('Drug (2).csv')
ax = sns.boxplot(x=df["Death"])

import seaborn
import matplotlib.pyplot as plt
import pandas as pd

seaborn.set(style = 'whitegrid')
df = pd.read_csv('Drug (2).csv')
df.head()
seaborn.stripplot(x="Year", y="Age Group 19-25", data=df)

plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")
df = pd.read_csv('Drug (2).csv')
ax = sns.countplot(x=df["Case Filed"])

import seaborn
import matplotlib.pyplot as palt
import pandas as pd	
	
seaborn.set(style = 'whitegrid')
df = pd.read_csv('Drug (2).csv')	
seaborn.violinplot(x ="Year",
			y ="Case Filed",
			style ="event",
			data = df)
plt.show()

import plotly.express as px
import pandas as pd
df = pd.read_csv('Drug (2).csv')
ax = df.plot.area(stacked = False)

# importing the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loading the dataset
# from seaborn library
df = pd.read_csv('Drug (2).csv')

# viewing the dataset
print(df.head(4))
# density plot for 'tip'
df.Death.plot.density(color='green')
plt.title('Density Plot for Death')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="ticks", color_codes=True)
df = pd.read_csv('Drug (2).csv')
sns.catplot(x="Gender", y="Case Filed", kind="point", data=df)
plt.show()