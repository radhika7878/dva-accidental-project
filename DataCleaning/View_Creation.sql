DROP VIEW Combined_data

CREATE VIEW Combined_data
AS 
SELECT * FROM Accident_Information A
INNER JOIN Clean_Vehicle_Info V
ON A.Accident_Index= V.Vehicle_Accident_Index
WHERE A.Accident_Severity LIKE '%fatal%'
OR A.Accident_Severity LIKE '%serious%'

SELECT COUNT(*) FROM Combined_data

SELECT COUNT(Accident_Index), Year FROM Combined_data
GROUP BY Year
ORDER BY Year

--SELECT DISTINCT Accident_Severity from Accident_Information