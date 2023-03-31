import sys
import os

from utils import get_specification as gs
from network import gpt_call as gpt


BRAND_SCHEMA = "[GPTerminal] -\n"

def main():

    DATA = gs.specs()

    if not DATA:
        print(f"{BRAND_SCHEMA} try to provide all required data, type --help to more info.")
    # Getting the prompt text to generate bash code 
    prompt = " ".join(sys.argv[1:])

    gpt.promptDataToGPT(prompt, DATA['API_KEY'], DATA)
    
if __name__ == "__main__":
    main()