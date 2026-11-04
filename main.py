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

        bullish = len(
            result["chart_debug"].get(
                "bullish_candles",
                []
            )
        )

        bearish = len(
            result["chart_debug"].get(
                "bearish_candles",
                []
            )
        )

        print()

        print("================================")
        print("CANDLE DETECTION")
        print("================================")

        print(
            f"Bullish Candles Found: {bullish}"
        )

        print(
            f"Bearish Candles Found: {bearish}"
        )


if __name__ == "__main__":
    main()
