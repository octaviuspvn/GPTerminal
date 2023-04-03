import re
import os
from configparser import ConfigParser

BRAND_SCHEMA = "[GPTerminal] -\n"

def find_macro(text: str):
    pattern = r"\b\w+\$"  # regular expression to match words endswith "$"
    matches = re.findall(pattern, text)
    words = [match[:-1] for match in matches]
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "settings", "macros.ini"))

    MACROS = {}

    try:
        # TRY TO REPLACE MACROS FOR ITS DEFINITION IN /SETTINGS/MACRO.INI FILE
        config = ConfigParser()
        config.read(file_path)

        for word in words:
            try:
                MACROS[str(word)] =  config.get('MACROS', word)
            except:
                continue
        
        formatted_text = ""
        for word in text.split():
            if word[-1] == "$":
                try:
                    formatted_text += MACROS[word[:-1]] + " "
                except:
                    formatted_text += word + " "
            else:
                formatted_text += word + " "

        return formatted_text
    except Exception as e:
        print(f"{BRAND_SCHEMA} Error in MACROS: {e}")
        return ""