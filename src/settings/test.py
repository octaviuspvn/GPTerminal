from configparser import ConfigParser

DATA = {}

config = ConfigParser()
config.read("settings.ini")

if config.getboolean('CUSTOM', 'USE_CUSTOM') == True:
    LOCATION = 'CUSTOM'
else:
    LOCATION = 'DEFAULT'

DATA['MODEL'] = config.get(LOCATION, 'MODEL').lower()
DATA['TEMPERATURE'] = config.getfloat(LOCATION, 'TEMPERATURE')
DATA['MAX_TOKENS'] = config.getint(LOCATION, 'MAX_TOKENS')
DATA['LEVEL'] = config.get(LOCATION, 'PERMISSION_LEVEL').lower()
DATA['SCRIPT_LANG'] = config.get(LOCATION, 'SCRIPT_LANG').lower()
DATA['RESPONSES'] = config.getint(LOCATION, 'NUMBER_OF_RESPONSES')

print(DATA)

