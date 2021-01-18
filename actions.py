# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector, re

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         var1 = tracker.get_slot('inc_no')

         var2 = tracker.get_slot('levelOne')
         var3 = tracker.get_slot('comment_var')
         connection = mysql.connector.connect(host='localhost',database='chatbotDB',user='root',password='rootpass')
         cursor = connection.cursor()

         if var1 != None:
             incVar = var1.upper()
             if re.match(r'^INC',incVar) != None:
                 sql_query = "select incident_ID,Severity,CI,State,'Ticket Summary',Work_Notes from snow_inc where incident_ID = '" + incVar + "'"
                 cursor.execute(sql_query)
                 result = cursor.fetchone()
                 if result != None:
                     finalString = "Ticket summary:\nTicket Number: " + str(result[0]) + "\nSeverity: " + str(
                         result[1]) + "\nCI : " + str(result[2]) + "\nState: " + str(
                         result[3]) + "\nTicket Short Description: " + str(result[4]) + "\nWork Notes: " + str(
                         result[5])
                     dispatcher.utter_message(finalString)
                 else:
                     dispatcher.utter_message("Given Service Ticket could not be found, please check ticket number")
                 cursor.close()
             if re.match(r'^SR',incVar) != None:
                 sql_query = "select Task_Ref_No,Task_Priority,Task_Assigned_To,Task_CI,Task_Closed_Date,Task_State,Task_Summary,Task_Comments from snow_sr where Task_Ref_No = '" + incVar + "'"
                 cursor.execute(sql_query)
                 result = cursor.fetchone()
                 cursor.close()
                 if result != None:
                     finalString = "Ticket summary:\nTicket Number: " + str(result[0]) + "\nSeverity: " + str(result[1]) + "\nAssigned To: " + str(result[2]) + "\nCI : " + str(result[3]) + "Ticket Closed On: " + str(result[4]) + "\nState: " + str(result[5]) + "\nSR Short Description: " + str(result[6]) + "\nSR Comments: " + str(result[7])
                     dispatcher.utter_message(finalString)
                 else:
                     dispatcher.utter_message("Given Service Ticket could not be found, please check ticket number")
         return []

class ActionAddComment(Action):
    def name(self) -> Text:
        return "action_add_comment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        connection = mysql.connector.connect(host='localhost', database='chatbotDB', user='root', password='rootpass')
        cursor = connection.cursor()
        var1 = tracker.get_slot('inc_no')
        var2 = tracker.get_slot('levelOne')
        var3 = tracker.get_slot('comment_var')
        #connection = mysql.connector.connect(host='localhost', database='chatbotDB', user='root', password='rootpass')
        #cursor = connection.cursor()
        if var1 != None and var3 != None:
            incVar = var1.upper()
            if re.match(r'^INC', incVar) != None:
                sql_query = "select Work_Notes from snow_inc where incident_ID = '" + incVar + "'"
                cursor.execute(sql_query)
                result = cursor.fetchone()
                if result != None:
                    finalUpdate = str(result[0]) + " " + var3
                    #dispatcher.utter_message("to be added ++++++++++")
                    #dispatcher.utter_message(finalUpdate)
                    sql_query = "update snow_inc set Work_Notes = '%s' where incident_ID = '%s'" %(finalUpdate,incVar)
                    cursor.execute(sql_query)
                    connection.commit()
                    result = cursor.fetchone()
                    cursor.close()
                    #dispatcher.utter_message(str(result[0]))
                else:
                    dispatcher.utter_message("Given Service Ticket could not be found, please check ticket number")
            if re.match(r'^SR', incVar) != None:
                sql_query = "select Task_Comments from snow_sr where Task_Ref_No = '" + incVar + "'"
                cursor.execute(sql_query)
                result = cursor.fetchone()
                if result != None:
                    finalUpdate = str(result[0]) + " " + var3
                    sql_query = "update snow_sr set Task_Comments = '%s' where Task_Ref_No = '%s'" % (finalUpdate, incVar)
                    cursor.execute(sql_query)
                    connection.commit()
                    result = cursor.fetchone()
                    cursor.close()
                    # dispatcher.utter_message(str(result[0]))
                else:
                    dispatcher.utter_message("Given Service Ticket could not be found, please check ticket number")


        else:
            dispatcher.utter_message("Could not capture service ticket details")

        return []

class ActionSNReport(Action):
    def name(self) -> Text:
        return "action_SR_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        var1 = tracker.get_slot('rep_type')
        var2 = tracker.get_slot('rep_team')
        var3 = tracker.get_slot('rep_state')
        dispatcher.utter_message(var3+var2+var1)

        connection = mysql.connector.connect(host='localhost', database='chatbotDB', user='root', password='rootpass')
        cursor = connection.cursor()

        sql_query = "select Task_Ref_No from snow_sr where Task_State = '" + var3 + "'"
        dispatcher.utter_message(sql_query)
        cursor.execute(sql_query)
        result = cursor.fetchone()
        cursor.close()
        #if result != None:
        dispatcher.utter_message(str(result[0]))

        return []