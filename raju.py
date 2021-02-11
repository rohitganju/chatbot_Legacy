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
                 cursor.close()
             if re.match(r'^SR',incVar) != None:
                 sql_query = "select Severity from snow_SR where incident_ID = '" + var1 + "'"
                 cursor.execute(sql_query)
                 result = cursor.fetchone()
                 cursor.close()
         return []

class ActionAddComment(Action):
    def name(self) -> Text:
        return "action_add_comment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        var1 = tracker.get_slot('inc_no')

        var2 = tracker.get_slot('levelOne')
        var3 = tracker.get_slot('comment_var')
        #connection = mysql.connector.connect(host='localhost', database='chatbotDB', user='root', password='rootpass')
        #cursor = connection.cursor()
        dispatcher.utter_message("**********At adding comment section")

        return []