
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from adapters.RegexAdapter import RegexAdapter
from adapters.TfidfAdapter import TfidfAdapter

class AdapterAdapterBuilder():
    def __init__(self):
        self.adapter_adapters : list[AdapterAdapter] = []
        self.regex_adapters : list[RegexAdapter] = []
        self.tfidf_adapters : list[TfidfAdapter] = []

    def get(self):
        adapters : list[Adapter] = []

        for adapter in self.regex_adapters:
            adapters.append(adapter)
        
        for adapter in self.tfidf_adapters:
            adapters.append(adapter)

        for adapter in self.adapter_adapters:
            adapters.append(adapter)
        
        return AdapterAdapter(adapters)
    
    def with_adapter_adapter(self, adapter_adapter : AdapterAdapter):
        self.adapter_adapters.append(adapter_adapter)
    
    def with_regex_adapter(self, regex_adapter : RegexAdapter):
        self.regex_adapters.append(regex_adapter)
    
    def with_tfidf_adapter(self, tfidf_adapter : TfidfAdapter):
        self.tfidf_adapters.append(tfidf_adapter)