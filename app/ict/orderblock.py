
class OrderBlockDetector:

    def __init__(self):
        pass

    def find_bullish_orderblocks(self, candles):

        orderblocks = []

        for i in range(len(candles) - 1):

            current = candles[i]
            next_candle = candles[i + 1]

            bearish_candle = (
                current["close"] < current["open"]
            )

            displacement_up = (
                next_candle["close"] > current["high"]
            )

            if bearish_candle and displacement_up:

                orderblocks.append(
                    {
                        "type": "bullish",
                        "index": i,
                        "high": current["high"],
                        "low": current["low"]
                    }
                )

        return orderblocks

    def find_bearish_orderblocks(self, candles):

        orderblocks = []

        for i in range(len(candles) - 1):

            current = candles[i]
            next_candle = candles[i + 1]

            bullish_candle = (
                current["close"] > current["open"]
            )

            displacement_down = (
                next_candle["close"] < current["low"]
            )

            if bullish_candle and displacement_down:

                orderblocks.append(
                    {
                        "type": "bearish",
                        "index": i,
                        "high": current["high"],
                        "low": current["low"]
                    }
                )

        return orderblocks
