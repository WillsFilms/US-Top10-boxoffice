#histogram of top 10 budgets


#make packages available
import ast 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import the data
Top_10 = pd.read_csv("C:\\Users\\HP\\Documents\\Data Analysis\\Wills Films\\Kaggle datasets\\Box_Office_top_10_2000_2023.csv")

#view the first 3 rows of data
Top_10.head(3)

                    #Stage 2 - preprocessing and data cleaning
Top_10.drop_duplicates(inplace=True) #remove duplicates

                    #Stage 4 - data visualisations
    #runtime distribution
budget_values = Top_10['Budget ($)']
    #plot histogram
plt.hist(budget_values, bins=int(150/10),
         color='#44546A', 
         edgecolor='black')
    #plot density line on chart

    #title and labels
plt.xlabel('Budget (Hundreds of Millions of Dollars)')
plt.xlim(left=0) # starts x axis at 0
plt.ylabel("")
plt.title('Distribution of Movie Budgets', size = 17,
          pad = 10)

    #remove ticks and/or spine using seaborn package
sns.despine()
    #show the visualisation
plt.show()
plt.figure()