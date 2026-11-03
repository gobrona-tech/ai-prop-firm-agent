import cv2


class ChartReader:

    def crop_chart(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.05)
        right = int(width * 0.82)

        top = int(height * 0.08)
        bottom = int(height * 0.93)

        chart = frame[top:bottom, left:right]

        return chart
