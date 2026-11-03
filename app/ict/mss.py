class MSSDetector:

    def __init__(self):
        pass

    def detect_bullish_mss(
        self,
        swing_highs,
        current_price
    ):

        if not swing_highs:
            return False

        last_high = swing_highs[-1]["price"]

        return current_price > last_high

    def detect_bearish_mss(
        self,
        swing_lows,
        current_price
    ):

        if not swing_lows:
            return False

        last_low = swing_lows[-1]["price"]

        return current_price < last_low
