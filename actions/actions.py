
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker ,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from databaseintegeration import DataUpdate
from rasa_sdk.types import DomainDict
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "user_detail_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

  
        required_slots=['budget','area','name','email','phone','timeline','location']
        for slot_name in required_slots:
            if  tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot",slot_name)]
            
        return [SlotSet("requested_slot",None)]
        
# class ActionSubmit(Action):
#         def name(self) -> Text:
#             return "action_submit"
#         async def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             DataUpdate(tracker.get_slot('budget'))
            # ,tracker.get_slot('area')
            # ,tracker.get_slot('name')
            # ,tracker.get_slot('email')
            # ,tracker.get_slot("budget")
            # ,tracker.get_slot("phone")
            # ,tracker.get_slot("timeline")
            # ,tracker.get_slot("location"))
            # dispatcher.utter_message("Thanks for the valuable information. ")
            # return() 

class ActionCarousel(Action):

    def name(self) -> Text:
        return "action_carousels"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message= {
            "type": "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"BUYING",
                        "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/modern-residential-building_1268-14735.jpg?t=st=1650363015~exp=1650363615~hmac=6cbe53eb5ce6fbc48ee2042826d0b03afcd0a2bc82ba5b307eac9def1f5635ed&w=1380",
                        "buttons": [
                            {
                                "title": "Buy Property",
                                "payload": "Buy Property",
                                "type": "postback"
                        }                   
                        ]
                    },
                    {
                        "title":"SELLING",
                        "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/house-isolated-field_1303-23773.jpg?t=st=1650363112~exp=1650363712~hmac=95ac044a03495d5542981df1a31c94942fb4bc51205b70c74d9e84ad25cea6cf&w=1380",
                        "buttons": [
                            {
                                "title": "Sell Property",
                                "payload": "Sell Property",
                                "type": "postback"
                        }
                        ]
                    },
                    
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return 


class ActionPropertyType(Action):

    def name(self) -> Text:
        return "action_property_type"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message= {
            "type": "template",
            "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Residential Real Estate",
                        # "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/jumeirah-beach-residence_158595-1979.jpg?t=st=1650363625~exp=1650364225~hmac=7d79b7520c0c1589593c45666bee8e1948de5b3cfd044a103d8a36ad25e7c13c&w=1380",
                        "buttons": [
                            {
                                "title": "Residential Real Estate",
                                "payload": "Residential Real Estate",
                                "type": "postback"
                        }                   
                        ]
                    },
                    {
                        "title":"Commercial Real Estate",
                        # "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/group-business-partners-formal-suits-pointing-office-building-meeting-outdoors-discussing-real-property-back-view-commercial-real-estate-concept_74855-7313.jpg?t=st=1650363673~exp=1650364273~hmac=cc6942cdbd60fa83e6a43fb7384d19a00f939799837c26e1a03b980f1bdc3211&w=1380",
                        "buttons": [
                            {
                                "title": "Commercial Real Estate",
                                "payload": "Commercial Real Estate",
                                "type": "postback"
                        }
                        ]
                    },
                    {
                        "title":"Industrial Real Estate",
                        # "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/industrial-park-factory-building-warehouse_1417-1933.jpg?t=st=1650363731~exp=1650364331~hmac=7a7195649a0bfcd1954a23674ad7ff108f7330488ad8935c38c33a697a063032&w=1480",
                        "buttons": [
                            {
                                "title": "Industrial Real Estate",
                                "payload": "Industrial Real Estate",
                                "type": "postback"
                        }                   
                        ]
                    },
                    {
                        "title":"Investing in Land",
                        # "subtitle": "PROPERTY",
                        "image_url": "https://img.freepik.com/free-photo/aerial-shot-beautiful-green-farmland_181624-33012.jpg?t=st=1650363769~exp=1650364369~hmac=e6bfe5cc7da00137a31e71a15bfd2d5dbcabe2e51e9cf2dfd0ac0442cdb4f3e9&w=1060",
                        "buttons": [
                            {
                                "title": "Investing in Land",
                                "payload": "Investing in Land",
                                "type": "postback"
                        }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return 