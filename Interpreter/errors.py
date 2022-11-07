from . import runtime,interpreter,types
class BaseError(Exception):
    def __init__(self, *args: object,point:runtime.fp) -> None:
        super().__init__(*args)
    def ShowErrInfo()->dict:
        return {}


