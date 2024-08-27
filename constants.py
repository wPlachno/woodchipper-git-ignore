EMPTY=""
NL="\n"
BS="\\"
QU="\""

COLOR_RED='\033[0;31m'
COLOR_GREY='\033[90m'
COLOR_YELLOW='\033[93m'
COLOR_BLUE='\033[94m'
COLOR_DARK_YELLOW='\033[0;33m'
COLOR_GREEN='\033[0;32m'
COLOR_PURPLE='\033[0;35m'
COLOR_BLACK='\033[0;30m'
COLOR_WHITE='\033[37m'
COLOR_DEFAULT='\033[0m'

COLOR_SUPER=COLOR_PURPLE
COLOR_SUB=COLOR_GREY
COLOR_SIBLING=COLOR_DARK_YELLOW
COLOR_QUOTE=COLOR_GREEN
COLOR_ACTIVE=COLOR_GREEN
COLOR_CANCEL=COLOR_RED

MODE_SETUP = "MODE_SETUP"
MODE_ADD = "MODE_ADD"
MODE_REMOVE = "MODE_REMOVE"
MODE_CLEAR = "APPEND_CORE"
MODE_LIST = "MODE_LIST"
MODE_CONFIG = "CONFIG"
MODE_HELP = "MODE_HELP"

CL_DESC_TASK = COLOR_SUPER+"Task"+COLOR_DEFAULT+": "
CL_DESC_UNIMPLEMENTED = " ["+COLOR_CANCEL+"UNIMPLEMENTED"+COLOR_DEFAULT+"]"
CL_DESC_ACTIVE = COLOR_ACTIVE+"Active"+COLOR_DEFAULT
CL_DESC_INACTIVE = COLOR_CANCEL+"Inactive"+COLOR_DEFAULT
CL_DESC_ATTRIBUTE = COLOR_SIBLING+"{0}"+COLOR_DEFAULT+": {1}"+NL
CL_DESC_TARGET = COLOR_SIBLING+"Target"+COLOR_DEFAULT+": {1}"+NL
CL_DESC_TYPE = COLOR_SIBLING+"Type"+COLOR_DEFAULT+": {1}"+NL
CL_DESC_SUCCESS = COLOR_ACTIVE+"Success"+COLOR_DEFAULT
CL_DESC_FAILURE = COLOR_CANCEL+"Failure"+COLOR_DEFAULT

CL_DESC_MODE_SETUP = CL_DESC_TASK+"List all notes."+NL
CL_DESC_MODE_ADD = CL_DESC_TASK+"List Core notes."+NL
CL_DESC_MODE_REMOVE = CL_DESC_TASK+"List Local notes."+NL
CL_DESC_MODE_CLEAR = CL_DESC_TASK+"Append new note to Core."+NL
CL_DESC_MODE_LIST = CL_DESC_TASK+"Append new note to Local."+NL
CL_DESC_MODE_CONFIG = CL_DESC_TASK+COLOR_SUB+"Config"+COLOR_DEFAULT+" - "+COLOR_SIBLING+"{0}"+COLOR_DEFAULT+": {1}"+NL

FLAG_SETUP = "-s"
FLAG_CLEAR = "-c"
FLAG_ADD = "-a"
FLAG_PYTHON = "Python"
FLAG_REMOVE = "-r"
FLAG_DEBUG = "-debug"
FLAG_VERBOSE = "-verbose"
FLAG_CONFIG = "-config"
FLAG_HELP = "-help"

CL_DESC_HELP = (COLOR_SIBLING+"Welcome to "+COLOR_SUPER+"gignore.py"+COLOR_SIBLING+"!"+NL+
                COLOR_DEFAULT+"This script is designed to allow command-line edits of "+
                COLOR_SIBLING+".gitignore"+COLOR_DEFAULT+" files."+NL+
                COLOR_SUB+"It is highly suggested to set up an alias to launch this script "+
                "as gignore or gig."+NL+
                "Usage: "+NL+
                COLOR_QUOTE+"gignore"+COLOR_DEFAULT+": Lists all nodes in your .gitignore file."+NL+
                COLOR_QUOTE+"gignore -a \"[NODE]\""+COLOR_DEFAULT+": Adds the given node to your .gitignore file."+NL+
                COLOR_QUOTE+"gignore -r \"[NODE]\""+COLOR_DEFAULT+": Removes the given node from your .gitignore file."+NL+
                COLOR_QUOTE+"gignore -s \"[LANG]\""+COLOR_DEFAULT+": Sets up your .gitignore file and populates it with the standard nodes of the given language. If the language cannot be deciphered or is a language currently not supported, the .gitignore file will be created and populated only with the \".wcn*\" node."+NL+
                COLOR_QUOTE+"gignore -c"+COLOR_DEFAULT+": Removes all nodes from your .gitignore file."+NL+
                "If you have any suggestions, feel free to send an email to the developer, Will, at "+COLOR_SUPER+"wjplachno@gmail.com"+COLOR_DEFAULT+NL)



FILE_NAME_GIT_IGNORE = ".gitignore"

RESULT_SUCCESS = True
RESULT_FAILURE = False

DISPLAY_COMMAND = "display_command"
TAG_ON = "on"
TAG_OFF = "off"

OOB = -1