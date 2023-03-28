import pymssql
import sys
import matplotlib.pyplot as plt

servername = 'arushiyer.database.windows.net'
login = 'ReadWriteUser'
pwd = 'nu!cs2022'
dbname = 'BoxerPurses'

print('**Trying to connect to BoxerPurses in Microsoft Azure cloud...')
print()
print('**Note that this may take a few tries')
print()

try:
  dbConn = pymssql.connect(server=servername,
                           user=login,
                           password=pwd,
                           database=dbname)
  print("**connected!")
except Exception:
  print("failed to connect. Please try again")
  sys.exit()
finally:
  print()


# views used 


  # Create View BoxersByAvgPurse AS
    #SELECT Boxers.Boxer, avg(Purse) as "Average Purse", count(Bouts.Bout_ID) as "# of fights"
    #FROM Bouts
    #INNER JOIN Boxers
    #ON Boxers.Boxer_ID = Bouts.Boxer_ID
    #GROUP BY Boxers.Boxer



#Create View BoxersByAvgRealPurse AS
    #SELECT Boxers.Boxer, avg(RPurse) as "Average Real Purse", #count(Bouts.Bout_ID) as "# of fights"
    #FROM Bouts
    #INNER JOIN Boxers
    #ON Boxers.Boxer_ID = Bouts.Boxer_ID
    #GROUP BY Boxers.Boxer

dbCursor = dbConn.cursor()

print("** Welcome to the BoxerPurses app **")
print()
print("This interactive database contains information on all professional boxing matches sanctioned by the Nevada State Athletic Commission (NSAC)")
print()
print("Here are the possible commands:")
print("1. View a list of boxers ordered by average purse or average real purse")
print("2. View all bout information associated with a specific bout id")
print("3. View visualizations of average purse across a collection of different variables")
print()

print()
cmd = input("Please enter a command (1-3, x to exit): ")
print()

