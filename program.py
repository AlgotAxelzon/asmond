from os import error
from instructions import parse_instruction

class Program(object):
    def __init__(self):
        self.instructions = []
    
    def from_file(filepath):
        p = Program()
        try:
            with open(filepath, "r") as f:
                lines = [line.split(";")[0].strip() for line in f.readlines()]
        except Exception as e:
            raise UserWarning("invalid program file")
        p.instructions = [parse_instruction(line.lower()) for line in lines if line != ""]
        return p

    def printarrow(self, pc):
        for i in range(0, len(self.instructions)):
            if i == pc:
                print("-->", self.instructions[i].asstring())
            else:
                print("   ", self.instructions[i].asstring())

    def run(self, system):
        while True:
            if system.pc == len(self.instructions):
                print("Program ended (end of instructions)")
                break
            self.instructions[system.pc].exec(system)
        print("Program done")

    def debug(self, system):
        while True:
            if system.pc == len(self.instructions):
                print("Program ended (end of instructions)")
                break

            self.printarrow(system.pc)

            print(system.asdict())
            user_input = input()
            if user_input == "e":
                exit()
            self.instructions[system.pc].exec(system)
        print("Program done")