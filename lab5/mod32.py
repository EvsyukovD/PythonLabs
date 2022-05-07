SIZE = 32
MOD = (1 << SIZE) - 1


class Mod32(int):
    def __add__(self, other):
        return Mod32((int(self) + int(other)) & MOD)

    def __sub__(self, other):
        return Mod32((int(self) - int(other)) & MOD)

    def __mul__(self, other):
        return Mod32((int(self) * int(other)) & MOD)

    def __invert__(self):
        return Mod32(MOD - int(self))

    def __lshift__(self, s):
        l, r = (int(self) << int(s)) & MOD, int(self) >> (SIZE - int(s))
        return Mod32(l | r)

    def __rshift__(self, s):
        l, r = (int(self) << (SIZE - int(s))) & MOD, int(self) >> int(s)
        return Mod32(l | r)
