import cv2
import numpy as np


class TimeframeDetector:

    def __init__(self):

        self.timeframes = {
            "15s": (0, 80),
            "1m": (80, 150),
            "3m": (150, 230),
            "5m": (230, 320),
            "15m": (320, 440),
            "30m": (440, 570),
            "1h": (570, 680),
            "4h": (680, 780)
        }

    def extract_timeframe_bar(
        self,
        frame
    ):

        height, width = frame.shape[:2]

        top = int(height * 0.05)
        bottom = int(height * 0.16)

        left = int(width * 0.15)
        right = int(width * 0.38)

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

        debug = region.copy()

        scores = {}

        for tf, (start_x, end_x) in (
            self.timeframes.items()
        ):

            end_x = min(
                end_x,
                w
            )

            start_x = min(
                start_x,
                w - 1
            )

            if end_x <= start_x:
                continue

            segment = gray[
                :,
                start_x:end_x
            ]

            dark_mask = cv2.inRange(
                segment,
                50,
                120
            )

            dark_pixels = cv2.countNonZero(
                dark_mask
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

            cv2.putText(
                debug,
                tf,
                (
                    start_x + 5,
                    20
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 255),
                1
            )

        cv2.imwrite(
            "data/screenshots/timeframe_segments.png",
            debug
        )

        if not scores:

            return {
                "active": "UNKNOWN",
                "scores": {}
            }

        active = max(
            scores,
            key=scores.get
        )

        return {
            "active": active,
            "scores": scores
        }
