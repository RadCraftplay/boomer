
from ast import Tuple
from Adapter import Adapter


class TdidfAdapter(Adapter):
    def can_parse(sentence) -> Tuple[bool, float]:
        pass

    def get_response(sentence) -> str:
        pass
