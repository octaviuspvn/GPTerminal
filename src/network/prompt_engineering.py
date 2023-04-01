prompt = """ 
THE NEW RULES YOU NEED TO ACCOMPLISH IT CORRECTLY ARE THE NEXT:

/
IF THE NEXT SCRIPT CODE HAS SENSE REALIZE IT, AND IN THE FINAL OF YOUR RESPONSE SAY "[200] - SCRIPT CODE VALID"

IF THE NEXT SCRIPT CODE ISN'T VALID AND DOESN'T HAVE SENSE, DON'T REALIZE IT AND IN THE FINAL OF YOUR
RESPONSE SAY "[400] - SCRIPT CODE INVALID"

IF THE NEXT SCRIPT CODE IS EMPTY, DON'T REALIZE IT AND IN THE FINAL OF YOUR
RESPONSE SAY "[400] - SCRIPT CODE INVALID" 

IN THE FIRST LINE OF THE SCRIPT CODE INSERT "#BASH" OR "#SHELL" IF IT IS A SHELL CODE, TO LET ME KNOW THIS IS START OF THE SCRIPT CODE,
ALSO IN THE LAST LINE OF THE BASH CODE INSERT "#BASH" OR "#SHELL" IF IT IS A SHELL CODE, AGAIN TO LET ME KNOW THIS IS THE FINISH
OF THE SCRIPT CODE.

VERIFY THAT THE CODE USES "[ADMIN]" AND THE START OF THE SCRIPT CODE TO DO DANGEROUS SCRIPT CODES, IF IT IS A DANGEROUS SCRIPT CODE AND DOESN'T HAVE THE "[ADMIN]" KEYWORD IN THE BEGIN, SAYS THAT "I CAN'T HAVE THE PERMISSIONS TO DO THAT SCRIPT CODE"

DON'T GIVE ME INDICATIONS WHAT IS DOING THE SCRIPT CODE.

ONCE YOU GOT THE SCRIPT CODE, SHOW ONLY THE CODE.
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

[STATUS CODE] - VALIDATION OF SCRIPT CODE. 
%

THE NEXT IS THE REQUEST SCRIPT INPUT:

"""