import pandas as pd
from datetime import datetime

# Assuming the data is already loaded into a DataFrame called 'df'
df=pd.read_csv('churndata222.csv')
print(df)
# Convert the 'Accuracy' column to numeric values
df['Accuracy'] = df['Accuracy'].str.rstrip('%').astype(float)

# Calculate the current quarter based on today's date
current_quarter = (datetime.now().month - 1) // 3 + 1

# Define the weightage for each quarter
weightage_current = 0.5
weightage_previous = 0.3
weightage_previous_previous = 0.2

# Calculate the weightage based on the quarter
df['Weightage'] = df['Quarter'].apply(lambda q: weightage_current if q == current_quarter
                                      else weightage_previous if q == current_quarter - 1
                                      else weightage_previous_previous)

# Calculate the weighted average accuracy by multiplying accuracy with weightage
df['Weighted_Accuracy'] = df['Accuracy'] * df['Weightage']











import pandas as pd
from datetime import datetime

# Assuming the data is already loaded into a DataFrame called 'df'
df=pd.read_csv('sampleaccuracy.csv')
# print(df)
# Convert the 'Accuracy' column to numeric values
df['Accuracy'] = df['Accuracy'].str.rstrip('%').astype(float)

current_quarter = (datetime.now().month - 1) // 3 + 1   # Calculate the current quarter based on today's date

# Calculate the weightage based on the quarter
df['Weightage'] = df['Quarter'].apply(lambda q: 0.5 if q == current_quarter
                                      else 0.3 if q == current_quarter - 1
                                      else 0.2)
print(df)
# Calculate the weighted average accuracy with weightage
df['Weighted_Accuracy'] = df['Accuracy'] * df['Weightage']
print(df)
# Group by 'Churn_Class', 'Model_Name', and 'Quarter','Prod_grp' and calculate the weighted average accuracy
grouped_data = df.groupby(['Footprint' ,'Churn_Class', 'Model_Name','Prod_grp'])['Weighted_Accuracy'].sum()/ df.groupby(['Footprint' ,'Churn_Class', 'Model_Name','Prod_grp'])['Weightage'].sum()

# Convert the grouped data back to a DataFrame
result = grouped_data.reset_index()

print(result)

# Group by 'Churn_Class', 'Model_Name', and 'Quarter', and calculate the weighted average accuracy
grouped_data = df.groupby(['Footprint' ,'Churn_Class', 'Model_Name', 'Quarter','Prod_grp'])['Weighted_Accuracy'].sum() / df.groupby(['Footprint' ,'Churn_Class', 'Model_Name', 'Quarter','Prod_grp'])['Weightage'].sum()

# Convert the grouped data back to a DataFrame
result = grouped_data.reset_index()

print(result)




import pandas as pd
from datetime import datetime

# Assuming the data is already loaded into a DataFrame called 'df'
df=pd.read_csv('sampleaccuracy.csv')

# Convert the 'Accuracy' column to numeric values
df['Accuracy'] = df['Accuracy'].str.rstrip('%').astype(float)

# Calculate the current quarter based on today's date
current_month = datetime.now().month
current_year = datetime.now().year

if current_month in [1, 2, 3]:
    current_quarter = 1
else:
    current_quarter = (current_month - 1) // 3 + 1

# Define the weightage for each quarter
weightage_current = 0.5
weightage_previous = 0.3
weightage_previous_previous = 0.2

# Function to calculate the weightage based on the quarter
def calculate_weightage(quarter):
    if quarter == current_quarter:
        return weightage_current
    elif quarter == current_quarter - 1 or (quarter == 4 and current_quarter == 1):
        return weightage_previous
    else:
        return weightage_previous_previous

# Calculate the weightage based on the quarter
df['Weightage'] = df['Quarter'].apply(calculate_weightage)

# Calculate the weighted average accuracy by multiplying accuracy with weightage
df['Weighted_Accuracy'] = df['Accuracy'] * df['Weightage']

# Group by 'Churn_Class', 'Model_Name', and 'Quarter', and calculate the weighted average accuracy
grouped_data = df.groupby(['Churn_Class', 'Model_Name', 'Quarter'])['Weighted_Accuracy'].sum() / df.groupby(['Churn_Class', 'Model_Name', 'Quarter'])['Weightage'].sum()

# Convert the grouped data back to a DataFrame
result = grouped_data.reset_index()

print(result)
