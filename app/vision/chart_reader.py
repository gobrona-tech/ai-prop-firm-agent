import cv2


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
