import re
from typing import Callable
from adapters.Adapter import Adapter

class RegexAdapter(Adapter):
    def __init__(self, conversation):
        self.conversation : dict[str, Callable[[re.Match[str]], Callable[[], str]]] = conversation

    def can_parse(self, sentence: str) -> tuple[bool, float]:
        for regex in self.conversation.keys():
            if re.match(regex, sentence) is not None:
                return True, 1.0
        return False, 0.0

    def get_response(self, sentence: str) -> Callable[[], str]:
        for regex, response_func in self.conversation.items():
            match = re.match(regex, sentence)
            if match is not None:
                resp = response_func(match)
                return resp

        return lambda: "Error: Trying to process a statement, that can not be processed!"
    
    @staticmethod
    def with_single_response(response_parser: Callable[[re.Match[str]], Callable[[], str]], questions: set[str]):
        conversation = [{question: response_parser} for question in questions]
        return RegexAdapter(conversation)
