
from ast import Tuple
from Adapter import Adapter


class RegexAdapter(Adapter):
    def can_parse(self, sentence: str) -> Tuple[bool, float]:
        pass

    def get_response(self, sentence: str) -> str:
        pass
