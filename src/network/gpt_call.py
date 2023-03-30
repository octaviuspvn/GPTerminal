import openai
import os

openai.api_key = os.getenv['OPENAI_API_KEY']

def promptDataToGPT(prompt: str, language: str, os: str)-> str:

        scripting_language = ""

        if os == "Linux" or os == "Darwin": 
                scripting_language = "bash"
        else: 
                scripting_language = "shell"

        first_language_prompt = "Please answer me in " + language
        second_data_prompt = f"Create a script code in {scripting_language} for {os} that does: " + prompt
        
        try:
                response = openai.Completion.create(
                                model="text-davinci-003",
                                prompt=f"{first_language_prompt}, {second_data_prompt}"
                                max_tokens=2048,
                                temperature=0.8
                )
                print(f"{brand_schema} script finished.")
                return response.choices[0].text
        except:
                print(f"{brand_schema} An error was ocurred, please try again")
