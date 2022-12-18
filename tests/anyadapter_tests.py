from ast import Tuple
from adapters import Adapter, AnyAdapter

def repeatSentence(sentence: str) -> str:
    return "User typed: " + sentence

adapter = AnyAdapter.AnyAdapter(repeatSentence)

def_ans = "Sorry, I don't understand"

while True:
    question = input(">")
    can_p, rating = adapter.can_parse(question)
    if (can_p):
        print(adapter.get_response(question)())
    else:
        print(def_ans)