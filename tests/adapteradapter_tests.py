from ast import Tuple
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from adapters.RegexAdapter import RegexAdapter
from adapters.TfidfAdapter import TfidfAdapter
from common.AdapterBuilder import AdapterBuilder
from sys import exit

def repeatSentence(sentence: str) -> str:
    return "User typed: " + sentence

factory = AdapterBuilder(0.6)
factory.with_regexes_single_answer(["weather in (.*)$", "weather (.*)$"], lambda m: lambda: "Weather in {} is clear".format(m.group(1)))
factory.with_questions_single_answer(["do you like turtles?", "are you wise?", "weather"], lambda: "I like turtles")
factory.with_question("exit", exit)

adapter = factory.get()
def_ans = "Sorry, I don't understand"

while True:
    question = input(">")
    can_p, rating = adapter.can_parse(question)
    if (can_p):
        print(adapter.get_response(question)())
    else:
        print(def_ans)