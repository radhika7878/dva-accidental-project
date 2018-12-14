import pandas as pd

clustered_data= pd.read_csv("Clusters_with_labels.csv", sep=',')
accident_data = pd.read_csv("Severe_Fatal.csv", sep=",")

accident_data['Cluster_Label'] = clustered_data["Cluster_Label"]

for i in range(0,100):
	required_data=accident_data[accident_data['Cluster_Label']==i]
	required_data.to_csv("clusters/cluster_number_"+str(i)+".csv", sep=',')
	print(i, "is done")