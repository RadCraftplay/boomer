import re
from adapters.RegexAdapter import RegexAdapter

def describe_weather(m: re.Match[str]) -> str:
    return "The weather in {} is clear".format(m.group(1)) 

conversation = {"weather in (.*)$": describe_weather, "weather (.*)$": describe_weather}
adapter = RegexAdapter(conversation)

def_ans = "Sorry, I don't understand"

while True:
    question = input(">")
    can_p, rating = adapter.can_parse(question.lower())
    if (can_p):
        print(adapter.get_response(question.lower()))
    else:
        print(def_ans)