import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt

accident_data= pd.read_csv("Severe_Fatal.csv", sep=',')

#data transformations
columns_to_drop=['Accident_Index', 'First_Road_Class', 'First_Road_Number', 'Police_Force', 'EndOfYear', 'InScotland', 'Vehicle_Accident_Index', 'Driver_Home_Area_Type', 'model', 'Towing_and_Articulation', 'Vehicle_Location Restricted_Lane', 'Vehicle_Reference', 'Was_Vehicle_Left_Hand_Drive']

#Dropping columns that are not required
#for column in columns_to_drop:
accident_data= accident_data.drop(columns=columns_to_drop, axis=1)

#rounding latitude to 2 decimal points
accident_data['Latitude']= accident_data['Latitude'].round(2)

#rounding longitude to 2 decimal points
accident_data['Longitude']= accident_data['Longitude'].round(2)


#spliting the 'Time' column into hours and minutes
#accident_data['Time']= accident_data['Time'].str.replace('.', ':')
accident_data.dropna(subset=['Time'], inplace=True)

time_df= pd.DataFrame(accident_data['Time'].str.split(':').tolist(),columns = ['hours','minutes'])

accident_data= accident_data.merge(time_df, left_index=True, right_index=True)

#Dropping column 'Time'
accident_data=accident_data.drop(columns=['Time'], axis=1)

accident_data['hours']= accident_data['hours'].astype(np.int8)
accident_data['minutes']= accident_data['minutes'].astype(np.int8)

#splitting the 'Date' column into day, month, year
date_df= pd.DataFrame(accident_data['Date'].str.split('/').tolist(),columns = ['month','day', 'year'])

accident_data= accident_data.merge(date_df, left_index=True, right_index=True)

#Dropping column 'Date'
accident_data=accident_data.drop(columns=['Date'], axis=1)

#Dropping column 'District' and minutes
accident_data=accident_data.drop(columns=['District', 'minutes'], axis=1)

'''
#Replacing column 'InScotland' with zeros and ones
accident_data.replace(to_replace='Yes', value=1, inplace=True)
accident_data.replace(to_replace='No', value=0, inplace=True)
'''

#Replacing column 'Rural_or_Urban' with zeros and ones
accident_data.replace(to_replace='Rural', value=1, inplace=True)
accident_data.replace(to_replace='Urban', value=0, inplace=True)

#Renaming certain columns for better naming of later columns
accident_data= accident_data.rename(index=str, columns={"Weather_Conditions": "Weather", "Special_Conditions_at_Site":"Special_Conditions", "Road_Surface_Conditions": "Road_Surface", "Light_Conditions":"Light", "Junction_Detail":"Junction"})

categorical_variables=['Accident_Severity', 'Day_of_Week', 'Junction','Light', 'District','Road_Surface','Special_Conditions','Road_Type', 'Weather']

numeric_columns=['Longitude', 'Latitude', 'Number_of_Casualties', 'Number_of_Vehicles', 'Pedestrian_Crossing-Human_Control', 'Pedestrian_Crossing-Physical_Facilities', 'Speed_limit', 'Age_of_Vehicle', 'Driver_IMD_Decile', 'Engine_Capacity_CC']
#imp = Imputer(missing_values=np.nan, strategy='mean')

column_name_list=[]
min_val_list=[]
max_val_list=[]

for column in numeric_columns:
	column_name_list.append(column)
	min_val_list.append(accident_data[column].min())
	max_val_list.append(accident_data[column].max())
	accident_data[column]=(accident_data[column]-accident_data[column].min())/(accident_data[column].max()-accident_data[column].min())
	mean= accident_data[column].mean()
	accident_data[column].fillna(mean, inplace= True)
#imp.transform(accident_data[numeric_columns])

accident_data.to_csv("Imputed_Data.csv", sep=',', index=False)


for col, col_data in accident_data.iteritems():
	if str(col) not in numeric_columns:
		col_data= pd.get_dummies(col_data, prefix=col).astype(np.int8)
		accident_data= accident_data.join(col_data)
		accident_data=accident_data.drop(columns=[str(col)], axis=1)
		print(str(col),"is done")

column_name_series= pd.Series(column_name_list)
min_series= pd.Series(min_val_list)
max_series= pd.Series(max_val_list)

series_df= pd.concat([column_name_series, min_series, max_series], axis=1).reset_index()

series_df.to_csv("Column_Min_Max.csv", sep=',', index=False)
'''
for i in range(2004,2016):
	required_data=accident_data[accident_data['Year']==i]
	required_data.to_csv("accident_data_sparse"+str(i)+".csv", sep=',')
	print(i, "is done")
'''
accident_data.to_csv("DroppedColumnsData.csv", sep=',', index=False)