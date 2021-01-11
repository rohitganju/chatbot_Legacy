import mysql.connector

connection = mysql.connector.connect(host='localhost',database='chatbotDB',user='root',password='rootpass')
cursor = connection.cursor()
sql_query = "select Severity, State from snow_inc where incident_ID = 'INC1234567'"
cursor.execute(sql_query)
result = cursor.fetchone()
new1 = ' '.join(result)
finalString = "Ticket summary:\nTicket Number: INC1234567\nSeverity: "+str(result[0])
print(finalString)
cursor.close()