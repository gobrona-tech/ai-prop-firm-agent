import cv2


class OCRReader:

    def __init__(self):
        pass

    def extract_header_region(self, frame):

        height, width = frame.shape[:2]

        top = 0
        bottom = int(height * 0.08)

        left = 0
        right = int(width * 0.45)

        header = frame[top:bottom, left:right]

        return header

    def extract_price_region(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.72)
        right = int(width * 0.80)

        top = int(height * 0.08)
        bottom = int(height * 0.92)

        price_area = frame[top:bottom, left:right]

        return price_area

    def preprocess_image(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        processed = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        return processed

    def save_debug_regions(self, frame):

        header = self.extract_header_region(frame)

        price_area = self.extract_price_region(frame)

        header_processed = self.preprocess_image(
            header
        )

        price_processed = self.preprocess
