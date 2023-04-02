import subprocess

BRAND_SCHEMA = "[GPTerminal] -\n"

def main(user_os: str, bash_code: str):
    try:
        OPTIONS = ["Y", "N"]
        execution = input(f"{BRAND_SCHEMA} - Do you want to execute the above code [Y/N]: ").upper()

        if execution == "Y":
                with open("gpterminal_script.sh", "w") as f:
                        f.write(bash_code)
                if user_os == "WINDOWS":
                        subprocess.run(["cmd.exe", "/c", "gpterminal_script.sh"], check=True, shell=True)
                        subprocess.run(["del", "gpterminal_script.sh"], shell=True)
                else:
                        subprocess.run(["bash", "gpterminal_script.sh"])
                        subprocess.run(["rm", "gpterminal_script.sh"])

        elif execution == "N":
                print(f"{BRAND_SCHEMA} Bash code wasn't executed.")
        
        else:
                print(f"{BRAND_SCHEMA} Exiting GPTerminal")
                return
    except Exception as error:
        print(error)