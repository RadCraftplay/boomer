import re
from adapters.Adapter import Adapter

class RegexAdapter(Adapter):
    def __init__(self, conversation):
        self.conversation = conversation

    def can_parse(self, sentence: str) -> tuple[bool, float]:
        for regex in self.conversation.keys():
            if re.match(regex, sentence) is not None:
                return True, 1.0
        return False, 0.0

    def get_response(self, sentence: str) -> str:
        for regex, response_func in self.conversation.items():
            match = re.match(regex, sentence)
            if match is not None:
                return response_func(match)

        assert "Trying to process a statement, that can not be processed!"
