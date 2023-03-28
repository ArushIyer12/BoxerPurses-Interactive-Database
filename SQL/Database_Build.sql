.open BoxerPurses.db
  
CREATE TABLE Productions(

Production_info TEXT,
Production_ID INT PRIMARY KEY

);

CREATE TABLE Promotions(

Promotional_info TEXT,
Promotional_ID INT PRIMARY KEY

);

CREATE TABLE Importances(

Fight_importance TEXT,
Fight_importance_ID INT PRIMARY KEY

);

CREATE TABLE Venues(

Venue TEXT,
Venue_ID INT PRIMARY KEY

);

CREATE TABLE Weights(

Weight_class TEXT,
Weight_class_ID INT PRIMARY KEY

);

CREATE TABLE Boxers(

Boxer_name TEXT,
Boxer_ID INT PRIMARY KEY,
Boxer_DOB TEXT

);

CREATE TABLE Bouts(

Bout_ID INT,
Boxer_ID INT,
Boxer_age INT,
Fight_date TEXT,
Venue_ID INT,
Real_Purse REAL,
Purse INT,
Production_ID INT,
Promotional_ID INT,
Weight_class_ID INT,
Fight_importance_ID INT,
PRIMARY KEY(Bout_ID, Boxer_ID),
FOREIGN KEY (Boxer_ID) REFERENCES Boxers(Boxer_ID),
FOREIGN KEY (Venue_ID) REFERENCES Venues(Venue_ID),
FOREIGN KEY (Production_ID) REFERENCES Productions(Production_ID),
FOREIGN KEY (Promotional_ID) REFERENCES Promotions(Promotional_ID),
FOREIGN KEY (Weight_class_ID) REFERENCES Weights(Weight_class_ID),
FOREIGN KEY (Fight_importance_ID) REFERENCES Importances(Fight_importance_ID)

);








