import cv2
import numpy as np


class TimeframeDetector:

    def __init__(self):

        self.timeframes = {
            "15s": (40, 90),
            "1m": (90, 160),
            "3m": (160, 240),
            "5m": (240, 330),
            "15m": (330, 450),
            "30m": (450, 580),
            "1h": (580, 690),
            "4h": (690, 800)
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

    def get_nearest_timeframe(
        self,
        center_x
    ):

        nearest = None
        min_distance = 999999

        for tf, (start_x, end_x) in (
            self.timeframes.items()
        ):

            middle = (
                start_x +
                end_x
            ) // 2

            distance = abs(
                center_x -
                middle
            )

            if distance < min_distance:

                min_distance = distance
                nearest = tf

        return nearest

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

        # selected timeframe capsule
        mask = cv2.inRange(
            hsv,
            np.array([0, 0, 40]),
            np.array([180, 80, 140])
        )

        cv2.imwrite(
            "data/screenshots/timeframe_capsule_mask.png",
            mask
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        debug = region.copy()

        best_contour = None
        best_area = 0

        for contour in contours:

            x, y, w, h = cv2.boundingRect(
                contour
            )

            area = w * h

            if area < 1500:
                continue

            if area > best_area:

                best_area = area
                best_contour = (
                    x,
                    y,
                    w,
                    h
                )

        if not best_contour:

            cv2.imwrite(
                "data/screenshots/timeframe_detected.png",
                debug
            )

            return {
                "active": "UNKNOWN"
            }

        x, y, w, h = best_contour

        center_x = x + (
            w // 2
        )

        active = (
            self.get_nearest_timeframe(
                center_x
            )
        )

        cv2.rectangle(
            debug,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        cv2.circle(
            debug,
            (
                center_x,
                y + h // 2
            ),
            6,
            (0, 0, 255),
            -1
        )

        cv2.putText(
            debug,
            active,
            (
                x,
                max(20, y - 5)
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imwrite(
            "data/screenshots/timeframe_detected.png",
            debug
        )

        return {
            "active": active,
            "center_x": center_x,
            "contour_area": best_area
        }
