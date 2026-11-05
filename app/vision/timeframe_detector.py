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

        cv2.imwrite(
            "data/screenshots/timeframe_bar.png",
            region
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

        cv2.imwrite(
            "data/screenshots/timeframe_blue_mask.png",
            blue_mask
        )

        h, w = blue_mask.shape

        slots = [
            "1m",
            "3m",
            "5m",
            "15m",
            "30m",
            "1h",
            "4h"
        ]

        segment_width = w // len(slots)

        scores = {}

        for i, tf in enumerate(slots):

            start_x = i * segment_width
            end_x = start_x + segment_width

            segment = blue_mask[
                :,
                start_x:end_x
            ]

            scores[tf] = int(
                cv2.countNonZero(
                    segment
                )
            )

        active = max(
            scores,
            key=scores.get
        )

        return {
            "active": active,
            "scores": scores
        }
