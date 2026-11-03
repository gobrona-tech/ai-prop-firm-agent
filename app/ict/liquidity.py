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
                        "index": i,
                        "price": lows[i]
                    }
                )

        return swing_lows
