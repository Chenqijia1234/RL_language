class TraceBack(list):
    def __init__(self, FileLine: str, FilePos: int):
        super().__init__()
        self[0] = (FileLine, FilePos)

    def GetValue(self) -> tuple:
        return self[0]


class Fp:
    def __init__(self, point: str, pos: int = 0) -> None:
        self.point = point
        self.pos = pos

    def GetValue(self) -> TraceBack:
        return TraceBack(self.point, self.pos)
