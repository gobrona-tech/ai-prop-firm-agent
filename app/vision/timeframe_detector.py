import cv2
import numpy as np


class TimeframeDetector:

    def __init__(self):

        self.timeframes = [
            "1m",
            "3m",
            "5m",
            "15m",
            "30m",
            "1h",
            "4h"
        ]

    def extract_timeframe_bar(
        self,
        frame
    ):

        height, width = frame.shape[:2]

        top = 0
        bottom = int(height * 0.12)

        left = int(width * 0.10)
        right = int(width * 0.45)

        return frame[
            top:bottom,
            left:right
        ]

    def detect_active_timeframe(
        self,
        frame
    ):

        region = self.extract_timeframe_bar(
            frame
        )

        hsv = cv2.cvtColor(
            region,
            cv2.COLOR_BGR2HSV
        )

        blue_mask = cv2.inRange(
            hsv,
            np.array([90, 40, 40]),
            np.array([140, 255, 255])
        )

        blue_pixels = cv2.countNonZero(
            blue_mask
        )

        return {
            "blue_pixels":
                blue_pixels
        }
