'''import pandas as pd

# Ensure you're providing the correct file path for your Excel and CSV files
# Read the Excel file for Countrylocation (adjust the file path and name if necessary)
df1 = pd.read_excel('Countrylocation.xlsx')  # Ensure this file exists and the path is correct

# Read the CSV file for household_air_pollution_deaths
df2 = pd.read_csv('household_air_pollution_deaths.csv')  # Ensure this file exists and the path is correct

# Check the actual column names in df1 and df2
print(df1.columns)  # This will help you confirm the correct column names in the Excel file
print(df2.columns)  # This will help you confirm the correct column names in the CSV file

# Adjust the merge if necessary based on actual column names
# Example: If the column name in df1 is not 'name', replace 'name' with the actual column name
merged_df = pd.merge(df2, df1, on='Location', how='inner')

# Display the merged dataframe (you can use print or save it to a file)
print(merged_df)

# Optionally, you can save the merged dataframe to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)
'''


import pandas as pd

# Sample data
'''data =  pd.read_csv('atleast_basic_Drinking_water.csv') 

df = pd.DataFrame(data)

# Step 2: Pivot the data
pivot_df = df.pivot_table(index=['Location', 'Period'], columns='Dim1', values='Value').reset_index()

# Step 3: Fill missing values with 0 if necessary (optional)
pivot_df.fillna(0, inplace=True)

# Step 4: Display the pivoted DataFrame
output_path = 'pivoted_data1.csv'
pivot_df.to_csv(output_path, index=False)'''
import pandas as pd

# Load the datasets
'''atleast_basic_path = 'C:/path_to_your_data/atleast_basic_Drinking_water.csv'
safely_managed_path = 'C:/path_to_your_data/safely_managed_drinking_water.csv'

df_atleast = pd.read_csv('pivoted_data1.csv')
df_safe = pd.read_csv('pivoted_data.csv')

# Merge the two datasets on 'Location' and 'Period'
merged_df = pd.merge(df_atleast, df_safe, on=['Location', 'Period'], suffixes=('_atleast', '_safe'))

# Display the merged dataframe
print(merged_df)

# Optionally, save the merged dataframe to a CSV file
output_path = 'merged_water_data.csv'
merged_df.to_csv(output_path, index=False)
'''

'''data =  pd.read_csv('Handwashing.csv') 

df = pd.DataFrame(data)

# Step 2: Pivot the data
pivot_df = df.pivot_table(index=['Location', 'Period'], columns='Dim1', values='Value_Handwash').reset_index()

# Step 3: Fill missing values with 0 if necessary (optional)
pivot_df.fillna(0, inplace=True)

# Step 4: Display the pivoted DataFrame
output_path = 'pivoted_data3.csv'
pivot_df.to_csv(output_path, index=False)'''

'''
df_atleast = pd.read_csv('pivoted_data2.csv')
df_safe = pd.read_csv('pivoted_data3.csv')

# Merge the two datasets on 'Location' and 'Period'
merged_df = pd.merge(df_atleast, df_safe, on=['Location', 'Period'], suffixes=('_defacation', '_handwash'))

# Display the merged dataframe
print(merged_df)

# Optionally, save the merged dataframe to a CSV file
output_path = 'merged_sanitation_data.csv'
merged_df.to_csv(output_path, index=False)'''
'''import pandas as pd
import pandas as pd
import json

# Load data
import pandas as pd
import json

# Load data from CSV
data = pd.read_csv("ghg_emissions.csv")

# Ensure that 'date' is a string
data['date'] = data['date'].astype(str)

# Create a hierarchical structure
hierarchy = [{"id": "root", "parent": "", "name": "Root"}]  # Add root node
seen_years = set()

# Iterate over each row
for index, row in data.iterrows():
    try:
        # Attempt to extract the year from the 'date' assuming it's in the format '1/1/2014'
        year = row['date'].split('/')[2]
    except IndexError:
        # Handle cases where 'date' might not be in the expected format
        print(f"Date format error in row {index}: {row['date']}")
        continue

    source = row['source']
    emissions = row['emissions']

    # Add year node if not already added, with "root" as its parent
    if year not in seen_years:
        hierarchy.append({"id": year, "parent": "root", "name": year})
        seen_years.add(year)

    # Add source node, with the year as its parent
    hierarchy.append({"id": f"{year}-{source}", "parent": year, "name": source, "emissions": emissions})

# Save the hierarchy to a JSON file
with open('emissions_hierarchy.json', 'w') as f:
    json.dump(hierarchy, f, indent=4)'''
import pandas as pd

# Load your dataset
df = pd.read_csv('population.csv')

# Melt the dataset to pivot years from columns into rows
df_melted = pd.melt(df, id_vars=["Country Name", "Country Code"], 
                    var_name="Year", 
                    value_name="Population")

# Save the transformed data to a new CSV file
df_melted.to_csv('population.csv', index=False)
