from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ActionExecuted

class ActionGetBibleVerse(Action):
    def name(self) -> Text:
        return "action_get_bible_verse"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract slots from the tracker
        book_number = tracker.get_slot("BookNumber")
        chapter = tracker.get_slot("Chapter")
        verse = tracker.get_slot("Verse")

        translation = "NKJV"  # You can modify this based on your requirement

        # Check if all required slots are filled
        if book_number and chapter and verse:
            try:
                # Construct the API URL
                api_url = f"https://bolls.life/get-verse/{translation}/{book_number}/{chapter}/{verse}/"
                
                # Fetch the verse from the API
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    verse_text = response.json().get("text")
                    if verse_text:
                        dispatcher.utter_message(text=verse_text)
                    else:
                        dispatcher.utter_message(text="Verse not found.")
                else:
                    dispatcher.utter_message(text=f"Failed to fetch verse. Status code: {response.status_code}")
            except Exception as e:
                dispatcher.utter_message(text=f"An error occurred: {str(e)}")
        else:
            dispatcher.utter_message(text="Please provide a valid book number, chapter, and verse.")

        return []

class ActionAskForVerse(Action):
    def name(self) -> Text:
        return "action_ask_for_verse"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the last action name to determine which slot to ask for
        last_action = tracker.latest_action_name

        if last_action is None or last_action == "action_ask_for_verse":
            # Return event to ask for the book number
            return [SlotSet("requested_slot", "BookNumber")]
        elif last_action == "action_store_book_number":
            # Return event to ask for the chapter number
            return [SlotSet("requested_slot", "Chapter")]
        elif last_action == "action_store_chapter_number":
            # Return event to ask for the verse number
            return [SlotSet("requested_slot", "Verse")]
        else:
            # Fallback to default message
            return [ActionExecuted("utter_default")]

class ActionStoreBookNumber(Action):
    def name(self) -> Text:
        return "action_store_book_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to store the book number slot
        book_number = next(tracker.get_latest_entity_values("BookNumber"), None)
        return [SlotSet("BookNumber", book_number)]

class ActionStoreChapterNumber(Action):
    def name(self) -> Text:
        return "action_store_chapter_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to store the chapter number slot
        chapter_number = next(tracker.get_latest_entity_values("Chapter"), None)
        return [SlotSet("Chapter", chapter_number)]

class ActionStoreVerseNumber(Action):
    def name(self) -> Text:
        return "action_store_verse_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to store the verse number slot
        verse_number = next(tracker.get_latest_entity_values("Verse"), None)
        return [SlotSet("Verse", verse_number)]


