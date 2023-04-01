import openai
import os 
import subprocess
import re

BRAND_SCHEMA = "[GPTerminal] -"

prompt = """
THE NEW RULES YOU NEED TO ACCOMPLISH IT CORRECTLY ARE THE NEXT:

/
IF THE NEXT SCRIPT CODE HAS SENSE REALIZE IT, AND IN THE FINAL OF YOUR RESPONSE SAY "#VALID%"

IF THE NEXT SCRIPT CODE ISN'T VALID AND DOESN'T HAVE SENSE, DON'T REALIZE IT AND IN THE FINAL OF YOUR
RESPONSE SAY "#INVALID%"

IF THE NEXT SCRIPT CODE IS EMPTY, DON'T REALIZE IT AND IN THE FINAL OF YOUR
RESPONSE SAY "%INVALID%" 

IN THE FIRST LINE OF THE SCRIPT CODE INSERT "#BASH" OR "#SHELL" IF IT IS A SHELL CODE, TO LET ME KNOW THIS IS START OF THE SCRIPT CODE,
ALSO IN THE LAST LINE OF THE BASH CODE INSERT "#BASH" OR "#SHELL" IF IT IS A SHELL CODE, AGAIN TO LET ME KNOW THIS IS THE FINISH
OF THE SCRIPT CODE.

VERIFY THAT THE CODE USES "[ADMIN]" AND THE START OF THE SCRIPT CODE TO DO DANGEROUS SCRIPT CODES, IF IT IS A DANGEROUS SCRIPT CODE AND DOESN'T HAVE THE "[ADMIN]" KEYWORD IN THE BEGIN, SAYS THAT "I CAN'T HAVE THE PERMISSIONS TO DO THAT SCRIPT CODE"

DON'T GIVE ME INDICATIONS WHAT IS DOING THE SCRIPT CODE.

ONCE YOU GOT THE SCRIPT CODE, SHOW ONLY THE CODE AND THE VALIDATION OF %VALID% OR %INVALID%.
/

THE INPUT WILL HAVE THE FOLLOW STRUCTURE INSIDE %:

(THE INPUT COULD BE IN WHATEVER LANGUAGE)

%
[SCRIPT LANGUAGE] - IT WILL BE "BASH" OR "SHELL".
[PLATFORM] - IT WILL BE "LINUX", "MAC", OR "WINDOWS"
[LEVEL] - IT WILL BE "ADMIN" OR "USER", IF NOT LEVEL IS PROVIDED, ASSUME USER LEVEL.
[ACTION] - THIS IS THE ACTION THAT THE USER WANT TO DO IN ITS SCRIPT CODE, THIS ACTION COULD BE IN ANY OTHER LANGUAGE, IF ISN'T IN ENGLISH, TRANSLATE IT AND INTERPRET TO GENERATE THE CODE.
%

THE VALIDATION OF THE INPUT ARE THE NEXT INSIDE %:

%
IF THE SCRIPT LANGUAGE ISN'T PROVIDED ASSUME BASH.
IF THE PLATFORM ISN'T PROVIDED ASSUME LINUX.
IF LEVEL ISN'T PROVIDED ASSUME USER LEVEL.
IF [ACTION] ISN'T PROVIDED RETURN A BAD REQUEST FROM THE USER.
IF IN [ACTION] THE FOLDER ISN'T PROVIDED, ASSUME THE USER CURRENT FOLDER.
IF IN [ACTION] THE SCRIPT CODE IS MALICIOUS OR DANGER VERIFY THAT THE LEVEL IS ADMIN, IF NOT, RETURN BAD PERMISSIONS TO THAT ACTION.
%

THE NEXT IS AN EXAMPLE PROVIDED FOR YOU TO GUIDE YOUR ANSWER, THE EXAMPLE IS INSIDE %:

%
[BASH]
[LINUX]
[ADMIN]
[install node.js then install chromium with sudo, then remove all files ends with .py in this current folder, and rename all files ends with .js into .ts, therefeore move that .ts renamed files into a new folder (if is not created) called "typescript files"]

YOUR OUTPUT WILL BE IN THE NEXT STYLE:

#BASH
[SCRIPT CODE WITH NO COMMENTARY OF EACH ACTION...]
#BASH

%

THE NEXT IS THE REQUEST SCRIPT INPUT:

"""

def promptDataToGPT(action_prompt: str, context)-> str:

        openai.api_key = context['API_KEY']
        user_os = context['OS']
        lvl = context['LEVEL']
        script = context['SCRIPT_LANG']
        model = context['MODEL']
        max_tokens = context['MAX_TOKENS']
        temperature = context['TEMPERATURE']
        
        try:    
                response = openai.Completion.create(
                                model=model,
                                max_tokens=max_tokens,
                                temperature=temperature,
                                prompt=f"""
                                {prompt}
                                [{script}]
                                [{user_os}]
                                [{lvl}]
                                [{action_prompt}]
                                """,
                                n=1
                )
                
                bash_code = response.choices[0]['text']

                if script == "bash":
                        bash_code = bash_code.replace("#BASH", "")
                else:
                        bash_code = bash_code.replace("#SHELL", "")

                if re.search(r'#INVALID%', bash_code):
                        print(f"{BRAND_SCHEMA} - The script code action is invalid.")
                        return

                print(f"{BRAND_SCHEMA} - The following bash code will execute: \n", bash_code)

                OPTIONS = ["Y", "N"]
                execution = input(f"{BRAND_SCHEMA} - Do you want to execute the above code [Y/N]: ").upper()

                if execution == "Y":
                        if user_os in ["linux", "mac"]:
                                with open("gpterminal_script.sh", "w") as f:
                                        f.write(bash_code)
                                subprocess.run(["bash", "gpterminal_script.sh"])
                                subprocess.run(["rm", "gpterminal_script.sh"])

                elif execution == "N":
                        print(f"{BRAND_SCHEMA} - Bash code wasn't executed.")
                
                else:
                        print(f"{BRAND_SCHEMA} -  Exiting GPTerminal")
                        return

        except Exception as error:
                print(error)
