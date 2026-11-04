from app.vision.detector import VisionDetector


def main():

    detector = VisionDetector()

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

            print()

            print(
                f"First Candle X: "
                f"{candles[0]['x']}"
            )

            print(
                f"Last Candle X: "
                f"{candles[-1]['x']}"
            )

            print()

            print("Recent Candles:")

            for candle in candles[-5:]:

                print(
                    f"x={candle['x']} "
                    f"y={candle['y']} "
                    f"w={candle['width']} "
                    f"h={candle['height']}"
                )


if __name__ == "__main__":
    main()
