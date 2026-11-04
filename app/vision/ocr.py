import cv2
import easyocr


class OCRReader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

        self.symbols = [
            "MNQ",
            "MES",
            "NQ",
            "ES"
        ]

        self.timeframes = [
            "15s",
            "1m",
            "3m",
            "5m",
            "15m",
            "30m",
            "1h",
            "4h",
            "D",
            "W",
            "M"
        ]

    def extract_header_region(self, frame):

        height, width = frame.shape[:2]

        top = 0
        bottom = int(height * 0.08)

        left = 0
        right = int(width * 0.45)

        return frame[top:bottom, left:right]

    def extract_price_region(self, frame):

        height, width = frame.shape[:2]

        left = int(width * 0.72)
        right = int(width * 0.80)

        top = int(height * 0.08)
        bottom = int(height * 0.92)

        return frame[top:bottom, left:right]

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

        return self.reader.readtext(
            image,
            detail=0
        )

    def extract_symbol(self, text_items):

        joined = " ".join(
            text_items
        ).upper()

        for symbol in self.symbols:

            if symbol in joined:
                return symbol

        return "UNKNOWN"

    def extract_timeframe(self, text_items):

        joined = " ".join(text_items)

        priority = [
            "1m",
            "3m",
            "5m",
            "15m",
            "30m",
            "1h",
            "4h",
            "D",
            "W",
            "M"
        ]

        found = []

        for tf in priority:

            if tf in joined:
                found.append(tf)

        if not found:
            return "UNKNOWN"

        if "1m" in found:
            return "1m"

        return found[0]

    def save_debug_regions(self, frame):

        header = self.extract_header_region(
            frame
        )

        price_area = self.extract_price_region(
            frame
        )

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
        print("===== OCR RAW HEADER =====")

        for item in header_text:
            print(item)

        symbol = self.extract_symbol(
            header_text
        )

        timeframe = self.extract_timeframe(
            header_text
        )

        return {
            "header": header,
            "price_area": price_area,
            "header_processed": header_processed,
            "price_processed": price_processed,
            "header_text": header_text,
            "price_text": price_text,
            "symbol": symbol,
            "timeframe": timeframe
        }
