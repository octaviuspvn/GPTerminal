from langcodes import *

def GetLanguageWithCode(lang_code: str) -> str:
    
    language = ""

    try:
        return Language.get(lang_code).display_name()
    except:
        return "Language code invalid, try again." 