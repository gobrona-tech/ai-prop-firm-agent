class LiquidityDetector:

    def __init__(self):
        pass

    def build_swing_series(
        self,
        candles
    ):

        swings = []

        for candle in candles:

            swing_value = (
                candle["y"] +
                candle["height"]
            )

            swings.append(
                {
                    "x": candle["x"],
                    "value": swing_value
                }
            )

        return swings

    def find_swing_highs(
        self,
        swings
    ):

        swing_highs = []

        for i in range(
            2,
            len(swings) - 2
        ):

            current = swings[i]["value"]

            if (
                current >
                swings[i - 1]["value"]
                and current >
                swings[i - 2]["value"]
                and current >
                swings[i + 1]["value"]
                and current >
                swings[i + 2]["value"]
            ):

                swing_highs.append(
                    {
                        "type": "swing_high",
                        "index": i,
                        "x": swings[i]["x"],
                        "value": current
                    }
                )

        return swing_highs

    def find_swing_lows(
        self,
        swings
    ):

        swing_lows = []

        for i in range(
            2,
            len(swings) - 2
        ):

            current = swings[i]["value"]

            if (
                current <
                swings[i - 1]["value"]
                and current <
                swings[i - 2]["value"]
                and current <
                swings[i + 1]["value"]
                and current <
                swings[i + 2]["value"]
            ):

                swing_lows.append(
                    {
                        "type": "swing_low",
                        "index": i,
                        "x": swings[i]["x"],
                        "value": current
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
                    "x": high["x"],
                    "value": high["value"]
                }
            )

        for low in swing_lows:

            liquidity_map.append(
                {
                    "type": "sell_side_liquidity",
                    "x": low["x"],
                    "value": low["value"]
                }
            )

        return liquidity_map
