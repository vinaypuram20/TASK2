# Import pandas
import pandas as pd

# reading csv file
df = pd.read_csv("county_demographics.csv")

# Extracting the Column Data of Education.Bachelors Degree or Higher
Data = df['Education.Bachelor\'s Degree or Higher']

# Counting the No of Rows and Calculating 10% of Total Rows
Count_Cal_Per = (Data.count()*10)/100

# Rounding the Count
n = round(Count_Cal_Per)

# Finding the Top 10% Colleges List
Top_Colleges = df.nlargest(n, ['Education.Bachelor\'s Degree or Higher'])
print(Top_Colleges)

# Writing Data to CSV File
Top_Colleges.to_csv("TopCollegesList.csv")
