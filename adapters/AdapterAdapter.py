from typing import Callable

from adapters.Adapter import Adapter


class AdapterAdapter(Adapter):

    def __init__(self, adapters: list[Adapter]):
        self.adapters = adapters

    def can_parse(self, sentence: str) -> tuple[bool, float]:
        can_p = False
        max_surtenty = 0.0

        for adapter in self.adapters:
            can_p_cur, surtenty = adapter.can_parse(sentence)
            if can_p_cur:
                if max_surtenty < surtenty:
                    max_surtenty = surtenty
                    can_p = True
        
        return can_p, max_surtenty
        

    def get_response(self, sentence: str) -> Callable[[], str]:
        used_adapter = None
        max_surtenty = 0.0

        for adapter in self.adapters:
            can_p_cur, surtenty = adapter.can_parse(sentence)
            if can_p_cur:
                if max_surtenty < surtenty:
                    max_surtenty = surtenty
                    used_adapter = adapter
        
        if used_adapter is None:
            return lambda: "Error: Trying to process a statement, that can not be processed!"

        return used_adapter.get_response(sentence)
