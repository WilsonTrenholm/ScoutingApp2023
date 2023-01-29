from flask import Flask, request
import mysql.connector
import atexit

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="my-secret-pw",
  database="rawData"
)

columns = ('Match_Number', 'Team_Number', 'Scouter_Name', 'Team_Alliance', 'Competition', 'Mobility', 'Show_Time', 'Auto_Cube_Low', 'Auto_Cube_Mid', 'Auto_Cube_High', 'Auto_Cone_Low', 'Auto_Cone_Mid', 'Auto_Cone_High', 'Auto_Station', 'Tele_Cube_Low', 'Tele_Cube_Mid', 'Tele_Cube_High', 'Tele_Cone_Low', 'Tele_Cone_Mid', 'Tele_Cone_High', 'Tele_Station', 'Comments')

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/data/matches', methods=['GET'])
def handle_get():
    # Handle GET request
    return getRawMatchData()

@app.route('/data/pits', methods=['GET'])
def handle_get4():
    request = "SELECT * FROM pitData"
    mycursor.execute(request)
    rows = mycursor.fetchall()

    # Format with column names
    return [dict(zip(columns, row)) for row in rows]


@app.route('/data/matches/team/<int:number>', methods=['GET'])
def handle_get_team(number):
    # Handle GET request
    return getRawMatchData(teamNumber=number)

@app.route('/data/matches/match/<int:number>', methods=['GET'])
def handle_get_match(number):
    # Handle GET request
    return getRawMatchData(matchNumber=number)

def getRawMatchData(**kwargs):
    request = "SELECT * FROM matchData"
    requestInput = []
    if 'teamNumber' in kwargs:
        request += " WHERE Team_Number=%s"
        requestInput.append(kwargs['teamNumber'])
    if 'matchNumber' in kwargs:
        request += " WHERE Match_Number=%s"
        requestInput.append(kwargs['matchNumber'])
    if 'sortBy' in kwargs:
        request += " ORDER BY %s"
        requestInput.append(kwargs['sortBy'])
    if 'limitTo' in kwargs:
        request += " LIMIT %s"
        requestInput.append(kwargs['limitTo'])
    print(requestInput,request)
    mycursor.execute(request,requestInput)
    rows = mycursor.fetchall()

    # Format with column names
    return [dict(zip(columns, row)) for row in rows]
              
                                                                                                                                                                                                                          

@app.route('/data/matches', methods=['POST'])
def handle_post():
    # Handle POST request
    formData = request.form
    # data = request.get_json()
    print(formData)

    # Insert all data into table
    mycursor.execute('INSERT INTO matchData({}) VALUES ({})'.format(
        ', '.join(formData.keys()),
        ', '.join(['%s'] * len(formData))
    ), [format_data(formData[key], key) for key in formData])

    mydb.commit()
    updateAnalysis(formData.get("Team_Number"))
    #for i in variable:
       # print(i)
    # Do something with the data
    return 'Data received'

@app.route('/data/pits', methods=['POST'])
def handle_post3():
    # Handle POST request
    formData = request.form
    # data = request.get_json()

    # Insert all data into table
    mycursor.execute('INSERT INTO pitData({}) VALUES ({})'.format(
        ', '.join(formData.keys()),
        ', '.join(['%s'] * len(formData))
    ), [format_data(formData[key], key) for key in formData])   

    mydb.commit()
    #for i in variable:
       # print(i)
    # Do something with the data
    return 'Data received'

def updateAnalysis(Team_Number):
    mycursor.execute('UPDATE dataAnalysis SET Auto_Low_Min = (SELECT MIN(Auto_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_Low_Average = (SELECT AVG(Auto_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_Low_Max = (SELECT MAX(Auto_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_Mid_Min = (SELECT MIN(Auto_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_Mid_Average = (SELECT AVG(Auto_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_Mid_Max = (SELECT MAX(Auto_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_High_Min = (SELECT MIN(Auto_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_High_Average = (SELECT AVG(Auto_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Auto_High_Max = (SELECT MAX(Auto_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Low_Min = (SELECT MIN(Tele_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Low_Average = (SELECT AVG(Tele_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Low_Max = (SELECT MAX(Tele_Cone_Low) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Mid_Min = (SELECT MIN(Tele_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Mid_Average = (SELECT AVG(Tele_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_Mid_Max = (SELECT MAX(Tele_Cone_Mid) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_High_Min = (SELECT MIN(Tele_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_High_Average = (SELECT AVG(Tele_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mycursor.execute('UPDATE dataAnalysis SET Tele_High_Max = (SELECT MAX(Tele_Cone_High) FROM matchData WHERE Team_Number = %s) WHERE Team = %s' ,  (Team_Number,Team_Number))
    mydb.commit()
    print('Update Analysis run')

# Convert data to proper format
def format_data(string, name):
    print("formatting data")
    print(string)
    print(name)
    if name in ('Scouter_Name', 'Competition', 'Comments'):
        return string
    if name in ('Mobility', 'Show_Time'):
        return bool(string)

    len(string)
    if len(string)==0:
        print(f"string='{string}',with no spaces is empty")
        return (0)
    else:
        print(f"string='{string}',with no spaces is not empty")
    return int(string)

# Close connections before exit
def exit_handler():
    mycursor.close()
    mydb.close()

atexit.register(exit_handler)

if __name__ == '__main__':
    app.run(debug=True)