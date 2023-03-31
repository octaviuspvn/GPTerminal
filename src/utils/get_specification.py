import os
import argparse
import platform

DATA = {
    "API_KEY" : "",
    "MODEL" : "",
    "TEMPERATURE" : "",
    "MAX_TOKENS" : ""
}

DOCUMENTATION = {
    "API_KEY" : "The Open AI API KEY for GPTerminal usage.",
    "MODEL" : "The AI Model of Open AI models [default: text-davinci-003]",
    "TEMPERATURE" : "The level of randomness that your script code contain [default: 0.8]",
    "MAX_TOKENS" : "The quantity of max tokens use in this api call [default: 200]" 
}

def specs() -> dict[str, str] or None:
    # Verify if OPEN_API_KEY is available
    API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL = os.getenv('OPENAI_MODEL')
    TEMPERATURE = os.getenv('OPENAI_TEMPERATURE')
    MAX_TOKENS = os.getenv('OPENAI_MAX_TOKENS')

    DATA_TO_SET = [API_KEY, MODEL, TEMPERATURE, MAX_TOKENS]
    # run through DATA dictionary keys
    for n, key in enumerate(DATA.keys()):
        DATA[key] = DATA_TO_SET[n]
        # if data is not provided via path, get it via cli flags.
        if not DATA[key]:
            DATA[key] = getArguments(key)
            # if data still not provided, return error.
            if not DATA[key]:
                return None

    DATA['os'] = platform.platform()
    # if all data is available
    return DATA

def getArguments(argument_to_copy: str) -> str:
    
    """
    Get data values via CLI Flags.

    This is the last instance if the data isn't provided via environment path.

    return: string
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(f"-{argument_to_copy[0:2]}",argument_to_copy, help=DOCUMENTATION[argument_to_copy])
    
    args = parser.parse_args()

    return args.argument_to_copy

    



    