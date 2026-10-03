import win32api
import win32con

        # 'shutdown',
        # 'reboot',
        # 'screenshot',
        # 'minimize'
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
        None
    
    def _command_minimize(self, args):
        None
    