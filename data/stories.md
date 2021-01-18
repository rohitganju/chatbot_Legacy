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
  - action_add_comment
  - utter_confirm_commit
  - action_hello_world
  - utter_selectService
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
    - action_add_comment
    - utter_confirm_commit
    - action_hello_world
    - utter_selectService
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
  - utter_selectService
* ticketModify
  - utter_serviceResponse
* capTicket
  - utter_modComment
* capComment
  - action_add_comment
  - utter_confirm_commit
  - action_hello_world
  - utter_selectService
* goodbye
  - utter_goodbye  


## interactive_story_1
* greet
    - utter_greet
* service{"levelOne": "One"}
    - slot{"levelOne": "One"}
    - utter_selectService
* snapShot
    - utter_serviceResponse
* capTicket{"inc_no": "INC1234567"}
    - slot{"inc_no": "INC1234567"}
    - action_hello_world
    - utter_selectService
* ticketModify
    - utter_serviceResponse
* capTicket{"inc_no": "INC1234567"}
    - slot{"inc_no": "INC1234567"}
    - utter_modComment
* capComment{"comment_var": "no issues found please close"}
    - slot{"comment_var": "no issues found please close"}
    - action_add_comment
    - utter_confirm_commit
    - action_hello_world
    - utter_selectService
* goodbye
    - utter_goodbye
    
* greet
  - utter_greet
* report
  - utter_selectReport
* service_now
  - utter_reportResponse  
* report_query
  - utter_confirm_fetch
  - action_SR_report
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* report{"levelOne": "Two"}
    - slot{"levelOne": "Two"}
    - utter_selectReport
* service_now
    - utter_reportResponse
* report_query{"rep_type": "SR", "rep_team": "trade l2", "rep_state": "open"}
    - slot{"rep_state": "open"}
    - slot{"rep_team": "trade l2"}
    - slot{"rep_type": "SR"}
    - utter_confirm_fetch
    - action_SR_report
    - utter_selectReport
* goodbye
   - utter_goodbye

