import cv2

from app.vision.tradingview import TradingViewWindow
from app.vision.screen_capture import ScreenCapture
from app.vision.chart_reader import ChartReader


class VisionDetector:

    def __init__(self):

        self.window = TradingViewWindow()
        self.capture = ScreenCapture()
        self.chart_reader = ChartReader()

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

        chart = self.chart_reader.crop_chart(frame)

        cv2.imwrite(
            "data/screenshots/latest.png",
            frame
        )

        cv2.imwrite(
            "data/screenshots/chart.png",
            chart
        )

        return {
            "success": True,
            "window": tv,
            "frame": frame,
            "chart": chart
        }
