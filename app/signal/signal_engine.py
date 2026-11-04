class SignalEngine:

    def build_signal(
        self,
        summary
    ):

        bias = summary["bias"]

        bullish_fvgs = summary[
            "bullish_fvgs"
        ]

        bearish_fvgs = summary[
            "bearish_fvgs"
        ]

        bullish_obs = summary[
            "bullish_obs"
        ]

        bearish_obs = summary[
            "bearish_obs"
        ]

        score = 0

        if bias == "bullish":
            score += 2

        if bias == "bearish":
            score -= 2

        score += (
            bullish_fvgs -
            bearish_fvgs
        )

        score += (
            bullish_obs -
            bearish_obs
        )

        if score >= 3:
            return "STRONG BUY"

        if score >= 1:
            return "BUY"

        if score <= -3:
            return "STRONG SELL"

        if score <= -1:
            return "SELL"

        return "NEUTRAL"
