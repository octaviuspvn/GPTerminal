[MIGRATING TO NEW PRODUCT CALLED COOPER] : https://github.com/octaviusp/COOPER/tree/main

![GPT TERMINAL IMAGE](https://github.com/octaviuspvn/GPTerminal/blob/main/GPTerminal%20banner.png)

[MIGRATING TO NEW PRODUCT CALLED COOPER] : https://github.com/octaviusp/COOPER/tree/main

An intelligent terminal that let you to use your operating system like talking to your best friend.

# HOW TO USE IT (ALPHA VERSION)
- 1) Clone repository locally
- 2) Find out main.py file inside repository, copy the path to execute from wherever you want.
- 3) Execute that main.py file found in the previous step: python {PATH}/src/main.py ACTION_TO_EXECUTE

- Example if the repository is in Downloads:
`python3 home/username/downloads/GPTerminal/src/main.py sort all files in this folder via filesize, from lower to higher`


## Examples:

- CLI Prompt:
`
~/: rename all files that ends with .js to .ts, also create a folder called "new typescript files" and move all recent rename files into it.
`
- Background input:


`INPUT:
[BASH ]
[LINUX]
[ADMIN]
[rename all files that ends with .js to .ts, also create a folder called "new typescript files" and move all recent rename files into it.]
`


- Bash code output:

`
find . -name ".js" -exec bash -c 'mv "$0" "${0%.js}.ts"' {} ;
mkdir "new typescript files"
find . -name ".ts" -newermt "-1 hour" -exec mv {} "new typescript files/" ;
`

It uses Chat-GPT in the background.

The prompt was perfectly refined to enhance operating system cli power.

- Version: 4.7.0.

Release date: 01/04/2023.
