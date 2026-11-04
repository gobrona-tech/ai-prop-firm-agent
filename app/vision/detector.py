import cv2

from app.vision.tradingview import TradingViewWindow
from app.vision.screen_capture import ScreenCapture
from app.vision.chart_reader import ChartReader
from app.vision.ocr import OCRReader
from app.vision.timeframe_detector import TimeframeDetector


class VisionDetector:

    def __init__(self):

        self.window = TradingViewWindow()
        self.capture = ScreenCapture()
        self.chart_reader = ChartReader()
        self.ocr = OCRReader()
        self.timeframe_detector = (
            TimeframeDetector()
        )

    def scan(self):

        tv = self.window.find()

        if not tv:

            return {
                "success": False,
                "message":
                    "TradingView window not found"
            }

        frame = self.capture.grab_region(
            {
                "left": tv["left"],
                "top": tv["top"],
                "width": tv["width"],
                "height": tv["height"]
            }
        )

        chart = self.chart_reader.crop_chart(
            frame
        )

        chart_info = (
            self.chart_reader.get_chart_info(
                chart
            )
        )

        chart_debug = (
            self.chart_reader.save_debug_images(
                chart
            )
        )

        regions = (
            self.ocr.save_debug_regions(
                frame
            )
        )

        timeframe_debug = (
            self.timeframe_detector
            .detect_active_timeframe(
                frame
            )
        )

        debug_frame = frame.copy()

        height, width = frame.shape[:2]

        cv2.rectangle(
            debug_frame,
            (0, 0),
            (
                int(width * 0.45),
                int(height * 0.08)
            ),
            (0, 255, 0),
            4
        )

        cv2.rectangle(
            debug_frame,
            (
                int(width * 0.72),
                int(height * 0.08)
            ),
            (
                int(width * 0.80),
                int(height * 0.92)
            ),
            (0, 0, 255),
            4
        )

        cv2.imwrite(
            "data/screenshots/latest.png",
            frame
        )

        cv2.imwrite(
            "data/screenshots/chart.png",
            chart
        )

        cv2.imwrite(
            "data/screenshots/debug_regions.png",
            debug_frame
        )

        return {
            "success": True,
            "window": tv,
            "frame": frame,
            "chart": chart,
            "chart_info": chart_info,
            "chart_debug": chart_debug,
            "regions": regions,
            "timeframe_debug":
                timeframe_debug
        }
