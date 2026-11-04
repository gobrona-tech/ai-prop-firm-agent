import cv2
import numpy as np


class ChartReader:

    def crop_chart(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.08)
        right = int(width * 0.78)

        top = int(height * 0.15)
        bottom = int(height * 0.94)

        return frame[top:bottom, left:right]

    def get_chart_info(self, chart):

        height, width = chart.shape[:2]

        return {
            "width": width,
            "height": height,
            "center_x": width // 2,
            "center_y": height // 2
        }

    def create_bullish_mask(self, chart):

        hsv = cv2.cvtColor(
            chart,
            cv2.COLOR_BGR2HSV
        )

        lower_green = np.array(
            [35, 40, 40]
        )

        upper_green = np.array(
            [90, 255, 255]
        )

        return cv2.inRange(
            hsv,
            lower_green,
            upper_green
        )

    def create_bearish_mask(self, chart):

        hsv = cv2.cvtColor(
            chart,
            cv2.COLOR_BGR2HSV
        )

        lower_red_1 = np.array(
            [0, 40, 40]
        )

        upper_red_1 = np.array(
            [15, 255, 255]
        )

        lower_red_2 = np.array(
            [165, 40, 40]
        )

        upper_red_2 = np.array(
            [180, 255, 255]
        )

        mask1 = cv2.inRange(
            hsv,
            lower_red_1,
            upper_red_1
        )

        mask2 = cv2.inRange(
            hsv,
            lower_red_2,
            upper_red_2
        )

        return cv2.bitwise_or(
            mask1,
            mask2
        )

    def save_debug_images(self, chart):

        bullish_mask = self.create_bullish_mask(
            chart
        )

        bearish_mask = self.create_bearish_mask(
            chart
        )

        cv2.imwrite(
            "data/screenshots/bullish_mask.png",
            bullish_mask
        )

        cv2.imwrite(
            "data/screenshots/bearish_mask.png",
            bearish_mask
        )

        return {
            "bullish_mask": bullish_mask,
            "bearish_mask": bearish_mask
        }
