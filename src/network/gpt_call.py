import openai
import limitations as l

BRAND_SCHEMA = "[GPTerminal] -\n"

def promptDataToGPT(action_prompt: str, api_key: str, context)-> str:

        scripting_language = ""
        os = context['os']
        
        prompt_engineering = l.getInstructions()

        prompt_first_part = prompt_engineering['indications']

        if prompt_engineering['status'] == 400 or not prompt_engineering['indications']:
                return "An error was ocurred."

        if os == "Linux" or os == "Darwin": 
                scripting_language = "bash"
        else: 
                scripting_language = "shell"
        

        level = "admin"
         
        try:
                response = openai.Completion.create(
                                model="text-davinci-003",
                                max_tokens=2048,
                                temperature=0.8,
                                prompt=f"""{prompt_first_part} \n 
                                [{scripting_language}]
                                [{os}]
                                [{level}]
                                [{action_prompt}]
                                """
                )
                print(f"{BRAND_SCHEMA} script finished.")
                return response
        except:
                print(f"{BRAND_SCHEMA} An error was ocurred, please try again")
