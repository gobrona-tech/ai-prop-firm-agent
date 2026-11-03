import cv2

from app.vision.tradingview import TradingViewWindow
from app.vision.screen_capture import ScreenCapture


class VisionDetector:

    def __init__(self):

        self.window = TradingViewWindow()
        self.capture = ScreenCapture()

    def scan(self):

        tv = self.window.find()

        if not tv:

            return {
                "success": False,
                "message": "TradingView window not found"
            }

        frame = self.capture.grab_region(
            {
                "left": tv["left"],
                "top": tv["top"],
                "width": tv["width"],
                "height": tv["height"]
            }
        )

        cv2.imwrite(
            "data/screenshots/latest.png",
            frame
        )

        return {
            "success": True,
            "window": tv,
            "frame": frame
        }
