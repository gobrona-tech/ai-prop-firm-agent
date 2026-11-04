class FVGDetector:

    def __init__(self):
        pass

    def get_recent_window(
        self,
        candles,
        size=50
    ):

        if len(candles) <= size:
            return candles

        return candles[-size:]

    def build_fvg_series(
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
                    "direction": candle.get(
                        "direction",
                        "unknown"
                    )
                }
            )

        return series

    def find_bullish_fvg(
        self,
        candles
    ):

        fvgs = []

        candles = self.get_recent_window(
            candles,
            50
        )

        series = self.build_fvg_series(
            candles
        )

        for i in range(
            len(series) - 2
        ):

            candle_1 = series[i]
            candle_3 = series[i + 2]

            if (
                candle_1["bottom"] <
                candle_3["top"]
            ):

                gap_size = (
                    candle_3["top"] -
                    candle_1["bottom"]
                )

                if gap_size < 10:
                    continue

                if gap_size > 300:
                    continue

                fvgs.append(
                    {
                        "type": "bullish",
                        "index": i,
                        "x": candle_3["x"],
                        "top": candle_3["top"],
                        "bottom": candle_1["bottom"],
                        "size": gap_size
                    }
                )

        return fvgs

    def find_bearish_fvg(
        self,
        candles
    ):

        fvgs = []

        candles = self.get_recent_window(
            candles,
            50
        )

        series = self.build_fvg_series(
            candles
        )

        for i in range(
            len(series) - 2
        ):

            candle_1 = series[i]
            candle_3 = series[i + 2]

            if (
                candle_1["top"] >
                candle_3["bottom"]
            ):

                gap_size = (
                    candle_1["top"] -
                    candle_3["bottom"]
                )

                if gap_size < 10:
                    continue

                if gap_size > 300:
                    continue

                fvgs.append(
                    {
                        "type": "bearish",
                        "index": i,
                        "x": candle_3["x"],
                        "top": candle_1["top"],
                        "bottom": candle_3["bottom"],
                        "size": gap_size
                    }
                )

        return fvgs

    def get_largest_fvg(
        self,
        fvgs
    ):

        if not fvgs:
            return None

        return max(
            fvgs,
            key=lambda x: x["size"]
        )

    def analyze_fvg(
        self,
        candles
    ):

        bullish = self.find_bullish_fvg(
            candles
        )

        bearish = self.find_bearish_fvg(
            candles
        )

        return {
            "bullish": bullish,
            "bearish": bearish,
            "largest_bullish":
                self.get_largest_fvg(
                    bullish
                ),
            "largest_bearish":
                self.get_largest_fvg(
                    bearish
                )
        }
