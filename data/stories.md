## happy path service_1
* greet
  - utter_greet
* service
  - utter_selectService
* ticketModify
  - utter_serviceResponse
* capTicket
  - utter_modComment
* capComment
  - action_hello_world
* goodbye
  - utter_goodbye
 
## interactive_story_1
* greet
    - utter_greet
* service{"levelOne": "One"}
    - slot{"levelOne": "One"}
    - utter_selectService
* ticketModify
    - utter_serviceResponse
* capTicket{"inc_no": "INC77262"}
    - slot{"inc_no": "INC77262"}
    - utter_modComment
* capComment{"comment_var": "no issues found please close"}
    - slot{"comment_var": "no issues found please close"}
    - action_hello_world
* goodbye
    - utter_goodbye

## happy path service_2
* greet
  - utter_greet
* service
  - utter_selectService
* snapShot
  - utter_serviceResponse
* capTicket
  - action_hello_world
* goodbye
  - utter_goodbye  

## interactive_story_2
* greet
    - utter_greet
* service{"levelOne": "One"}
    - slot{"levelOne": "One"}
    - utter_selectService
* snapShot
    - utter_serviceResponse
* capTicket{"inc_no": "kb172727"}
    - slot{"inc_no": "kb172727"}
    - action_hello_world
* goodbye
    - utter_goodbye
