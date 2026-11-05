class LiquidityDetector:

    def __init__(self):

        self.swing_window = 5
        self.min_distance = 15

    def build_swing_series(
        self,
        candles
    ):

        swings = []

        candles = sorted(
            candles,
            key=lambda x: x["x"]
        )

        for candle in candles:

            top = candle["y"]

            bottom = (
                candle["y"] +
                candle["height"]
            )

            center = (
                top +
                bottom
            ) // 2

            swings.append(
                {
                    "x": candle["x"],
                    "top": top,
                    "bottom": bottom,
                    "center": center
                }
            )

        return swings

    def is_swing_high(
        self,
        swings,
        index
    ):

        current = swings[index]["top"]

        left = swings[
            index -
            self.swing_window:index
        ]

        right = swings[
            index + 1:
            index +
            self.swing_window + 1
        ]

        if (
            len(left) <
            self.swing_window
        ):
            return False

        if (
            len(right) <
            self.swing_window
        ):
            return False

        highest_neighbor = min(
            [x["top"] for x in left] +
            [x["top"] for x in right]
        )

        distance = abs(
            current -
            highest_neighbor
        )

        return (
            current <
            highest_neighbor
            and
            distance >=
            self.min_distance
        )

    def is_swing_low(
        self,
        swings,
        index
    ):

        current = swings[index]["bottom"]

        left = swings[
            index -
            self.swing_window:index
        ]

        right = swings[
            index + 1:
            index +
            self.swing_window + 1
        ]

        if (
            len(left) <
            self.swing_window
        ):
            return False

        if (
            len(right) <
            self.swing_window
        ):
            return False

        lowest_neighbor = max(
            [x["bottom"] for x in left] +
            [x["bottom"] for x in right]
        )

        distance = abs(
            current -
            lowest_neighbor
        )

        return (
            current >
            lowest_neighbor
            and
            distance >=
            self.min_distance
        )

    def find_swing_highs(
        self,
        swings
    ):

        swing_highs = []

        for i in range(
            self.swing_window,
            len(swings) -
            self.swing_window
        ):

            if not self.is_swing_high(
                swings,
                i
            ):
                continue

            swing_highs.append(
                {
                    "type":
                        "swing_high",
                    "index": i,
                    "x":
                        swings[i]["x"],
                    "value":
                        swings[i]["top"],
                    "confidence": 100
                }
            )

        return swing_highs

    def find_swing_lows(
        self,
        swings
    ):

        swing_lows = []

        for i in range(
            self.swing_window,
            len(swings) -
            self.swing_window
        ):

            if not self.is_swing_low(
                swings,
                i
            ):
                continue

            swing_lows.append(
                {
                    "type":
                        "swing_low",
                    "index": i,
                    "x":
                        swings[i]["x"],
                    "value":
                        swings[i]["bottom"],
                    "confidence": 100
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
                    "type":
                        "buy_side_liquidity",
                    "x":
                        high["x"],
                    "value":
                        high["value"],
                    "confidence":
                        high.get(
                            "confidence",
                            0
                        )
                }
            )

        for low in swing_lows:

            liquidity_map.append(
                {
                    "type":
                        "sell_side_liquidity",
                    "x":
                        low["x"],
                    "value":
                        low["value"],
                    "confidence":
                        low.get(
                            "confidence",
                            0
                        )
                }
            )

        return liquidity_map
