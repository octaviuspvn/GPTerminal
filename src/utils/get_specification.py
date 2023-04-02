from os import getenv, path
from platform import system

import argparse

from src.utils import errors

from configparser import ConfigParser

BRAND_SCHEMA = "\n[GPTerminal] -"

DATA = {
    "API_KEY" : "",
    "MODEL" : "",
    "TEMPERATURE" : "",
    "MAX_TOKENS" : ""
}

def specs() -> dict[str, str] or None:

    # Verify if OPEN_API_KEY is available
    DATA['API_KEY'] = getenv('OPENAI_API_KEY')

    file_path = path.abspath(path.join(path.dirname(__file__), "..", "settings", "settings.ini"))

    try:
        config = ConfigParser()
        config.read(file_path)
        
        # SETTINGS SECTION IS "DEFAULT"
        LOCATION = 'DEFAULT'

        # IF THE USER ACTIVE THE CUSTOM MODE CHANGE THE LOCATION SECTION
        if config.getboolean('CUSTOM', 'USE_CUSTOM') == True:
            LOCATION = 'CUSTOM'

        # GET USER SETTINGS FROM THE CONFIG INI
        DATA['MODEL'] = config.get(LOCATION, 'MODEL').lower()
        DATA['TEMPERATURE'] = config.getfloat(LOCATION, 'TEMPERATURE')
        DATA['MAX_TOKENS'] = config.getint(LOCATION, 'MAX_TOKENS')
        DATA['LEVEL'] = config.get(LOCATION, 'PERMISSION_LEVEL').lower()
        DATA['SCRIPT_LANG'] = config.get(LOCATION, 'SCRIPT_LANG').lower()
        DATA['RESPONSES'] = config.getint(LOCATION, 'NUMBER_OF_RESPONSES')
        DATA['EXPLICIT_MODE'] = config.getboolean(LOCATION, 'EXPLICIT_MODE')

         # IF THE USER SETTINGS WANT TO SET ITS OWN OPERATING SYSTEM
        enable_custom_os = config.getboolean('CUSTOM', 'CUSTOM_OS')
        if enable_custom_os:
            DATA['OS'] = config.get('CUSTOM','OS')
        if not enable_custom_os:
            DATA['OS'] = system().upper()
        else:

            valid_os = ['LINUX', 'WINDOWS', 'MAC']
            custom_os = DATA['OS'].upper()

            if custom_os in valid_os:
                if not DATA['SCRIPT_LANG']:
                    if custom_os in ['LINUX', 'MAC']:
                        data['SCRIPT_LANG'] = 'BASH'
                    else:
                        data['SCRIPT_LANG'] = 'SHELL'
            else:
                errors.ConfigError('CUSTOM_OS', valid_os, errors.DOCUMENTATION['OS'])

        for key, value in DATA.items():
            if not value and key != 'API_KEY':
                errors.ConfigError(key, "https://platform.openai.com/docs/api-reference/", errors.DOCUMENTATION[key])

        # THIS CONFIGS ARE VALIDATED VIA THE API ENDPOINT, ONLY WE ENSURE THAT IT CONTAINS A VALUE.
        if not DATA['API_KEY']:
            errors.ErrorAPIKEY()
        
        return DATA

    except Exception as error:
        print(str(error))
