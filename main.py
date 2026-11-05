from app.vision.detector import VisionDetector
from app.ict.liquidity import LiquidityDetector
from app.ict.mss import MSSDetector
from app.ict.fvg import FVGDetector
from app.ict.orderblock import OrderBlockDetector
from app.signal.signal_engine import SignalEngine
from app.signal.trade_setup import TradeSetup


def main():

    detector = VisionDetector()
    liquidity = LiquidityDetector()
    mss = MSSDetector()
    fvg = FVGDetector()
    orderblock = OrderBlockDetector()
    engine = SignalEngine()
    setup_engine = TradeSetup()

    result = detector.scan()

    if not result["success"]:
        print(result["message"])
        return

    symbol = "UNKNOWN"
    timeframe = "UNKNOWN"

    if "regions" in result:

        symbol = result["regions"].get(
            "symbol",
            "UNKNOWN"
        )

        timeframe = result["regions"].get(
            "timeframe",
            "UNKNOWN"
        )

    # Vision timeframe overrides OCR timeframe
    if "timeframe_debug" in result:

        detected_timeframe = (
            result["timeframe_debug"].get(
                "active"
            )
        )

        if (
            detected_timeframe and
            detected_timeframe != "UNKNOWN"
        ):

            timeframe = (
                detected_timeframe
            )

    if "chart_debug" not in result:
        return

    stats = result["chart_debug"].get(
        "stats",
        {}
    )

    candles = stats.get(
        "candles",
        []
    )

    if not candles:
        return

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

    orderblock_data = (
        orderblock.analyze_orderblocks(
            candles
        )
    )

    signal_summary = {

        "symbol": symbol,
        "timeframe": timeframe,
        "bias": structure["bias"],

        "candles": stats.get(
            "total",
            0
        ),

        "swing_highs": len(
            swing_highs
        ),

        "swing_lows": len(
            swing_lows
        ),

        "liquidity_levels": len(
            liquidity_map
        ),

        "bullish_fvgs": len(
            fvg_data["bullish"]
        ),

        "bearish_fvgs": len(
            fvg_data["bearish"]
        ),

        "bullish_obs": len(
            orderblock_data["bullish"]
        ),

        "bearish_obs": len(
            orderblock_data["bearish"]
        ),

        "largest_bullish_fvg":
            fvg_data["largest_bullish"],

        "largest_bearish_fvg":
            fvg_data["largest_bearish"],

        "strongest_bullish_ob":
            orderblock_data[
                "strongest_bullish"
            ],

        "strongest_bearish_ob":
            orderblock_data[
                "strongest_bearish"
            ]
    }

    decision = engine.analyze(
        signal_summary
    )

    print()
    print("================================")
    print("TIMEFRAME DEBUG")
    print("================================")

    print(
        result.get(
            "timeframe_debug",
            {}
        )
    )

    signal_summary["signal"] = (
        decision["signal"]
    )

    trade_setup = (
        setup_engine.build_setup(
            signal_summary
        )
    )

    print()
    print("================================")
    print("SIGNAL SUMMARY")
    print("================================")
    print()

    for key, value in signal_summary.items():

        print(
            f"{key}: {value}"
        )

    print()
    print("================================")
    print("TRADE SIGNAL")
    print("================================")

    print(
        f"Score: "
        f"{decision['score']}"
    )

    print(
        f"Signal: "
        f"{decision['signal']}"
    )

    print()
    print("================================")
    print("TRADE SETUP")
    print("================================")

    for key, value in trade_setup.items():

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()
