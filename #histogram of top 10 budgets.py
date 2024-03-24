#histogram of top 10 budgets


#make packages available
import ast 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

                    #Stage 1 - import the data
Top_10 = pd.read_csv("C:\\Users\\HP\\Documents\\Data Analysis\\Wills Films\\Kaggle datasets\\Box_Office_top_10_2000_2023.csv")

#view the first 3 rows of data
Top_10.head(3)

                    #Stage 2 - preprocessing and data cleaning
Top_10.drop_duplicates(inplace=True) #remove duplicates

                    #Stage 3 - data visualisations
    #define budget values
budget_values = Top_10['Budget ($)']
    #plot histogram
bins=[0,50000000,100000000,150000000,200000000,
      250000000,300000000,350000000,400000000,
      450000000,500000000] #manually define the bins to use
plt.hist(budget_values, bins=bins,
         color='#44546A', 
         edgecolor='black')

    #calculate and plot the median budget value
median_budget = np.median(budget_values)
plt.axvline(median_budget, color='r', 
            label="Median Budget ($)")
plt.legend()

    #title and labels
plt.xlabel('Budget (Hundreds of Millions of Dollars)')
plt.xlim(left=0) # starts x axis at 0
plt.ylabel("Number of movies")
plt.title('Movie Budgets for the top box office hits in the US; 2000-2023', 
          size = 14,
          pad = 10)

    #remove ticks and/or spine using seaborn package
sns.despine()

    #show the visualisation
plt.show()