while cmd != "x":
  if cmd == str(1):

    question1 = input("Are you interested in regular purse numbers or real purse numbers (adjusted for cost of living? (regular/real): ")
    print()
    if question1 in ['regular', 'Regular', 'reg', 'Reg']:
      
      question2 = input("Do you have a minimum average purse in mind? (Y/N): ")

      print()
      
      if question2 in ["Y", "y", "Yes", "yes"]:
         minPurse = input("Please enter a minimum purse. Note that purses in this dataset range from $800 to upwards of $30,000,000: ")
      else:
        minPurse = str(0)


      sql = """
        Select Boxer, format(round("Average Purse",2), 'C2'), "# of fights"
FROM BoxersByAvgPurse
WHERE "Average Purse" > %s
ORDER BY "Average Purse" desc
        """
      try: 
        dbCursor.execute(sql, (minPurse))
        rows = dbCursor.fetchmany(10)
      except Exception as err:
        print()
        print("query failed:", err)
        print()
        print("Please try again")
        print()
        continue

      # rows = helper.select_n_rows(dbConn, sql, 10, (minPurse))

      print()

      print("Boxer Name : Average Purse: # of Fights Sanctioned by NSAC")

      print()

      while True:
        if len(rows) == 0:
          print("no boxers found")
          break
        else:
          for row in rows:
            result = ' : '.join(map(str, row))
            print(result)
  
          rows = dbCursor.fetchmany(10)

          # rows = helper.select_n_rows(dbConn, sql, 10, (minPurse))
  
        if len(rows) == 0:
          break
          
        print()
        more = input("Display more? [yes/no] ")
        if more == "y" or more == "yes":
          continue
        else:
          break

    elif question1 in ['real','Real','rea','Rea']:
      
      question2 = input("Do you have a minimum average real purse in mind? (Y/N): ")
      print()

      if question2 in ["Y", "y", "Yes", "yes"]:
        minPurse = input("Please enter a minimum real purse. Note that average real purses in this dataset range from $700 to $20,000,000: ")
      else:
        minPurse = str(0)  

      
      sql = """
        Select Boxer, format(round("Average Real Purse",2),'C2'), "# of fights"
FROM BoxersByAvgRealPurse
WHERE "Average Real Purse" > %s
ORDER BY "Average Real Purse" desc
        """
      
      try: 
        dbCursor.execute(sql, (minPurse))
        rows = dbCursor.fetchmany(10)
      except Exception as err:
        print()
        print("query failed:", err)
        print()
        print("Please try again")
        print()
        continue

      # rows = helper.select_n_rows(dbConn, sql, 10, (minPurse))

      print()

      print("Boxer Name : Average Purse: # of Fights Sanctioned by NSAC")

      print()

      while True:
        if len(rows) == 0:
          print("no boxers found")
          break
        else:
          for row in rows:
            result = ' : '.join(map(str, row))
            print(result)
  
        rows = dbCursor.fetchmany(20)

        # rows = helper.select_n_rows(dbConn, sql, 10, (minPurse))
  
        if len(rows) == 0:
          break
          
        print()
        more = input("Display more? [yes/no] ")
        if more == "y" or more == "yes":
          continue
        else:
          break
    else:
      print("Invalid input. Please try again")
  
  elif cmd == str(2):

    id = input("Please enter a bout id (ex: 1207 or 547): ")

    sql = """
    SELECT Bout_ID, Boxer, Age, Bouts.Date, Venue, format(Purse,'C2'), Production_info, Promotional_info, Weight_class, Fight_Importance 
FROM Bouts 
INNER JOIN Boxers
ON Bouts.Boxer_ID = Boxers.Boxer_ID
INNER JOIN Venues
ON Bouts.Venue_ID = Venues.Venue_ID
INNER JOIN Productions
ON Bouts.Production_ID = Productions.Production_ID
INNER JOIN Promotions
ON Bouts.Promotional_ID = Promotions.Promotional_ID
INNER JOIN Weights
On Bouts.Weight_ID = Weights.Weight_class_ID
INNER JOIN Importances
ON Bouts.Fight_Importance_ID = Importances.Importance_ID
WHERE Bouts.Bout_ID = %s
;
    """
    try: 
      dbCursor.execute(sql, (id))
      rows = dbCursor.fetchall()
    except Exception as err:
      print()
      print("error: ", err)
      print()
      print("Invalid Query. Try again")
      print()
      continue

    if len(rows) == 1:
      row = rows[0]
      print('Bout ID : ', row[0])
      print('Boxer 1 Name : ', row[1])
      print('Boxer 1 Age : ', row[2])
      print('Boxer 2 Name : NA')
      print('Boxer 2 Age : NA')
      print('Date : ', row[3])
      print('Venue : ', row[4])
      print('Boxer 1 Purse : ', row[5])
      print('Boxer 2 Purse : NA')
      print('Production Info : ', row[6])
      print('Promotional Info : ', row[7])
      print('Boxer 1 Weight Class : ', row[8])
      print('Boxer 2 Weight Class : NA')
      print('Fight Importance : ', row[9])
    elif len(rows) == 2: 

      combined = rows[0] + rows[1]
      unique = []
      
      for i in combined:
        if i not in unique:
          unique.append(i)

      if rows[0][8] == rows[1][8]:
        unique.append(rows[0][8])

      print('Bout ID : ', unique[0])
      print('Boxer 1 Name : ', unique[1])
      print('Boxer 1 Age : ', unique[2])
      print('Boxer 2 Name : ', unique[10])
      print('Boxer 2 Age : ', unique[11])
      print('Date : ', unique[3])
      print('Venue : ', unique[4])
      print('Boxer 1 Purse : ', unique[5])
      print('Boxer 2 Purse : ', unique[12])
      print('Production Info : ', unique[6])
      print('Promotional Info : ', unique[7])
      print('Boxer 1 Weight Class : ', unique[8])
      print('Boxer 2 Weight Class : ', unique[13])
      print('Fight Importance : ', unique[9])

    else:
      print()
      print('No bout found')
      

  elif cmd == str(3):
    print("You can visualize average purse vs. ")
    print("1. Weight class")
    print("2. Venue (top 10)")
    print("3. Production Company")
    print("4. Promotional Company (top 10)")
    print("5. Fight Importance")
    print()
    
    selection = input("Which would you like to see (enter 1-5): ")

    if selection == str(1):

      sql = """SELECT Weight_class, format(avg(Purse),'C2') FROM Bouts
INNER JOIN  Weights
ON Bouts.Weight_ID = Weights.Weight_class_ID
GROUP BY Weight_class 
ORDER BY avg(Purse); """

      dbCursor.execute(sql)
      rows = dbCursor.fetchall()

      for row in rows:
        print(row[0], ':', row[1])
  
      x = []
      y = []

      for row in rows:
        x.append(row[0])
        y.append(row[1])

      fig = plt.figure(figsize = (2, 2))  
      plt.bar(x,y)
      plt.xticks(rotation = 90)
      plt.show(block = False)
      
    elif selection == str(2):
      sql = """SELECT Top(10) Venue, format(avg(Purse),'C2') FROM Bouts
INNER JOIN  Venues
ON Bouts.Venue_ID = Venues.Venue_ID
GROUP BY Venue
ORDER BY avg(Purse) desc; """

      dbCursor.execute(sql)
      rows = dbCursor.fetchall()

      for row in rows:
        print(row[0], ':', row[1])
  
      x = []
      y = []

      for row in rows:
        x.append(row[0])
        y.append(row[1])

      fig = plt.figure(figsize = (2, 2))  
      plt.bar(x,y)
      plt.xticks(rotation = 90)
      plt.show(block = False)

      

    
    elif selection == str(3):
      sql = """SELECT Production_info, format(avg(Purse),'C2') FROM Bouts
INNER JOIN  Productions
ON Bouts.Production_ID = Productions.Production_ID
GROUP BY Production_info
ORDER BY avg(Purse) desc; """

      dbCursor.execute(sql)
      rows = dbCursor.fetchall()

      for row in rows:
        print(row[0], ':', row[1])
  
      x = []
      y = []

      for row in rows:
        x.append(row[0])
        y.append(row[1])

      fig = plt.figure(figsize = (2, 2))  
      plt.bar(x,y)
      plt.xticks(rotation = 90)
      plt.show(block = False)
      
    elif selection == str(4):
      sql = """SELECT Top(10) Promotional_info, format(avg(Purse),'C2') FROM Bouts
INNER JOIN  Promotions
ON Bouts.Promotional_ID = Promotions.Promotional_ID
GROUP BY Promotional_info
ORDER BY avg(Purse) desc; """

      dbCursor.execute(sql)
      rows = dbCursor.fetchall()

      for row in rows:
        print(row[0], ':', row[1])
  
      x = []
      y = []

      for row in rows:
        x.append(row[0])
        y.append(row[1])

      fig = plt.figure(figsize = (2, 2))  
      plt.bar(x,y)
      plt.xticks(rotation = 90)
      plt.show(block = False)
      
  
    elif selection == str(5):
      sql = """SELECT Fight_Importance, format(avg(Purse),'C2') FROM Bouts
INNER JOIN  Importances
ON Bouts.Fight_Importance_ID = Importances.Importance_ID
GROUP BY Fight_Importance
ORDER BY avg(Purse) desc;"""

      dbCursor.execute(sql)
      rows = dbCursor.fetchall()

      for row in rows:
        print(row[0], ':', row[1])
  
      x = []
      y = []

      for row in rows:
        x.append(row[0])
        y.append(row[1])

      fig = plt.figure(figsize = (2, 2))  
      plt.bar(x,y)
      plt.xticks(rotation = 90)

      plt.show(block = False)

    else: 
      print()
      print('Invalid Query. Try again')
      print()
      continue
      
  print()
  cmd = input("Please enter a command (1-3, x to exit): ")
  print()

  
print()
print('***Done***')
dbConn.close()
