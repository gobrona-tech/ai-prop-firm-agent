class OrderBlockDetector:

    def __init__(self):
        pass

    def build_orderblock_series(
        self,
        candles
    ):

        series = []

        for candle in candles:

            top = candle["y"]

            bottom = (
                candle["y"] +
                candle["height"]
            )

            series.append(
                {
                    "x": candle["x"],
                    "top": top,
                    "bottom": bottom,
                    "height": candle["height"],
                    "direction": candle.get(
                        "direction",
                        "unknown"
                    )
                }
            )

        return series

    def find_bullish_orderblocks(
        self,
        candles
    ):

        orderblocks = []

        series = self.build_orderblock_series(
            candles
        )

        for i in range(
            len(series) - 1
        ):

            current = series[i]
            next_candle = series[i + 1]

            if (
                current["direction"] ==
                "bearish"
                and
                next_candle["direction"] ==
                "bullish"
            ):

                orderblocks.append(
                    {
                        "type": "bullish",
                        "index": i,
                        "x": current["x"],
                        "top": current["top"],
                        "bottom": current["bottom"],
                        "strength": current["height"]
                    }
                )

        return orderblocks

    def find_bearish_orderblocks(
        self,
        candles
    ):

        orderblocks = []

        series = self.build_orderblock_series(
            candles
        )

        for i in range(
            len(series) - 1
        ):

            current = series[i]
            next_candle = series[i + 1]

            if (
                current["direction"] ==
                "bullish"
                and
                next_candle["direction"] ==
                "bearish"
            ):

                orderblocks.append(
                    {
                        "type": "bearish",
                        "index": i,
                        "x": current["x"],
                        "top": current["top"],
                        "bottom": current["bottom"],
                        "strength": current["height"]
                    }
                )

        return orderblocks

    def get_strongest_orderblock(
        self,
        orderblocks
    ):

        if not orderblocks:
            return None

        return max(
            orderblocks,
            key=lambda x: x["strength"]
        )

    def analyze_orderblocks(
        self,
        candles
    ):

        bullish = (
            self.find_bullish_orderblocks(
                candles
            )
        )

        bearish = (
            self.find_bearish_orderblocks(
                candles
            )
        )

        return {
            "bullish": bullish,
            "bearish": bearish,
            "strongest_bullish":
                self.get_strongest_orderblock(
                    bullish
                ),
            "strongest_bearish":
                self.get_strongest_orderblock(
                    bearish
                )
        }
