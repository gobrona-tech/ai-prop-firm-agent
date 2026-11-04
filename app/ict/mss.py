class MSSDetector:

    def __init__(self):
        pass

    def get_recent_swings(
        self,
        swings,
        size=5
    ):

        if len(swings) <= size:
            return swings

        return swings[-size:]

    def detect_bullish_mss(
        self,
        swing_highs,
        current_value
    ):

        swing_highs = self.get_recent_swings(
            swing_highs,
            5
        )

        if not swing_highs:
            return None

        last_high = swing_highs[-1]

        broken = (
            current_value >
            last_high["value"]
        )

        distance = abs(
            current_value -
            last_high["value"]
        )

        return {
            "direction": "bullish",
            "broken": broken,
            "level": last_high["value"],
            "x": last_high["x"],
            "distance": distance
        }

    def detect_bearish_mss(
        self,
        swing_lows,
        current_value
    ):

        swing_lows = self.get_recent_swings(
            swing_lows,
            5
        )

        if not swing_lows:
            return None

        last_low = swing_lows[-1]

        broken = (
            current_value <
            last_low["value"]
        )

        distance = abs(
            current_value -
            last_low["value"]
        )

        return {
            "direction": "bearish",
            "broken": broken,
            "level": last_low["value"],
            "x": last_low["x"],
            "distance": distance
        }

    def get_market_bias(
        self,
        bullish_mss,
        bearish_mss
    ):

        bullish_broken = (
            bullish_mss and
            bullish_mss["broken"]
        )

        bearish_broken = (
            bearish_mss and
            bearish_mss["broken"]
        )

        if bullish_broken and not bearish_broken:
            return "bullish"

        if bearish_broken and not bullish_broken:
            return "bearish"

        if bullish_broken and bearish_broken:

            if (
                bullish_mss["distance"] <
                bearish_mss["distance"]
            ):
                return "bullish"

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
