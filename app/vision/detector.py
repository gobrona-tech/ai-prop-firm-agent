import cv2

from app.vision.tradingview import TradingViewWindow
from app.vision.screen_capture import ScreenCapture
from app.vision.chart_reader import ChartReader
from app.vision.ocr import OCRReader


class VisionDetector:

    def __init__(self):

        self.window = TradingViewWindow()
        self.capture = ScreenCapture()
        self.chart_reader = ChartReader()
        self.ocr = OCRReader()

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

        regions = self.ocr.save_debug_regions(frame)

        debug_frame = frame.copy()

        height, width = frame.shape[:2]

        # HEADER REGION
        cv2.rectangle(
            debug_frame,
            (0, 0),
            (int(width * 0.45), int(height * 0.08)),
            (0, 255, 0),
      
