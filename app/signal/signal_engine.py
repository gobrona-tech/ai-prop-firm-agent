class SignalEngine:

    def __init__(self):
        pass

    def get_fvg_score(
        self,
        summary
    ):

        score = 0

        bullish_fvg = summary.get(
            "largest_bullish_fvg"
        )

        bearish_fvg = summary.get(
            "largest_bearish_fvg"
        )

        if bullish_fvg:

            size = bullish_fvg["size"]

            if size >= 150:
                score += 3
            elif size >= 75:
                score += 2
            elif size >= 30:
                score += 1

        if bearish_fvg:

            size = bearish_fvg["size"]

            if size >= 150:
                score -= 3
            elif size >= 75:
                score -= 2
            elif size >= 30:
                score -= 1

        return score

    def get_ob_score(
        self,
        summary
    ):

        score = 0

        bullish_ob = summary.get(
            "strongest_bullish_ob"
        )

        bearish_ob = summary.get(
            "strongest_bearish_ob"
        )

        if bullish_ob:

            strength = bullish_ob["strength"]

            if strength >= 120:
                score += 3
            elif strength >= 80:
                score += 2
            elif strength >= 40:
                score += 1

        if bearish_ob:

            strength = bearish_ob["strength"]

            if strength >= 120:
                score -= 3
            elif strength >= 80:
                score -= 2
            elif strength >= 40:
                score -= 1

        return score

    def calculate_score(
        self,
        summary
    ):

        score = 0

        bias = summary.get(
            "bias",
            "neutral"
        )

        if bias == "bullish":
            score += 5

        elif bias == "bearish":
            score -= 5

        score += self.get_fvg_score(
            summary
        )

        score += self.get_ob_score(
            summary
        )

        return score

    def get_signal(
        self,
        summary
    ):

        score = self.calculate_score(
            summary
        )

        if score >= 8:
            return "STRONG BUY"

        if score >= 3:
            return "BUY"

        if score <= -8:
            return "STRONG SELL"

        if score <= -3:
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
