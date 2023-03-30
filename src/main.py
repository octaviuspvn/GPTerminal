import sys
import argparse
import platform

from language import GetLanguageWithCode


def main():
    
    # Getting the prompt text to generate bash code 
    prompt = " ".join(sys.argv[1:])

    # Getting language argument from cmd
    parser = argparse.ArgumentParser(description='Language code and prompt to chat gpt.')
    parser.add_argument('-l', '--language', type=str, help='a language code (e.g. "es" for Spanish, "kr" for korean)')
    args = parser.parse_args()
    
    language_code = GetLanguageWithCode(args.language) 

if __name__ == "__main__":
    main()