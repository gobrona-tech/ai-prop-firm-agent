import cv2


class ChartReader:

    def crop_chart(self, frame):

        height, width = frame.shape[:2]

        # Left drawing toolbar
        left = int(width * 0.08)

        # Right watchlist / panels
        right = int(width * 0.78)

        # Top TradingView toolbar
        top = int(height * 0.15)

        # Bottom time scale
        bottom = int(height * 0.94)

        chart = frame[top:bottom, left:right]

        return chart
