from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSummarizeUserState(Action):
    def name(self) -> Text:
        return "action_summarize_user_state"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Collect slot values
        mood_is_good = tracker.get_slot("mood_is_good")
        appetite_is_good = tracker.get_slot("appetite_is_good")
        sleep_is_good = tracker.get_slot("sleep_is_good")

        # Create a summary based on slot values
        mood_summary = "Your mood is good." if mood_is_good else "It seems you're feeling a bit down."
        appetite_summary = "Your appetite is good." if appetite_is_good else "Your appetite has been low."
        sleep_summary = "You've been sleeping well." if sleep_is_good else "It seems your sleep hasn't been great."

        # Combine the summary and send it to the user
        summary = f"{mood_summary} {appetite_summary} {sleep_summary}"
        dispatcher.utter_message(text=summary)

        # Reset slots after conversation ends
        return [
            SlotSet("mood_is_good", None),
            SlotSet("poor_mood_cause", None),
            SlotSet("appetite_is_good", None),
            SlotSet("poor_appetite_cause", None),
            SlotSet("sleep_is_good", None),
            SlotSet("poor_sleep_cause", None),
        ]
