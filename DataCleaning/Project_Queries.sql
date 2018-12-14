--CREATE INDEX accident_index
--ON Accident_Information (Accident_Index);

--CREATE INDEX accident_index
--ON Vehicle_Information (Accident_Index);

--SELECT COUNT(Accident_Index) FROM Accident_Information;
--SELECT COUNT(DISTINCT Accident_Index) FROM Accident_Information;

--SELECT COUNT(Vehicle_Accident_Index) FROM Clean_Vehicle_Info;
--SELECT COUNT(DISTINCT Vehicle_Accident_Index) FROM Clean_Vehicle_Info;

--SELECT COUNT(*) FROM Accident_Information
--WHERE Accident_Index NOT IN(
--SELECT Accident_Index FROM Accident_Information
--GROUP BY Accident_Index
--HAVING COUNT(Accident_Index)>=2)

--ABOVE COUNT: 670991

--SELECT COUNT(*) FROM Vehicle_Information
--WHERE Vehicle_Accident_Index NOT IN(
--SELECT Accident_Index FROM Accident_Information
--GROUP BY Accident_Index
--HAVING COUNT(Accident_Index)>=2)

--ABOVE COUNT: 749052

SELECT Date, Accident_Index, Accident_Severity FROM Accident_Information
WHERE Accident_Index IN(
SELECT Accident_Index FROM Accident_Information
WHERE Accident_Severity LIKE '%fatal%'
GROUP BY Accident_Index
HAVING COUNT(Accident_Index)>=2)
ORDER BY 2 ASC, 1 ASC

UPDATE Accident_Information
SET District='Herefordshire'
WHERE District like '%herefordshire%'

UPDATE Accident_Information
SET District='Bristol'
WHERE District like '%bristol%'

UPDATE Accident_Information
SET District='London'
WHERE District like '%london%'

UPDATE Accident_Information
SET District='Edinburgh'
WHERE District like '%edinburgh%'

UPDATE Accident_Information
SET District='Kingston upon Hull'
WHERE District like '%Kingston upon Hull%'


SELECT DISTINCT District 
FROM Accident_Information
WHERE District like '%city of%'

DELETE FROM Accident_Information
