import cv2


class ChartReader:

    def crop_chart(self, frame):

        height, width = frame.shape[:2]

        # მარცხენა toolbar-ის მოჭრა
        left = int(width * 0.07)

        # watchlist-ის მოჭრა
        right = int(width * 0.88)

        # ზედა toolbar-ის მოჭრა
        top = int(height * 0.12)

        # ქვედა ზოლის დატოვება დროისთვის
        bottom = int(height * 0.92)

        chart = frame[top:bottom, left:right]

        return chart
