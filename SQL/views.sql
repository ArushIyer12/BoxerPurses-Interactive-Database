-- views used when building the database

Create View BoxersByAvgPurse AS
    SELECT Boxers.Boxer, avg(Purse) as "Average Purse", count(Bouts.Bout_ID) as "# of fights"
    FROM Bouts
    INNER JOIN Boxers
    ON Boxers.Boxer_ID = Bouts.Boxer_ID
    GROUP BY Boxers.Boxer;



Create View BoxersByAvgRealPurse AS
    SELECT Boxers.Boxer, avg(RPurse) as "Average Real Purse", count(Bouts.Bout_ID) as "# of fights"
    FROM Bouts
    INNER JOIN Boxers
    ON Boxers.Boxer_ID = Bouts.Boxer_ID
    GROUP BY Boxers.Boxer;