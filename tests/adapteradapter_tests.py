from ast import Tuple
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from adapters.AnyAdapter import AnyAdapter
from adapters.RegexAdapter import RegexAdapter
from adapters.TfidfAdapter import TfidfAdapter
from sys import exit

def repeatSentence(sentence: str) -> str:
    return "User typed: " + sentence

adapter = AdapterAdapter([
    RegexAdapter.with_single_response(lambda m: lambda: "Weather in {} is clear".format(m.group(1)), ["weather in (.*)$", "weather (.*)$"]),
    TfidfAdapter.with_single_response(0.6, lambda: "I like turtles", ["do you like turtles?", "are you wise?", "weather"]),
    TfidfAdapter([ ("exit", exit) ], 0.6)
])
def_ans = "Sorry, I don't understand"

while True:
    question = input(">")
    can_p, rating = adapter.can_parse(question)
    if (can_p):
        print(adapter.get_response(question)())
    else:
        print(def_ans)