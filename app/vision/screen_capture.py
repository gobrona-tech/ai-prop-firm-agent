from mss import mss
import numpy as np


class ScreenCapture:

    def __init__(self):
        self.sct = mss()

    def grab_region(self, region):

        screenshot = self.sct.grab(region)

        frame = np.array(screenshot)

        return frame
