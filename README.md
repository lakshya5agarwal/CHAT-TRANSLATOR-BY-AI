# Chat Language Translator

A simple language translator running in the terminal. Type anything, and it will translate it in real time using Google Translate. No API key required.

---

## What it does

- Translate any text into any language
- Translate any language into any other language
- Auto detects the language if you don't know the language
- Keeps track of all the translation history
- Allows you to change the language

---

## Requirements

- Python 3.7+
- Internet connectivity

Only one package is required. It can be installed using pip.

```bash
pip install deep-translator
```

---

## Usage

```bash
python chat_translator_human.py
```

After running the script, it will prompt you to enter the language. Type the language code. For example, if you want to translate to Hindi, type `hi`. If you don't know the language, type `auto`.

---

## Usage

| Command   | Description                                 |
|-----------|---------------------------------------------|
| `help`    | List all the commands                       |
| `lang`    | List the language codes                     |
| `quit`    | Quit the application                        |
| `clear`   | Clear the translation history              |
| `history` | List the translation history              |
| `change lang` | Change the language to any language       |
| `exit`   | Exit the application                       |
| `clear history`| Clear the translation history            |
| `history` | List the translation history              |
| `change lang`| Change the language to any language       |
| `exit`   | Exit the application                       |
| `clear history`| Clear the translation history            |
| `history` | List the translation history              |
| `change lang`| Change the language to any language       |
| `exit`   | Exit the application                       |
| `
| `swap`    | Flip source and target language       |
| `reset`   | Choose new source and target language |
| `history` | View all translations from this session |
| `quit`    | Exit the program                      |

---

## Example session

```
--- Chat Language Translator ---
Translate anything, from any language to any language.
Type 'help' anytime to see commands.

Set your languages. Use 'auto' if you want it to detect the source.
Source language code (default: auto): auto
Target language code (default: en): hi

Ready! Translating from [auto] to [hi]
Go ahead and type something...

You: Hello, how are you?
Bot: नमस्ते, आप कैसे हैं?

You: swap
Swapped. Now going from [hi] to [auto]

You: quit
Bye! See you next time.
```

---

## Supported Languages (common ones)

| Code    | Language             |
|---------|----------------------|
| en      | English              |
| hi      | Hindi                |
| mr      | Marathi              |
| fr      | French               |
| es      | Spanish              |
| de      | German               |
| ar      | Arabic               |
| zh-CN   | Chinese (Simplified) |
| ja      | Japanese             |
| ko      | Korean               |
| ru      | Russian              |
| pt      | Portuguese           |
| it      | Italian              |
| bn      | Bengali              |
| ur      | Urdu                 |
| ta      | Tamil                |
| te      | Telugu               |
| gu      | Gujarati             |
| pa      | Punjabi              |
| auto    | Auto-detect          |

Any ISO 639 language code will work, not just those above.

***

## Project Structure

```
chat_translator_human.py   # This is the script, run this
README.md                  # This is what you're reading
```

***

## How it works

This script uses a library called `deep-translator` that uses Google Translate's free API. This means that every time you input a message, it will be sent to Google Translate, and then we'll print out the result.

***

## Known limitations

- Requires internet, cannot be run offline
- Long messages will be cut off
- History will not be saved when you close the application

***

## Possible improvements (if you want to improve this)

- Save history to a `.txt` or `.csv` file
- Create a GUI application using `tkinter` to create a simple GUI
- Add batch translation support, where you can input a text file to translate
- Add a confidence level or a detected language when using `auto`

***

## License

Free to use for personal and educational projects.
