#pie chart of male_female ratio box office top 10

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

                    #Stage 3 - data viz - pie chart
director_gender = 'Male', 'Female' #define the series
sizes = ['230','10'] #define the data sizes for the slices defined above

#plot pie chart
plt.pie(sizes, explode=None, labels=director_gender, colors= ("Blue","pink"),
        autopct=None, shadow=None)

#show plot
plt.show()