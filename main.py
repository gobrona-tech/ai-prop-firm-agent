from app.vision.detector import VisionDetector
from app.ict.liquidity import LiquidityDetector
from app.ict.mss import MSSDetector
from app.ict.fvg import FVGDetector


def main():

    detector = VisionDetector()
    liquidity = LiquidityDetector()
    mss = MSSDetector()
    fvg = FVGDetector()

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

            current_value = swings[-1]["value"]

            structure = (
                mss.analyze_structure(
                    swing_highs,
                    swing_lows,
                    current_value
                )
            )

            fvg_data = (
                fvg.analyze_fvg(
                    candles
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

            print()
            print("================================")
            print("MARKET STRUCTURE")
            print("================================")

            print(
                f"Bias: "
                f"{structure['bias']}"
            )

            print(
                f"Bullish MSS: "
                f"{structure['bullish_mss']}"
            )

            print(
                f"Bearish MSS: "
                f"{structure['bearish_mss']}"
            )

            print()
            print("================================")
            print("FVG")
            print("================================")

            print(
                f"Bullish FVGs: "
                f"{len(fvg_data['bullish'])}"
            )

            print(
                f"Bearish FVGs: "
                f"{len(fvg_data['bearish'])}"
            )

            print()

            print(
                "Largest Bullish FVG:"
            )

            print(
                fvg_data[
                    "largest_bullish"
                ]
            )

            print()

            print(
                "Largest Bearish FVG:"
            )

            print(
                fvg_data[
                    "largest_bearish"
                ]
            )


if __name__ == "__main__":
    main()
