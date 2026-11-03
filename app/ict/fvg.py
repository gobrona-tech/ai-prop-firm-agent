class FVGDetector:

    def __init__(self):
        pass

    def find_bullish_fvg(self, candles):

        fvgs = []

        for i in range(len(candles) - 2):

            candle_1 = candles[i]
            candle_2 = candles[i + 1]
            candle_3 = candles[i + 2]

            if candle_1["high"] < candle_3["low"]:

                fvgs.append(
                    {
                        "type": "bullish",
                        "index": i,
                        "top": candle_3["low"],
                        "bottom": candle_1["high"]
                    }
                )

        return fvgs

    def find_bearish_fvg(self, candles):

        fvgs = []

        for i in range(len(candles) - 2):

            candle_1 = candles[i]
            candle_2 = candles[i + 1]
            candle_3 = candles[i + 2]

            if candle_1["low"] > candle_3["high"]:

                fvgs.append(
                    {
                        "type": "bearish",
                        "index": i,
                        "top": candle_1["low"],
                        "bottom": candle_3["high"]
                    }
                )

        return fvgs
