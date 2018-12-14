import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans  
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
'''
Citations:
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
https://scikit-learn.org/0.15/modules/generated/sklearn.preprocessing.Imputer.html#sklearn.preprocessing.Imputer.transform
https://matplotlib.org/users/pyplot_tutorial.html
'''

accident_data= pd.read_csv("DroppedColumnsData.csv", sep=',')

'''
component_list=[]
variance_ratio_list=[]	
for n in range(50, 501, 50):
	print(str(n)+" is starting");
	svd = TruncatedSVD(n_components=n, n_iter=10)
	svd.fit(accident_data)
	variance_ratio_list.append(svd.explained_variance_ratio_.sum())
	component_list.append(n)
	print(str(n)+" is done")

plt.plot(component_list, variance_ratio_list)
plt.ylabel('Explained Variance')
plt.xlabel('Number of Components')
plt.show()
'''
print("Reducing data")
svd= TruncatedSVD(n_components=200, n_iter=10)
reduced_data=svd.fit_transform(accident_data)

'''
cluster_count_list=[]
sse_list=[]
for n in range(10, 201, 10):
	print("Clustering:"+str(n))
	cluster= KMeans(n_clusters=n, init='k-means++').fit(reduced_data)
	sse= cluster.inertia_
	cluster_count_list.append(n)
	sse_list.append(sse)
	
plt.plot(cluster_count_list, sse_list)
plt.ylabel('Number of clusters')
plt.xlabel('Sum of Squared Errors')
plt.show()

'''
#Writing cluster centres to csv
print("Starting clustering")
cluster= KMeans(n_clusters=100, init='k-means++').fit(reduced_data)
centres= cluster.cluster_centers_
print("Getting inverse transform")
centres_inverse_transform= svd.inverse_transform(centres)
centre_columns= list(accident_data.columns.values)
centres_dataframe= pd.DataFrame(data= centres_inverse_transform, columns= centre_columns)
centres_dataframe.to_csv("Cluster_Centers.csv", sep=',', index=False)

#Getting cluster labels for each record
print("Getting cluster labels")
labels= cluster.predict(reduced_data)
accident_data['Cluster_Label']= pd.Series(labels, index=accident_data.index)

accident_data.to_csv("Clusters_with_labels.csv", sep=',',  index=False)


	

