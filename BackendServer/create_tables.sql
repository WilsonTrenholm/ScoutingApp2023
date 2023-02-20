USE rawData;

CREATE TABLE matchData(
	Match_Number INT NULL,
	Team_Number INT NULL,
	Scouter_Name TEXT NULL,
	Team_Alliance INT NULL,
	Competition TEXT NULL,
	Mobility BOOLEAN NULL,
	Auto_Cube_Low INT NULL,
	Auto_Cube_Mid INT NULL,
	Auto_Cube_High INT NULL,
	Auto_Cone_Low INT NULL,
	Auto_Cone_Mid INT NULL,
	Auto_Cone_High INT NULL,
	Auto_Station INT NULL,
	Tele_Cube_Low INT NULL,
	Tele_Cube_Mid INT NULL,
	Tele_Cube_High INT NULL,
	Tele_Cone_Low INT NULL,
	Tele_Cone_Mid INT NULL,
	Tele_Cone_High INT NULL,
	Tele_Station INT NULL,
	Comments TEXT NULL
);

CREATE TABLE pitData(
	Scouter_Name TEXT NULL,
	Team_Number INT NULL,
	Competition TEXT NULL,
	Team_Name TEXT NULL,
	DriveTrain INT NULL,
	Can_Hold_Cone BOOLEAN NULL,
	Can_Hold_Cube BOOLEAN NULL,
	Scoring_Location_Capability INT NULL,
	Number_Of_Motors INT NULL,
	Number_Of_Batteries INT NULL,
	DriveTrain_Motor_Type TEXT NULL,
	Working_On TEXT NULL,
	Autos TEXT NULL,
	Comments TEXT NULL
);

CREATE TABLE superScout(
	Scouter_Name TEXT NULL,
	Competition TEXT NULL,
	Match_Number INT NULL,
	Team_Alliance INT NULL,
	Team_1 INT NULL,
	Team_2 INT NULL,
	Team_3 INT NULL,
	Comments TEXT NULL
);

CREATE TABLE fouls(
	Scouter_Name TEXT NULL, 
	Competition TEXT NULL,
	Match_Number INT NULL,
	Team_Alliance INT NULL,
	Team_Number INT NULL,
	Cause INT NULL,
	Comments TEXT NULL
);

CREATE TABLE dataAnalysis(
	Team_Number INT NOT NULL,
	Auto_Total_Average FLOAT,
	Auto_Total_Max FLOAT,
	Auto_Low_Average FLOAT,
	Auto_Low_Max INT,
	Auto_Mid_Average FLOAT,
	Auto_Mid_Max INT,
	Auto_High_Average FLOAT,
	Auto_High_Max INT,
	Auto_Balance_Frequency FLOAT,
	Tele_Pieces_Total_Average FLOAT,
	Tele_Pieces_Total_Max INT,
	Tele_Pieces_Low_Average FLOAT,
	Tele_Pieces_Low_Max INT,
	Tele_Pieces_Mid_Average FLOAT,
	Tele_Pieces_Mid_Max INT,
	Tele_Pieces_High_Average FLOAT,
	Tele_Pieces_High_Max INT,
	Tele_Cone_Total_Average FLOAT,
	Tele_Cone_Total_Max INT,
	Tele_Cone_Low_Average FLOAT,
	Tele_Cone_Low_Max INT,
	Tele_Cone_Mid_Average FLOAT,
	Tele_Cone_Mid_Max INT,
	Tele_Cone_High_Average FLOAT,
	Tele_Cone_High_Max INT,
	Tele_Cube_Total_Average FLOAT,
	Tele_Cube_Total_Max INT,
	Tele_Cube_Low_Average FLOAT,
	Tele_Cube_Low_Max INT,
	Tele_Cube_Mid_Average FLOAT,
	Tele_Cube_Mid_Max INT,
	Tele_Cube_High_Average FLOAT,
	Tele_Cube_High_Max INT,
	End_Dock_Frequency FLOAT,
	End_Balance_Frequency FLOAT,
	Average_Fouls FLOAT,
	Total_Pin_Fouls INT,
	Total_Disabled_Fouls INT,
	Total_Overextension_Fouls INT,
	Total_Inside_Robot_Fouls INT,
	PRIMARY KEY(Team_Number)
);
