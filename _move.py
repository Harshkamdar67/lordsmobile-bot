import win32api, win32con
import pyautogui

from _utils import *
from _configurations import *

def _mouse_set(coordinates):
    win32api.SetCursorPos(coordinates)

def _mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)

def _open_coordinates():
    _mouse_set(MAGNIFIER_ICON)
    _mouse_click()

def _mouse_drag(start, end):
    x1, y1 = start
    x2, y2 = end
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, .5)



def drag_down():
    return

def drag(option, base=False):
    x = (WIDTH + 200 / 2) - 30
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

    _mouse_drag((MID_X, MID_Y), (MID_X - x, MID_Y))

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def click_mouse_at(coordinates):
    _mouse_set(coordinates)

    time.sleep(1)

    _mouse_click()

def move_mouse_at(coordinates):
    _mouse_set(coordinates)

