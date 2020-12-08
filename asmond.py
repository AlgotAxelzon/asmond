import sys

from system import System
from program import Program

VALID_FLAGS = ["-f", "-d"]
DEFAULT_PROGRAM_FILE = "program.ond"
DEFAULT_MODE = "run"


program_file = DEFAULT_PROGRAM_FILE
mode = DEFAULT_MODE
args = sys.argv
args.pop(0)
n_args = len(args)
while n_args > 0:
    flag = args.pop(0)
    if flag in VALID_FLAGS:
        if flag == VALID_FLAGS[0]:
            program_file = args.pop(0)
        if flag == VALID_FLAGS[1]:
            mode = "debug"
    else:
        raise UserWarning("invalid flag/argument")
    n_args = len(args)

p = Program.from_file(program_file)
s = System()

if mode == "debug":
    p.debug(s)
else:
    p.run(s)
