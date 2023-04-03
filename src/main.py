import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from configparser import ConfigParser

from utils import get_specification as gs
from utils import search_for_macro as sfm
from network import gpt_call as gpcall

BRAND_SCHEMA = "[GPTerminal] -\n"

def main():

    DATA = gs.specs()
    if not DATA:
        print(f"{BRAND_SCHEMA} try to provide all required data, type --help to more info.")
    # Getting the prompt text to generate bash code 

    prompt = " ".join(sys.argv[1:])
    if prompt:
        formatted_text = sfm.find_macro(prompt)
        if len(formatted_text) > 1:
            gpcall.promptDataToGPT(formatted_text, DATA)
        else:
            gpcall.promptDataToGPT(prompt, DATA)
    else:
        print(f"{BRAND_SCHEMA} Please provide an action to perform.")
    
if __name__ == "__main__":
    main()