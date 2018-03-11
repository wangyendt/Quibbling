# coding: utf-8

import os

class ScreenShot:
    def __init__(self):
        pass

    def take_screen_shot(self):
        self.execute("adb shell 'system/bin/screencap' storage/self/primary/wy_workplace/screenshot.png")
        self.execute("adb pull storage/self/primary/wy_workplace/screenshot.png ./")

    @staticmethod
    def execute(cmd):
        return os.popen(cmd).read()


if __name__ == '__main__':
    ss = ScreenShot()
    ss.take_screen_shot()
