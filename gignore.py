import os
import sys
from pathlib import Path

import constants as S
import default_nodes as Nodes
import wcutil
from constants import CL_DESC_NODE_ADDED


class gignore_command_line:
    def __init__(self):
        self.mode = None
        self.target = None
        self.actor = None

        self.settings = wcutil.WoodchipperSettingsFile()
        self.settings.load()
        self.debug = wcutil.Debug(active=(self.settings.get_debug()))
        self.dbg = self.debug.scribe
        self.settings.get_or_default(S.DISPLAY_COMMAND, S.TAG_ON)
        self.gig_path = Path(os.getcwd()) / S.FILE_NAME_GIT_IGNORE

    def set_mode(self, args):
        self.dbg("CL ARGS: "+str(args))
        if len(args) > 1:
            if args[1] == S.FLAG_HELP:
                self.mode = S.MODE_HELP
                self.actor = self._run_help
            elif args[1] == S.FLAG_SETUP:
                self.mode = S.MODE_SETUP
                self.target = args[2:]
                self.actor = self._run_setup
            elif args[1] == S.FLAG_CLEAR:
                self.mode = S.MODE_CLEAR
                self.actor = self._run_clear
            elif args[1] == S.FLAG_ADD:
                self.mode = S.MODE_ADD
                self.target = args[2:]
                self.actor = self._run_add
            elif args[1] == S.FLAG_REMOVE:
                self.mode = S.MODE_REMOVE
                self.target = args[2:]
                self.actor = self._run_remove
            elif args[1] == S.FLAG_CONFIG:
                self.mode = S.MODE_CONFIG
                self.target = args[2:]
                self.actor = self._run_config
        else:
            self.mode = S.MODE_LIST
            self.actor = self._run_list

    def run(self):
        return self.actor()

    def _run_help(self):
        return S.CL_DESC_HELP

    def _run_setup(self):
        targets = Nodes.setup_defaults["Default"]
        for setup_type in self.target:
            if setup_type in Nodes.setup_defaults:
                targets = targets + Nodes.setup_defaults[setup_type]

        gig_file = wcutil.WoodChipperFile(self.gig_path)
        gig_file.read()
        text = S.EMPTY
        for node in targets:
            gig_file.append_line(node)
            text = text + CL_DESC_NODE_ADDED.format(node)
        gig_file.write()
        return text

    def _run_list(self):
        gig_file = wcutil.WoodChipperFile(self.gig_path, False)
        if not gig_file.exists():
            return S.CL_DESC_FILE_DOES_NOT_EXIST
        gig_file.read()
        if len(gig_file.text) == 0:
            return S.CL_DESC_FILE_IS_EMPTY

        list = S.CL_DESC_NODE_LIST
        for rawLine in gig_file.text:
            line = rawLine
            if line[-1] == '\n':
                line = line[:-1]
            list += S.CL_DESC_NODE_LIST.format(line)
        return list

    def _run_clear(self):
        gig_file = wcutil.WoodChipperFile(self.gig_path, False)
        if not gig_file.exists():
            return S.CL_DESC_FILE_DOES_NOT_EXIST
        gig_file.read()
        gig_file.text = list(())
        gig_file.write()
        return S.CL_DESC_FILE_HAS_BEEN_CLEARED

    def _run_add(self):
        gig_file = wcutil.WoodChipperFile(self.gig_path)
        gig_file.read()
        text = S.EMPTY
        for node in self.target:
            gig_file.append_line(node)
            text = text + S.CL_DESC_NODE_ADDED.format(node)
        gig_file.write()
        return text

    def _run_remove(self):
        gig_file = wcutil.WoodChipperFile(self.gig_path, False)
        if not gig_file.exists():
            return S.CL_DESC_FILE_DOES_NOT_EXIST
        gig_file.read()
        self.dbg("Nodes in file: "+S.NL)
        for node in gig_file.text:
            self.dbg("- "+node)
        text = S.EMPTY
        self.dbg("Targets: "+S.NL)
        for node in self.target:
            self.dbg("- "+node)
            gig_file.text.remove(node)
            text = text + S.CL_DESC_NODE_REMOVED.format(node)
        gig_file.write()
        return text

    def _run_config(self):
        return S.CL_DESC_UNIMPLEMENTED

def _main(args):
    cl = gignore_command_line()
    cl.set_mode(args)
    results = cl.run()
    print(results)

if __name__ == "__main__":
    _main(sys.argv)
