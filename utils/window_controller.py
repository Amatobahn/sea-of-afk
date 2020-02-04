from utils.utilities import is_linux, is_macos, is_windows


class WindowControllerException(BaseException):
    pass


class WindowController:

    def __init__(self):
        self.os_module = self.load_os_module()()

    def locate_window(self, name):
        return self.os_module.locate_window(name)

    def move_window(self, window_id, x, y):
        self.os_module.move_window(window_id, x, y)

    def resize_window(self, window_id, width, height):
        self.os_module.resize_window(window_id, width, height)

    def focus_window(self, window_id):
        self.os_module.focus_window(window_id)

    def bring_to_top(self, window_id):
        self.os_module.bring_to_top(window_id)

    def is_window_focused(self, window_id):
        return self.os_module.is_window_focused(window_id)

    def get_focused_window_name(self):
        return self.os_module.get_focused_window_name()

    def get_focused_window_id(self):
        return self.os_module.get_focused_window_id()

    def get_window_geometry(self, window_id):
        return self.os_module.get_window_geometry(window_id)

    @staticmethod
    def load_os_module():
        if is_linux():
            from utils.window_controllers.linux_window_controller import LinuxWindowController
            return LinuxWindowController
        elif is_macos():
            pass  # to be implemented
        elif is_windows():
            from utils.window_controllers.win32_window_controller import Win32WindowController
            return Win32WindowController
