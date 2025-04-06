# Box Office Analysis

This project takes data from Box Office Mojo on the top 10 highest grossing films at the US box office in the 21st century and examines and analyses various aspects of it. It also looks at the overall US box office numbers; i.e., total gross.

- Box Office = `Box_Office_top_10_2000_2024`
- Gross = `Box_Office_gross_2000_2024`

# Data cleaning
Although the data are mostly clean from my collection, there are some issues that need resolving. One studio has gone through a name change during the time series represented by these data. I therefore wrote this line of code to make sure all old occurrences of the studio name where renamed to the new name to avoid any missrepresentation in my analysis.

![image](https://github.com/user-attachments/assets/c189ed07-0f3f-44a8-941c-6b4c8bc844c2)


# Charts
I have set up a jupyter notebook that will process the input csv data into a number of pre-defined charts as listed below:

## 1. Box office budgets for highest grossing film
For this I made sure to create a filtered datafram with only the number one ranked film at the box office for each year:
![image](https://github.com/user-attachments/assets/71884931-6778-46e9-bce4-169e5e3fb464)

These data are then plotted within a line chart:

![image](https://github.com/user-attachments/assets/50ef45de-fff3-4551-a7a6-d5c59498bb4a)

## 2. Average budgets for box office top 10
For this chart I calculated a new dataframe that had the average budget for each year within the original dataframe:
![image](https://github.com/user-attachments/assets/c39b0973-81a2-4c27-a6bf-d2178a3623df)

These data are then plotted within a line chart:

![image](https://github.com/user-attachments/assets/6fab1171-e317-4d9a-b050-f2091e591cbe)

## 3. The top 5 distributors in the top 10
For this chart I used a `groupby()` method to return a count of each distributor in the dataset. I then sorted count in descending order and applied a `head(5)` method as I only wanted to see the 5 most common distributors:
![image](https://github.com/user-attachments/assets/a65d5dc8-1e39-4363-bfda-154c22211b12)

These data are plotted in a horizontal bar chart:

![image](https://github.com/user-attachments/assets/c205f29e-917b-43bb-95af-b64d9dccfa44)

## 4. Overall box office gross over time
This chart takes data from the `Box_Office_gross_2000_2024` csv and plots total gross against year in a line chart.
![image](https://github.com/user-attachments/assets/92c7410a-0181-410f-ac11-bb99f58c73dd)

## 5. Density plot showing total films in the top 10 by distributor over time
For this chart, I used the `groupby()` method to group the dataframe by Year and Distributor and return the size of each grouped row:
![image](https://github.com/user-attachments/assets/02e5da67-4f88-4725-b539-b97bb39e6ff9)

These data were then plotted within a scatter plot using a variable size and colourscale to indicate density:

![image](https://github.com/user-attachments/assets/1cc3dc24-672a-4124-8434-f818d1b5a752)

## 6. Density plot showing total films in the top 10 by genre over time
For this chart, I used the `groupby()` method to group the dataframe by Year and Genre and return the size of each grouped row:
![image](https://github.com/user-attachments/assets/655f597f-6492-4430-a12d-e19d7e537b7c)

These data were then plotted within a scatter plot using a variable size and colourscale to indicate density:

![image](https://github.com/user-attachments/assets/d5ba0064-06c5-40b9-9a98-e642f82b9526)

# Future work
I will look to improve what insights I can gain from this data. This will include introducing an inflation adjustment for budget/gross data to provide a more reliable measure.

# Credits
Data for this project are taken from Box Office Mojo - https://www.boxofficemojo.com/
