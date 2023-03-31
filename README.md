# GPTerminal
An intelligent terminal that let you to use your operating system like talking to your best friend.

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

- Version: 2.0.0.

Release date: 30/03/2023.
