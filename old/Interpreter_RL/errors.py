class InitError(Exception):
    def __init__(self,mode,where,args):
        super(InitError, self).__init__(f"Errors:  InitError_{mode}  in {where}:  {args}")
class Interpreter_settings_error(Exception):
    def __init__(self,mode,where,args):
        super(Interpreter_settings_error, self).__init__(f"Errors:  Interpreter_settings_error_{mode} in {where}: {args}")
class Runtime_error(Exception):
    def __init__(self,mode,where,args):
        super(Runtime_error, self).__init__(f"Errors:  Runtime_error_{mode} in {where}:  {args}")