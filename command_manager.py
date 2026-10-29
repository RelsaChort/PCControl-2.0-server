from pathlib import Path
from datetime import datetime

import win32api
import win32con
import win32gui

from PIL import ImageGrab

import ctypes

class CommandManager:
    def __init__(self, command: str, args: dict) -> str:
        method_name = f"_command_{command}"
        method = getattr(self, method_name, None)
        
        if method:
            return method(args)
        return f'команда "{command}" не найдена!'
    
    def _command_shutdown(self, args):
        win32api.ExitWindowsEx(
            win32con.EWX_SHUTDOWN,
            0
        )
    
    def _command_reboot(self, args):
        win32api.ExitWindowsEx(
            win32con.EWX_REBOOT,
            0
        )

    def _command_screenshot(self, args):
        timestamp = datetime.now().strftime("%d %m %Y - %H %M %S")
        path = self._screenshot_mkdir()
        path = path / f"{timestamp}.png"

        image = ImageGrab.grab()
        image.save(path)
    
    def _command_minimize(self, args):
        ctypes.windll.user32.PostMessageW(
            ctypes.windll.user32.GetDesktopWindow(), 0x0112, 0xF0E0, 0
        )
        
    def _screenshot_mkdir(self):
        main_dir = Path(__file__).resolve().parent
        screenshot_dir = main_dir / "Screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        return screenshot_dir