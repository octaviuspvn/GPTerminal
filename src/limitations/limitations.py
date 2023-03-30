def main():
    try:
        with open("./prompt_limitations.txt") as prompt_limit:
            indications = prompt_limit.readlines()
            print(" ".join(indications))
    except:
        print("An error was ocurred, please verify that the prompt_limitations.txt exists.")

if __name__ == "__main__":
    main() 