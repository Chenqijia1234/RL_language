import sys
import enum

class ConsoleMode(enum.Enum):
    LINE_AND_LINE = 0
    FROM_FILE = 1   



class Rtype:
    pass
class NoneType(Rtype):
    pass
class Rint(Rtype):
    pass
class Rfloat(Rtype):
    pass
class Rstring(Rtype):
    pass
class Rlist(Rtype):
    pass
class Rdict(Rtype):
    pass
class Rclass(Rtype):
    pass
class NameSpace(dict):
    pass
class SafeIOSandbox:
    pass

