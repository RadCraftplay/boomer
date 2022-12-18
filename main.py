
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from common.CommonAdapters import get_exit_adapter
from common.Configuration import ConfigurationProvider, JsonConfigurationProvider
from common.io.IOProviders import ConsoleIOProvider, IOProvider

config_provider : ConfigurationProvider = JsonConfigurationProvider("./config.json")
io_provider : IOProvider = ConsoleIOProvider()

config = config_provider.read()
default_answer: str = config["default_answer"]
threshold: float = config["threshold"]

adapter : Adapter = AdapterAdapter([
    get_exit_adapter(threshold)
])


while True:
    question = io_provider.read()
    can_p, rating = adapter.can_parse(question.lower())
    if (can_p):
        resp_func = adapter.get_response(question.lower())
        io_provider.write(resp_func())
    else:
        io_provider.write(default_answer)