
from adapters.Adapter import Adapter
from adapters.AdapterAdapter import AdapterAdapter
from common.AdapterBuilder import AdapterBuilder
from common.Configuration import ConfigurationProvider, JsonConfigurationProvider
from common.io.IOProviders import ConsoleIOProvider, IOProvider, SpeechIOProvider

from datetime import datetime, date

def main():
    config_provider : ConfigurationProvider = JsonConfigurationProvider("./config.json")
    io_provider : IOProvider = ConsoleIOProvider()

    config = config_provider.read()
    default_answer: str = config["default_answer"]
    use_wakeup_sentence: bool = config["use_wakeup_sentence"]
    wakeup_sentence: str = config["wakeup_sentence"]
    threshold: float = config["threshold"]



    builder = AdapterBuilder(threshold)
    builder.with_question("exit", exit)
    builder.with_questions_single_answer([
        "time",
        "what time is it",
        "current time"
    ], lambda: "The current time is {}".format(datetime.now().strftime("%H:%M")))
    builder.with_questions_single_answer([
        "date",
        "what day is today"
        "today's date"
    ], lambda: "Today is {}".format(datetime.now().strftime("%A, %B %d %Y")))
    adapter = builder.get()



    while True:
        if use_wakeup_sentence:
            while io_provider.read().lower() != wakeup_sentence:
                pass
            io_provider.write("What do you want me to do?")
        
        question = io_provider.read().lower()
        can_p, _ = adapter.can_parse(question)
        if (can_p):
            resp_func = adapter.get_response(question)
            io_provider.write(resp_func())
        else:
            io_provider.write(default_answer)

if __name__ == "__main__":
    main()