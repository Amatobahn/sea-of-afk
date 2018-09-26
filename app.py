import sys
from gergcob.window_controller import WindowController
from gergcob.keyboard_controller import Keyboard

import keyboard as kb

from PySideSimplify import *

from threading import Thread
from time import sleep

import data


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.setFixedSize(width, height)
        self.setWindowTitle("Sea of AFK - [HERE]")
        self.setWindowIcon(QtGui.QIcon(":src/sot_icon.png"))
        self.is_afk = False
        self.listening = True

        self.window = WindowController()
        self.keyboard = Keyboard()

        self.setStyleSheet("QPushButton{background-image: url(:src/sot_active.png);}")

        # INTERFACE
        self.btn_afk = QtGui.QPushButton("")
        self.btn_afk.setFlat(True)
        self.btn_afk.clicked.connect(lambda: self.afk(self.is_afk))
        self.btn_afk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setCentralWidget(self.btn_afk)

        l = Thread(target=self.hotkey_listener)
        l.start()

        self.show()
        self.focusWidget().clearFocus()

    def hotkey_listener(self):
        print('listening')
        while self.listening:
            if kb.is_pressed('=') and kb.is_pressed('-'):
                self.afk(self.is_afk)
                sleep(0.5)

    def afk(self, afk: bool=False):
        try:
            if not afk:
                self.is_afk = True
                self.setWindowTitle("Sea of AFK - [AWAY]")
                self.setStyleSheet("QPushButton{background-image: url(:src/sot_away.png);}")
                print("afk")
                t = Thread(target=self.move_pirate)
                t.start()
            else:
                print("not afk")
                self.setWindowTitle("Sea of AFK - [HERE]")
                self.setStyleSheet("QPushButton{background-image: url(:src/sot_active.png);}")
                self.is_afk = False
        except:
            pass

    def move_pirate(self):
        try:
            # Find and focus window
            sot_id = self.window.locate_window("Sea of Thieves")
            self.window.focus_window(sot_id)

            while self.is_afk:
                for i in ['w', 'a', 's', 'd']:
                    self.keyboard.press_key(i)
                    sleep(0.05)
                    self.keyboard.release_key(i)
                    sleep(0.5)
        except:
            pass

    # [Override] Prompts user to close application with confirmation, sends analytics on accept.
    def closeEvent(self, event):
        self.listening = False
        event.accept()
        sys.exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app_window = ApplicationWindow(300, 100)
    sys.exit(app.exec_())
