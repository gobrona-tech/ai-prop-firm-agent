class MSSDetector:

    def __init__(self):
        pass

    def detect_bullish_mss(
        self,
        swing_highs,
        current_price
    ):

        if len(swing_highs) < 1:
            return None

        last_high = swing_highs[-1]

        broken = (
            current_price >
            last_high["price"]
        )

        return {
            "direction": "bullish",
            "broken": broken,
            "level": last_high["price"],
            "index": last_high["index"]
        }

    def detect_bearish_mss(
        self,
        swing_lows,
        current_price
    ):

        if len(swing_lows) < 1:
            return None

        last_low = swing_lows[-1]

        broken = (
            current_price <
            last_low["price"]
        )

        return {
            "direction": "bearish",
            "broken": broken,
            "level": last_low["price"],
            "index": last_low["index"]
        }

    def get_market_bias(
        self,
        bullish_mss,
        bearish_mss
    ):

        if bullish_mss and bullish_mss["broken"]:
            return "bullish"

        if bearish_mss and bearish_mss["broken"]:
            return "bearish"

        return "neutral"
