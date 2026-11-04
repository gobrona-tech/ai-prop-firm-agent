class LiquidityDetector:

    def __init__(self):
        pass

    def find_swing_highs(self, highs):

        swing_highs = []

        for i in range(2, len(highs) - 2):

            if (
                highs[i] > highs[i - 1]
                and highs[i] > highs[i - 2]
                and highs[i] > highs[i + 1]
                and highs[i] > highs[i + 2]
            ):

                swing_highs.append(
                    {
                        "type": "swing_high",
                        "index": i,
                        "price": highs[i]
                    }
                )

        return swing_highs

    def find_swing_lows(self, lows):

        swing_lows = []

        for i in range(2, len(lows) - 2):

            if (
                lows[i] < lows[i - 1]
                and lows[i] < lows[i - 2]
                and lows[i] < lows[i + 1]
                and lows[i] < lows[i + 2]
            ):

                swing_lows.append(
                    {
                        "type": "swing_low",
                        "index": i,
                        "price": lows[i]
                    }
                )

        return swing_lows

    def build_liquidity_map(
        self,
        swing_highs,
        swing_lows
    ):

        liquidity_map = []

        for high in swing_highs:

            liquidity_map.append(
                {
                    "type": "buy_side_liquidity",
                    "index": high["index"],
                    "price": high["price"]
                }
            )

        for low in swing_lows:

            liquidity_map.append(
                {
                    "type": "sell_side_liquidity",
                    "index": low["index"],
                    "price": low["price"]
                }
            )

        return liquidity_map
