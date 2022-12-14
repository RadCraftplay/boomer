from ast import Tuple
from adapters import Adapter, TfidfAdapter

conversation = [["Hello", "Hi"],["How are you?", "I am fine"], ["What is your name?", "My name is HAL" ]]
adapter = TfidfAdapter.TfidfAdapter(conversation, 0.6)

ans_thr = 0.6
def_ans = "Sorry, I don't understand"

while True:
    question = input(">")
    can_p, rating = adapter.can_parse(question)
    if (can_p):
        print(adapter.get_response(question))
    else:
        print(def_ans)