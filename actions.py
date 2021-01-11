# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector

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
         sql_query = "select Severity from snow_inc where incident_ID = '"+var1+"'"
         cursor.execute(sql_query)
         result = cursor.fetchone()
         if var1 != None:
             dispatcher.utter_message("******************")
             dispatcher.utter_message(str(result))
         cursor.close()
         #if var1 != None and var2 != None and var3 != None:
          #  dispatcher.utter_message("---- test message---------")
          #  dispatcher.utter_message(var1+var2+var3)
         #else:
          #   dispatcher.utter_message("********All var not set*******")
         return []
