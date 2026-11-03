import cv2
import easyocr


class OCRReader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

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

    def read_text(self, image):

        results = self.reader.readtext(
            image,
            detail=0
        )

        return results

    def save_debug_regions(self, frame):

        header = self.extract_header_region(frame)

        price_area = self.extract_price_region(frame)

        header_processed = self.preprocess_image(
            header
        )

        price_processed = self.preprocess_image(
            price_area
        )

        cv2.imwrite(
            "data/screenshots/header_region.png",
            header
        )

        cv2.imwrite(
            "data/screenshots/price_region.png",
            price_area
        )

        cv2.imwrite(
            "data/screenshots/header_processed.png",
            header_processed
        )

        cv2.imwrite(
            "data/screenshots/price_processed.png",
            price_processed
        )

        header_text = self.read_text(
            header_processed
        )

        price_text = self.read_text(
            price_processed
        )

        print()
        print("===== HEADER OCR =====")

        for item in header_text:
            print(item)

        print()
        print("===== PRICE OCR =====")

        for item in price_text:
            print(item)

        return {
            "header": header,
            "price_area": price_area,
            "header_processed": header_processed,
            "price_processed": price_processed,
            "header_text": header_text,
            "price_text": price_text
        }
