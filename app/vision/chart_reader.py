import cv2
import numpy as np


class ChartReader:

    def crop_chart(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.08)
        right = int(width * 0.78)

        top = int(height * 0.15)
        bottom = int(height * 0.94)

        chart = frame[top:bottom, left:right]

        return chart

    def get_chart_info(self, chart):

        height, width = chart.shape[:2]

        return {
            "width": width,
            "height": height,
            "center_x": width // 2,
            "center_y": height // 2
        }

    def create_chart_mask(self, chart):

        gray = cv2.cvtColor(
            chart,
            cv2.COLOR_BGR2GRAY
        )

        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        _, mask = cv2.threshold(
            blurred,
            120,
            255,
            cv2.THRESH_BINARY
        )

        return mask

    def save_debug_images(self, chart):

        mask = self.create_chart_mask(
            chart
        )

        cv2.imwrite(
            "data/screenshots/chart_mask.png",
            mask
        )

        return {
            "mask": mask
        }
