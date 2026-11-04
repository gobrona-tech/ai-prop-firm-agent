from app.vision.detector import VisionDetector
from app.ict.liquidity import LiquidityDetector


def main():

    detector = VisionDetector()
    liquidity = LiquidityDetector()

    result = detector.scan()

    if not result["success"]:

        print(result["message"])
        return

    print("================================")
    print("MARKET INFO")
    print("================================")

    if "regions" in result:

        symbol = result["regions"].get(
            "symbol",
            "UNKNOWN"
        )

        timeframe = result["regions"].get(
            "timeframe",
            "UNKNOWN"
        )

        print(f"Symbol: {symbol}")
        print(f"Timeframe: {timeframe}")

    print()

    print("================================")
    print("TRADINGVIEW DETECTED")
    print("================================")

    print(result["window"]["title"])

    print()

    print(
        f"WIDTH: {result['window']['width']}"
    )

    print(
        f"HEIGHT: {result['window']['height']}"
    )

    print()

    print(
        f"FRAME SHAPE: {result['frame'].shape}"
    )

    if "chart_info" in result:

        print()

        print("================================")
        print("CHART INFO")
        print("================================")

        print(
            f"Chart Width: "
            f"{result['chart_info']['width']}"
        )

        print(
            f"Chart Height: "
            f"{result['chart_info']['height']}"
        )

        print(
            f"Center X: "
            f"{result['chart_info']['center_x']}"
        )

        print(
            f"Center Y: "
            f"{result['chart_info']['center_y']}"
        )

    if "chart_debug" in result:

        stats = result["chart_debug"].get(
            "stats",
            {}
        )

        candles = stats.get(
            "candles",
            []
        )

        print()

        print("================================")
        print("CANDLE DETECTION")
        print("================================")

        print(
            f"Total Candles Found: "
            f"{stats.get('total', 0)}"
        )

        print(
            f"Bullish Candles Found: "
            f"{stats.get('bullish', 0)}"
        )

        print(
            f"Bearish Candles Found: "
            f"{stats.get('bearish', 0)}"
        )

        if candles:

            swings = liquidity.build_swing_series(
                candles
            )

            swing_highs = (
                liquidity.find_swing_highs(
                    swings
                )
            )

            swing_lows = (
                liquidity.find_swing_lows(
                    swings
                )
            )

            liquidity_map = (
                liquidity.build_liquidity_map(
                    swing_highs,
                    swing_lows
                )
            )

            print()

            print("================================")
            print("LIQUIDITY")
            print("================================")

            print(
                f"Swing Highs: "
                f"{len(swing_highs)}"
            )

            print(
                f"Swing Lows: "
                f"{len(swing_lows)}"
            )

            print(
                f"Liquidity Levels: "
                f"{len(liquidity_map)}"
            )

            if swing_highs:

                print()

                print(
                    "Latest Swing High:"
                )

                print(
                    swing_highs[-1]
                )

            if swing_lows:

                print()

                print(
                    "Latest Swing Low:"
                )

                print(
                    swing_lows[-1]
                )


if __name__ == "__main__":
    main()
