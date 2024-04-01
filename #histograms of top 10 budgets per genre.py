#histograms of top 10 budgets per genre


#make packages available
import ast 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.rcsetup
import seaborn as sns

matplotlib.rcParams["axes.formatter.limits"] = (-99, 99) #removes scientific labels

                    #Stage 1 - import the data
Top_10 = pd.read_csv("C:\\Users\\HP\\Documents\\Data Analysis\\Wills Films\\Kaggle datasets\\Box_Office_top_10_2000_2023.csv")

                    #Stage 3 - data visualisations
    #define budget values
budget_values = Top_10['Budget ($)']
group = Top_10['Genre']

    #group values
dat = pd.concat([group, budget_values], axis=1)
dat.columns = ['group','budget_values']

    #plot 
dat.groupby('group')['budget_values'].hist(bins=15, 
                                           alpha=0.50) #add transparency

   #title and labels
plt.legend(group, title = 'Genre')
plt.xlabel('Budget ($)')
plt.xlim(left=0) # starts x axis at 0
plt.ylabel("Number of movies")
plt.title('Movie Budgets by genre for the top box office hits \n in the US; 2000-2023', 
          size = 14,
          pad = 10)

    #remove ticks and/or spine using seaborn package
sns.despine()

    #show the visualisation
plt.tight_layout()
plt.show()