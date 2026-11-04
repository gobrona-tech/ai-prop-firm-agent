class SignalEngine:

    def __init__(self):
        pass

    def calculate_score(
        self,
        summary
    ):

        score = 0

        if summary["bias"] == "bullish":
            score += 3

        elif summary["bias"] == "bearish":
            score -= 3

        score += (
            summary["bullish_fvgs"] -
            summary["bearish_fvgs"]
        )

        score += (
            summary["bullish_obs"] -
            summary["bearish_obs"]
        )

        return score

    def get_signal(
        self,
        summary
    ):

        score = self.calculate_score(
            summary
        )

        if score >= 5:
            return "STRONG BUY"

        if score >= 2:
            return "BUY"

        if score <= -5:
            return "STRONG SELL"

        if score <= -2:
            return "SELL"

        return "NEUTRAL"

    def analyze(
        self,
        summary
    ):

        score = self.calculate_score(
            summary
        )

        signal = self.get_signal(
            summary
        )

        return {
            "score": score,
            "signal": signal
        }
