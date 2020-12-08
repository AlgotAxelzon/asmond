def parse_instruction(string):
    ins = string.split(" ")
    if len(ins) == 1:
        if ins[0] == "nop":
            return Nop()
        if ins[0] == "inc":
            return Inc()
        if ins[0] == "dec":
            return Dec()
        if ins[0] == "swp":
            return Swp()
        if ins[0] == "add":
            return Add()

    # TODO: check types of data
    if len(ins) == 2:
        if ins[0] == "lda":
            return Lda(int(ins[1]))
        if ins[0] == "jmp":
            return Jmp(int(ins[1]))

    if len(ins) == 3:
        if ins[0] == "jeq":
            return Jeq(int(ins[1]), int(ins[2]))
        if ins[0] == "jne":
            return Jne(int(ins[1]), int(ins[2]))


class Instruction(object):
    def exec(self, system):
        return



#.......................................
#............. 1 BYTE(S) ...............
#.......................................

class Nop(Instruction):
    name = "nop"
    def __init__(self):
        return

    def exec(self, system):
        system.pc += 1
        return system

    def asstring(self):
        return self.name

class Inc(Instruction):
    name = "inc"
    def __init__(self):
        return

    def exec(self, system):
        system.a += 1
        system.pc += 1
        return system

    def asstring(self):
        return self.name

class Dec(Instruction):
    name = "dec"
    def __init__(self):
        return

    def exec(self, system):
        system.a -= 1
        system.pc += 1
        return system

    def asstring(self):
        return self.name

class Swp(Instruction):
    name = "swp"
    def __init__(self):
        return

    def exec(self, system):
        temp = system.a
        system.a = system.b
        system.b = temp
        system.pc += 1
        return system

    def asstring(self):
        return self.name

class Add(Instruction):
    name = "add"
    def __init__(self):
        return

    def exec(self, system):
        system.a = system.a + system.b
        system.pc += 1
        return system

    def asstring(self):
        return self.name



#.......................................
#............. 2 BYTE(S) ...............
#.......................................

class Lda(Instruction):
    name = "lda"
    def __init__(self, value):
        self.value = value
        return

    def exec(self, system):
        system.a = self.value
        system.pc += 1
        return system

    def asstring(self):
        return self.name+ " " +str(self.value)

class Jmp(Instruction):
    name = "jmp"
    def __init__(self, value):
        self.value = value
        return

    def exec(self, system):
        system.pc += self.value
        return system

    def asstring(self):
        return self.name+ " " +str(self.value)



#.......................................
#............. 3 BYTE(S) ...............
#.......................................

class Jeq(Instruction):
    name = "jeq"
    def __init__(self, value, jump):
        self.value = value
        self.jump = jump
        return

    def exec(self, system):
        if system.a != self.value:
            system.pc += 1
        else:
            system.pc += self.jump
        return system

    def asstring(self):
        return self.name+ " " +str(self.value)+ " " +str(self.jump)

class Jne(Instruction):
    name = "jne"
    def __init__(self, value, jump):
        self.value = value
        self.jump = jump
        return

    def exec(self, system):
        if system.a == self.value:
            system.pc += 1
        else:
            system.pc += self.jump
        return system

    def asstring(self):
        return self.name + " " + str(self.value) + " " + str(self.jump)
