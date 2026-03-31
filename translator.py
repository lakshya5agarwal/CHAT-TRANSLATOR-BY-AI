# simple chat translator

from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException
lang_codes = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ar": "Arabic",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
    "pt": "Portuguese",
    "it": "Italian",
    "tr": "Turkish",
    "bn": "Bengali",
    "ur": "Urdu",
    "ta": "Tamil",
    "te": "Telugu",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "auto": "Auto-detect",
}
def show_langs():
    print("\nHere are some common language codes you can use:")
    print("-" * 40)
    for code, name in lang_codes.items():
        print(f"  {code:<12} {name}")
    print("\n  Tip: Any language code works, not just these.")
    print("-" * 40)


def do_translate(text, src, tgt):
    t = GoogleTranslator(source=src, target=tgt)
    return t.translate(text)


def ask_lang(prompt, fallback=""):
    suffix = f" (default: {fallback})" if fallback else ""
    val = input(f"{prompt}{suffix}: ").strip().lower()
    if not val:
        return fallback
    return val


def pick_languages():
    print("\nSet your languages. Use 'auto' if you want it to detect the source.")
    src = ask_lang("Source language code", "auto")
    tgt = ask_lang("Target language code", "en")
    return src, tgt


def show_help():
    print("\nAvailable commands:")
    print("  lang    - show language codes")
    print("  swap    - flip source and target")
    print("  reset   - choose new languages")
    print("  history - see past translations")
    print("  quit    - exit the program\n")


def run():
    print("\n--- Chat Language Translator ---")
    print("Translate anything, from any language to any language.")
    print("Type 'help' anytime to see commands.\n")

    src_lang, tgt_lang = pick_languages()
    history = []

    print(f"\nReady! Translating from [{src_lang}] to [{tgt_lang}]")
    print("Go ahead and type something...\n")

    while True:
        try:
            msg = input("You: ").strip()

            if not msg:
                continue

            cmd = msg.lower()

            if cmd in ("quit", "exit", "q"):
                print("\nBye! See you next time.\n")
                break

            elif cmd == "help":
                show_help()

            elif cmd == "lang":
                show_langs()

            elif cmd == "swap":
                src_lang, tgt_lang = tgt_lang, src_lang
                print(f"Swapped. Now going from [{src_lang}] to [{tgt_lang}]\n")

            elif cmd == "reset":
                src_lang, tgt_lang = pick_languages()
                print(f"\nUpdated. Now going from [{src_lang}] to [{tgt_lang}]\n")

            elif cmd == "history":
                if not history:
                    print("Nothing translated yet.\n")
                else:
                    print("\nYour translation history:")
                    for i, item in enumerate(history, 1):
                        print(f"  {i}. Original  [{item['src']}]: {item['original']}")
                        print(f"     Translated [{item['tgt']}]: {item['result']}")
                    print()

            else:
                result = do_translate(msg, src_lang, tgt_lang)
                print(f"Bot: {result}\n")

                history.append({
                    "src": src_lang,
                    "tgt": tgt_lang,
                    "original": msg,
                    "result": result
                })

        except LanguageNotSupportedException:
            print("Hmm, that language code doesn't seem right.")
            print("Type 'lang' to see a list of valid codes.\n")

        except Exception as e:
            print(f"Something went wrong: {e}")
            print("Make sure you're connected to the internet and the language codes are correct.\n")


if __name__ == "__main__":
    run()