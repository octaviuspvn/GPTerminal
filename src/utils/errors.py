BRAND_SCHEMA = f"\n[GPTerminal] -"

DOCUMENTATION = {
    "API_KEY" : "The Open AI API KEY for GPTerminal usage.",
    "MODEL" : "The AI Model of Open AI models [default: text-davinci-003]",
    "TEMPERATURE" : "The level of randomness that your script code contain [default: 0.8]",
    "MAX_TOKENS" : "The quantity of max tokens use in this api call [default: 200]" ,
    "OS" : "The operating system that you want your code in.",
    "SCRIPT_LANG" : "The scripting language that you want your code in",
    "LEVEL" : "The level of permissions that the returned scripting code needs to have."
}

class ReadingPromptFileError(Exception):
    def __str__(self):
        return f"{BRAND_SCHEMA} Error reading /settings/prompt_validations.txt"

class ConfigError(Exception):
    def __init__(self, parameter_in_problem, valid_values, documentation):
        self.parameter_in_problem = parameter_in_problem
        self.valid_values = valid_values
        self.documentation = documentation
    
    def __str__(self):
        return f"""{BRAND_SCHEMA} Please set {self.parameter_in_problem} config valid. \n Valid values of {self.parameter_in_problem} = {self.valid_values} \n
        Documentation: {self.documentation}"""

class APIKeyError(Exception):
    def __str__(self):
        return f"{BRAND_SCHEMA} Set API_KEY in PATH as 'OPENAI_API_KEY = YOUR_API_KEY'."

class BadPromptError(Exception):
    def __str__(self):
        return f"{BRAND_SCHEMA} That isn't a valid scripting prompt."

class SettingsIniError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __str__(self):
        return f"{BRAND_SCHEMA} An error was ocurred in get [settings.ini]: \n {self.error} \n - Try again."

def ErrorConfig(parameter_in_problem: str, valid_values, doc:str):
    raise ConfigError(parameter_in_problem, valid_values, doc)

def ErrorAPIKEY():
    raise APIKeyError()

def ErrorBadPrompt():
    raise BadPromptError()

def ErrorSettingsIni(error: Exception):
    raise SettingsIniError(error)

def ErrorReadingPromptFile():
    raise ReadingPromptFileError()
