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
    DATA['API_KEY'] = os.getenv('OPENAI_API_KEY')
    DATA['MODEL'] = os.getenv('OPENAI_MODEL')
    DATA['TEMPERATURE'] = float(os.getenv('TEMPERATURE'))
    DATA['MAX_TOKENS'] = int(os.getenv('MAX_TOKENS'))
    DATA['SCRIPT_LANG'] = 'bash'
    DATA['OS'] = 'linux'
    DATA['LEVEL'] = 'admin'
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

    



    