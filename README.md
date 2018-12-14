# dva-accidental-project

1. DESCRIPTION - 

The code package contains both the website where all the visualization is amalgamated and the analysis part of the code along with a csv file which is the data for analysis.

We have downloaded the original datasets from : https://www.kaggle.com/tsiaras/uk-road-safety-accidents-and-vehicles
We have also hosted our results on the following website: https://ukaccidentdva.azurewebsites.net

You can also use the code below to run the website locally, perform data cleaning and perform the dimensionality reduction, clustering and association mining experiments.

2. INSTALLATION - 

For the website you need run a local server(python) and for the if you wish to see the PowerBI analysis, 
you will need PowerBI desktop. 
For the analysis part following packages are required - Python3, numpy, pandas, apyori, matplotlib, scikit-learn, sqlite
Softwares used: Microsoft SQL Server, SQL Server Management Studio 17.0

3. EXECUTION - 

3.1 Visualization - For PowerBI visualizations just navigate to 
CODE -> 'PowerBI Trivial Analysis' and open 'Trivial Visualizations' file in PowerBI.
For the website start a local server when you are in CODE directory (python -m http.server 8000 --bind 127.0.0.1) 
and from there navigate to 'Website' -> 'webtest.html' and explore away!

3.2 Data cleaning - If you wish to create the dataset that we have combined in the Severe_Fatal.csv, please perform the following steps:
i) Download the Accident and Vehicle dataset from the following Kaggle link: https://www.kaggle.com/tsiaras/uk-road-safety-accidents-and-vehicles
ii) Import the data into SQL Server Management Studio or Sqlite into tables called Accident_Information and Clean_Vehicle_Info respectively.
iii) Run the queries in the files Project_Queries.sql and View_Creation.sql in that order. The can be found in the SQL_Queries folder.
iv) After we have created a view of the combined data, store the data back into a csv called Severe_Fatal.csv.

3.3 Analysis - For the analysis experiments, Severe_Fatal.csv is the data file which goes through the following steps: 
i) Run script Accident_ConvertToSparse.py to clean the dataset (drop columns, split columns) and one hot encode the categorical variables.
ii) Run script SVD_Truncation_Clustering.py to perform dimensionality reduction and clustering. This will create a file with cluster labels for each accident.
iii) Run Script Create_Clusters.py which will join the cluster labels with the original data and create separate csv files for each cluster.
iv) Run script Cluster_Analysis.py which will run the Apriori algorithm for each cluster and output the set of rules for each cluster


