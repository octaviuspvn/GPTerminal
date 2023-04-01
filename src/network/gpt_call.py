import openai
import os 
import subprocess
import re
from src.utils import errors
from src.executor import execute_script as exe

BRAND_SCHEMA = "[GPTerminal] -"

def main():

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "settings", "prompt_limitations.txt"))

        try:
                with open(file_path, "r") as prompt_file:
                        prompt = prompt_file.readlines()
                        prompt_file.close()
                return " ".join(prompt)
        except:
                errors.ErrorReadingPromptFile()

def promptDataToGPT(action_prompt: str, context)-> str:

        guidance_prompt = main()

        openai.api_key = context['API_KEY']
        user_os = context['OS']
        lvl = context['LEVEL']
        script = context['SCRIPT_LANG']
        model = context['MODEL']
        max_tokens = context['MAX_TOKENS']
        temperature = context['TEMPERATURE']
        number_of_responses = context['RESPONSES']

        try:    
                response = openai.Completion.create(
                                model=model,
                                max_tokens=max_tokens,
                                temperature=temperature,
                                prompt=f"""
                                {guidance_prompt} \n
                                [{script}]
                                [{user_os}]
                                [{lvl}]
                                [{action_prompt}]
                                """,
                                n=number_of_responses
                )
                
                bash_code = response.choices[0]['text']

                if script == "bash":
                        bash_code = bash_code.replace("#BASH", "")
                else:
                        bash_code = bash_code.replace("#SHELL", "")

                if re.search(r'#INVALID%', bash_code):
                        errors.ErrorBadPrompt()
                
                exe.main(user_os, bash_code)


        except Exception as error:
                print(error)