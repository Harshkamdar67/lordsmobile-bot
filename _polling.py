import time
import win32api

def _get_coordinates():
    return win32api.GetCursorPos()

def poll_coordinates(seconds):
    print(_get_coordinates())

    time.sleep(seconds)
    poll_coordinates(seconds)

if __name__ == '__main__':
    poll_coordinates(.5)
