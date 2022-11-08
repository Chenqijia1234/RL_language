


if __name__ != "__main__":
    from . import runtime, interpreter,Rtypes
else:
    import runtime
    import interpreter
    import Rtypes


class BaseError(Exception):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args)
        self.point = point

    def ShowErrInfo(self) -> tuple:
        traceback = self.point.GetValue()
        return traceback.GetValue()


class TypeError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)


class NameError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)


class InterpreterInnerError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)


class SyntaxError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)


class UnsafeError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)


class UnKnownError(BaseError):
    def __init__(self, *args: object, point: runtime.Fp) -> None:
        super().__init__(*args, point=point)
