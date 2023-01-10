import json
import urllib.request


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']





deckInput = input("What deck should be cards moved from?\n > ")
idCards = invoke("findCards", query="deck:" + deckInput)

deckMovedFrom = invoke("getDecks", cards=idCards)


newDeck = input("In what Deck should be the cards moved?\n > ")
result = invoke('changeDeck', cards=idCards, deck=newDeck)

invoke("deleteDecks", decks=deckMovedFrom, cardsToo="true")




