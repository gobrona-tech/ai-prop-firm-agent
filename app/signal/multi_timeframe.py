
class MultiTimeframeAnalysis:

    def __init__(self):
        pass

    def analyze(
        self,
        higher_tf,
        setup_tf,
        entry_tf
    ):

        signals = [
            higher_tf,
            setup_tf,
            entry_tf
        ]

        bullish = len([
            s for s in signals
            if "BUY" in s
        ])

        bearish = len([
            s for s in signals
            if "SELL" in s
        ])

        if bullish == 3:
            return "STRONG BUY"

        if bearish == 3:
            return "STRONG SELL"

        if bullish >= 2:
            return "BUY"

        if bearish >= 2:
            return "SELL"

        return "NO TRADE"
