class TradeSetup:

    def __init__(self):
        pass

    def build_setup(
        self,
        summary
    ):

        signal = summary.get(
            "signal",
            "NEUTRAL"
        )

        if "SELL" in signal:

            reference = (
                summary.get(
                    "strongest_bearish_ob"
                )
            )

            if reference:

                return {
                    "direction": "SELL",
                    "entry_top":
                        reference["top"],
                    "entry_bottom":
                        reference["bottom"],
                    "strength":
                        reference["strength"]
                }

        if "BUY" in signal:

            reference = (
                summary.get(
                    "strongest_bullish_ob"
                )
            )

            if reference:

                return {
                    "direction": "BUY",
                    "entry_top":
                        reference["top"],
                    "entry_bottom":
                        reference["bottom"],
                    "strength":
                        reference["strength"]
                }

        return {
            "direction": "NONE"
        }
