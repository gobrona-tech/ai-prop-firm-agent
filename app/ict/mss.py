class MSSDetector:

    def __init__(self):
        pass

    def detect_bullish_mss(
        self,
        swing_highs,
        current_value
    ):

        if not swing_highs:
            return None

        last_high = swing_highs[-1]

        broken = (
            current_value >
            last_high["value"]
        )

        return {
            "direction": "bullish",
            "broken": broken,
            "level": last_high["value"],
            "x": last_high["x"]
        }

    def detect_bearish_mss(
        self,
        swing_lows,
        current_value
    ):

        if not swing_lows:
            return None

        last_low = swing_lows[-1]

        broken = (
            current_value <
            last_low["value"]
        )

        return {
            "direction": "bearish",
            "broken": broken,
            "level": last_low["value"],
            "x": last_low["x"]
        }

    def get_market_bias(
        self,
        bullish_mss,
        bearish_mss
    ):

        if (
            bullish_mss and
            bullish_mss["broken"]
        ):
            return "bullish"

        if (
            bearish_mss and
            bearish_mss["broken"]
        ):
            return "bearish"

        return "neutral"

    def analyze_structure(
        self,
        swing_highs,
        swing_lows,
        current_value
    ):

        bullish = self.detect_bullish_mss(
            swing_highs,
            current_value
        )

        bearish = self.detect_bearish_mss(
            swing_lows,
            current_value
        )

        bias = self.get_market_bias(
            bullish,
            bearish
        )

        return {
            "bullish_mss": bullish,
            "bearish_mss": bearish,
            "bias": bias
        }
