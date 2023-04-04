import subprocess
import sys
import re

BRAND_SCHEMA = "[GPTerminal] -\n"

def main(user_os: str, bash_code: str, is_python: bool, execute_instantly: bool):
    try:
        OPTIONS = ["Y", "N"]
        execution = ""
        if not execute_instantly:
                execution = input(f"{BRAND_SCHEMA} - Do you want to execute the above code [Y/N]: ").upper()

        temporaly_file_name = ""

        if execution == "Y" or execute_instantly:
                if is_python:
                        with open("gpterminal_script.py", "w") as f:
                                f.write(bash_code)
                        
                        python_version = re.search(r"^\d+?", str(sys.version)).group(0)
                        prefix = ""
                        if int(python_version) >= 3:
                                prefix = "python3"
                        else:
                                prefix = "python"

                        temporaly_file_name = "gpterminal_script.py"
                        subprocess.run([prefix, temporaly_file_name])
                        
                else:
                        with open("gpterminal_script.sh", "w") as f:
                                f.write(bash_code)

                        temporaly_file_name = "gpterminal_script.sh"

                        if user_os == "WINDOWS":
                                subprocess.run(["cmd.exe", "/c",temporaly_file_name], check=True, shell=True)
                        else:
                                subprocess.run(["bash", temporaly_file_name])
                                
                remove_file(user_os, temporaly_file_name)
                print("\n")

        elif execution == "N":
                print(f"{BRAND_SCHEMA} Bash code wasn't executed.")
        
        else:
                print(f"{BRAND_SCHEMA} Exiting GPTerminal")
                return
    except Exception as error:
        print(error)

def remove_file(os: str, file: str):
        if os.lower() == "windows":
                subprocess.run(["del", file], shell=True)
        elif os.lower() == "linux":
                subprocess.run(["rm", file])


