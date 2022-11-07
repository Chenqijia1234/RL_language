# from Interpreter_RL import interpre
#
# it = interpre.Interpreter()
# it.run_loop()
import time
# import ctypes

import win32api
import win32con
import win32gui
win32api.ShellExecute(0,"open","notepad.exe","","",1)
time.sleep(5)
notepad = win32gui.FindWindow("Notepad",None)

if notepad != 0:
    win32gui.SendMessage(notepad,win32con.WM_SETTEXT,None,"Hello")
    edit = win32gui.FindWindowEx(notepad,None,"Edit",None)
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,"您好，PYTHON")