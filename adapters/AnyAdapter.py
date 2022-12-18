from typing import Callable

from adapters.Adapter import Adapter


class AnyAdapter(Adapter):

    def __init__(self, function: Callable[[str], str]):
        self.function = function

    def can_parse(self, sentence: str) -> tuple[bool, float]:
        return True, 1.0

    def get_response(self, sentence: str) -> Callable[[], str]:
        return lambda: self.function(sentence)