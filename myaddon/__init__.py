import requests
import json
from aqt import mw
from aqt import QAction
from aqt.utils import showInfo, getText


def create_new_deck(name):
    # Make the API call to create the new deck
    payload = {
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": name
        }
    }

   #I'm not very proud of it but it works
    try:
        response = requests.post("http://127.0.0.1:8765", json=payload, timeout=1)
        response_json = json.loads(response.text)
        error = response_json.get("error")
        if error == '':
            showInfo("Error: " + error)
            return
    except requests.exceptions.RequestException:
        showInfo("Deck '%s' has been created." % name)


def create_new_deck_action():
    name, ok = getText("Enter the name of the new deck:")
    if ok:
        create_new_deck(name)
    else:
        showInfo("Deck was not created.")


action = QAction("Create New Deck", mw)
action.triggered.connect(create_new_deck_action)
mw.form.menuTools.addAction(action)
