import mysql.connector
import re

connection = mysql.connector.connect(host='localhost',database='chatbotDB',user='root',password='rootpass')
cursor = connection.cursor()
sql_query = "select incident_ID,Severity,CI,State,'Ticket Summary',Work_Notes from snow_inc where incident_ID = 'INC18347'"
cursor.execute(sql_query)
result = cursor.fetchone()
if result != None:
    finalString = "Ticket summary:\nTicket Number: " + str(result[0]) + "\nSeverity: " + str(result[1]) + "\nCI : " + str(result[2]) + "\nState: " + str(result[3]) + "\nTicket Short Description: " + str(result[4]) + "\nWork Notes: " + str(result[5])
    print(finalString)
cursor.close()

