
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from adapters.RegexAdapter import RegexAdapter
from adapters.TfidfAdapter import TfidfAdapter

class AdapterAdapterBuilder():
    def __init__(self):
        self.__adapter_adapters : list[AdapterAdapter] = []
        self.__regex_adapters : list[RegexAdapter] = []
        self.__tfidf_adapters : list[TfidfAdapter] = []

    def get(self):
        adapters : list[Adapter] = []

        for adapter in self.__regex_adapters:
            adapters.append(adapter)
        
        for adapter in self.__tfidf_adapters:
            adapters.append(adapter)

        for adapter in self.__adapter_adapters:
            adapters.append(adapter)
        
        return AdapterAdapter(adapters)
    
    def with_adapter_adapter(self, adapter_adapter : AdapterAdapter):
        self.__adapter_adapters.append(adapter_adapter)
        return self
    
    def with_regex_adapter(self, regex_adapter : RegexAdapter):
        self.__regex_adapters.append(regex_adapter)
        return self
    
    def with_tfidf_adapter(self, tfidf_adapter : TfidfAdapter):
        self.__tfidf_adapters.append(tfidf_adapter)
        return self