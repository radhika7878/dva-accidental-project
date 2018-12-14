import pandas as pd
from apyori import apriori

for cluster_number in range(0, 100):
    accident_data = pd.read_csv("clusters/cluster_number_"+str(cluster_number)+".csv", sep=",")

    accident_data=accident_data.drop(columns=['Towing_and_Articulation','Carriageway_Hazards',  'Accident_Index', 'Date', 'Time', 'EndOfYear' , 'Vehicle_Accident_Index', 'Cluster_Label', 'First_Road_Number', 'Number_of_Casualties', 'Pedestrian_Crossing-Physical_Facilities', 'Police_Force', 'InScotland', 'Driver_IMD_Decile', 'Vehicle_Location Restricted_Lane', 'Vehicle_Reference'])
    accident_data = accident_data.drop(accident_data.columns[0], axis=1)
    accident_data.loc[accident_data['Skidding_and_Overturning'] == 'None', 'Skidding_and_Overturning'] = 'No Skidding'
    accident_data.loc[accident_data['Special_Conditions_at_Site'] == 'None', 'Special_Conditions_at_Site'] = 'No Spl Cond'
    accident_data.loc[accident_data['Pedestrian_Crossing-Human_Control'] > 0, 'Pedestrian_Crossing-Human_Control'] = 'Ped_Crossing'
    accident_data.loc[accident_data['Pedestrian_Crossing-Human_Control'] == 0, 'Pedestrian_Crossing-Human_Control'] = 'No_Ped_Crossing'
    records = []  
    for i in range(0, len(accident_data.index)):  
        records.append([str(accident_data.values[i,j]) for j in range(0, 26)])
    # association_rules = apriori(records, min_support=0.2, min_confidence=0.3, min_lift=2, min_length=2) 
    association_rules = apriori(records, min_support=0.1, min_confidence=0.2, min_lift=3, min_length=2)  
    association_results = list(association_rules)

    myfile = open('rules/cluster_rules_'+str(cluster_number)+'.txt', 'w')
    for item in association_results:
        myfile.write(str(item[0]) + '\n')
    myfile.close()

    print(str(cluster_number) + "done")