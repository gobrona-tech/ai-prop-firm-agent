import cv2
import numpy as np


class TimeframeDetector:

    def __init__(self):

        self.timeframes = [
            "15s",
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

        gray = cv2.cvtColor(
            region,
            cv2.COLOR_BGR2GRAY
        )

        h, w = gray.shape

        slots = [
            "15s",
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

        debug = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

        for i, tf in enumerate(slots):

            start_x = i * segment_width
            end_x = start_x + segment_width

            segment = gray[
                :,
                start_x:end_x
            ]

            # უფრო მუქი ფონების შეფასება
            dark_pixels = cv2.countNonZero(
                cv2.inRange(
                    segment,
                    40,
                    120
                )
            )

            scores[tf] = int(
                dark_pixels
            )

            cv2.rectangle(
                debug,
                (start_x, 0),
                (end_x, h),
                (0, 255, 0),
                2
            )

        cv2.imwrite(
            "data/screenshots/timeframe_segments.png",
            debug
        )

        active = max(
            scores,
            key=scores.get
        )

        return {
            "active": active,
            "scores": scores
        }
