import cv2


class OCRReader:

    def __init__(self):
        pass

    def extract_header_region(self, frame):

        height, width = frame.shape[:2]

        top = 0
        bottom = int(height * 0.10)

        left = 0
        right = width

        header = frame[top:bottom, left:right]

        return header

    def extract_price_region(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.88)
        right = width

        top = int(height * 0.10)
        bottom = int(height * 0.90)

        price_area = frame[top:bottom, left:right]

        return price_area

    def save_debug_regions(self, frame):

        header = self.extract_header_region(frame)

        price_area = self.extract_price_region(frame)

        cv2.imwrite(
            "data/screenshots/header_region.png",
            header
        )

        cv2.imwrite(
            "data/screenshots/price_region.png",
            price_area
        )

        return {
            "header": header,
            "price_area": price_area
        }
