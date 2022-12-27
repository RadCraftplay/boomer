# Boomer

## Requirements

- Windows (Linux will probably work if you modify ```SpeechProvider.__init__().set_voice``` function to detect language correctly. Had to implement it that way to set language on Windows 11)
- Python (>=3.9 should work fine, the older versions were not tested)

## Quick start

1. (Optional) Create and activate Python virtual environment:

On Windows:
```console
$ python -m venv ./.venv
$ .\.venv\Scripts\Activate.ps1
```

On Linux:
```console
$ python -m venv ./.venv
$ source ./.venv/bin/activate
```

2. Install dependencies

```console
$ pip install -r requirements.txt
```

3. Create configuration file (```config.json```) in the project directory:

```json
{
    "default_answer": "Sorry, I don't understand",
    "threshold": 0.6,
    "use_wakeup_sentence": true,
    "wakeup_sentence": "okay boomer",
    "use_console_io": false,
    "weather":
    {
        "openweatherapi_key": "<YOUR OPENWEATHERAPI KEY>",
        "default_city": "London"
    },
    "search_directory": "./library"
}
```

- **default_answer**: Bot's anster when user input doesn't match any adapter
- **threshold**: TF-IDF adapter detection threshold
- **use_wakeup_sentence**: If ```true```, bot will wait for user to say ```wakeup_sentence``` before trying to detect commands 
- **wakeup_sentence**: Sentence starting bot listening for command
- **use_console_io**: If ```true``` will use console input/output instead of voice interface
- **weather**:
    - **openweatherapi_key**: Your OpenWeatherAPI key (required for weather-related commands)
    - **default_city**: City used if user does not provide any when asking for weather
- **search_directory**: Directory containing the files searched using "search" command

4. Download stop words used by nltk

```console
$ python setup.py
```

5. Start assistant

```console
$ python main.py
```
