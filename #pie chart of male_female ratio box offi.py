#pie chart of male_female ratio box office top 10

#make packages available
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the data
Top_10 = pd.read_csv("C:\\Users\\HP\\Documents\\Data Analysis\\Wills Films\\Kaggle datasets\\Box_Office_top_10_2000_2023.csv")

#view the first 3 rows of data
Top_10.head(3)

                    #Stage 2 - preprocessing and data cleaning
Top_10.drop_duplicates(inplace=True) #remove duplicates

                    #Stage 3 - data viz - pie chart
director_gender = 'Male', 'Female' #define the series
sizes = ['230','10'] #define the data sizes for the slices defined above

#define the explosion of the pie chart categories
explode = (0.0, 0.2)
#wedge properties
wp = {'linewidth':1, 'edgecolor': "black"}

#plot pie chart
plt.pie(sizes, explode=explode,  
        colors= ("#0070C0","#F612DB"),
        autopct='%1.1f%%', 
        shadow=True, 
        wedgeprops=wp)
plt.title('Proportion of male to female directors of US top 10 box office hits; 2000-2023')
plt.legend(labels=director_gender, fontsize="18", loc="best")

#fine tune display and show plot
plt.axis('equal')
plt.tight_layout()
plt.show()