class System(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.pc = 0

    def asdict(self):
        return {"a": self.a,
                "b": self.b,
                "c": self.c,
                "pc": self.pc}