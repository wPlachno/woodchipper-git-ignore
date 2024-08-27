import sys
import constants as S
import wcutil

settings = None
debug = None
dbg = None

class gignore_command_line:
    def __init__(self):
        self.mode = None
        self.target = None

def init_infrastructure():
    settings = wcutil.WoodchipperSettingsFile()
    settings.load()
    debug = wcutil.Debug(active=(settings.get_debug()))
    dbg = debug.scribe
    settings.get_or_default(S.DISPLAY_COMMAND, S.TAG_ON)

def decipher_command_line(args):
    dbg("CL ARGS: "+args)
    cl = gignore_command_line()
    if len(args) > 1:
        if args[1] == S.MODE_HELP:
            cl.mode = S.MODE_HELP
        elif args[1] == S.MODE_CLEAR:
            cl.mode = S.MODE_CLEAR
        elif args[1] == S.MODE_ADD:
            cl.mode = S.MODE_ADD
            cl.target = args[2:]
        elif args[1] == S.MODE_REMOVE:
            cl.mode = S.MODE_REMOVE
            cl.target = args[2:]
        elif args[1] == S.MODE_CONFIG:
            cl.mode = S.MODE_CONFIG
            cl.target = args[2:]
    else:
        cl.mode = S.MODE_LIST
    return cl

def _main(args):
    print(S.CL_DESC_UNIMPLEMENTED)
    init_infrastructure()

    decipher_command_line(args)
    # check verbose and print

if __name__ == "__main__":
    _main(sys.argv)
