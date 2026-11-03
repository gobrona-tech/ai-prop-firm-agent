import pygetwindow as gw


BLOCKLIST = [
    "Windows Input Experience",
    "Program Manager",
    "Settings",
    "Task Manager",
    "Administrator:",
    "Copilot",
    "Spotify",
    "Google Chrome",
    "github.com",
    "ai-prop-firm-agent"
]

TARGET_HINTS = [
    "MNQ",
    "MES",
    "NQ",
    "ES",
    "BTCUSDT",
    "Unnamed"
]


class TradingViewWindow:

    def find(self):

        candidates = []

        for window in gw.getAllWindows():

            try:

                title = window.title

                if not title:
                    continue

                blocked = False

                for item in BLOCKLIST:

                    if item.lower() in title.lower():
                        blocked = True
                        break

                if blocked:
                    continue

                if window.width < 800:
                    continue

                if window.height < 500:
                    continue

                score = 0

                for hint in TARGET_HINTS:

                    if hint.lower() in title.lower():
                        score += 100

                score += int(
                    (window.width * window.height) / 100000
                )

                candidates.append(
                    {
                        "score": score,
                        "title": title,
                        "left": window.left,
                        "top": window.top,
                        "width": window.width,
                        "height": window.height
                    }
                )

            except Exception:
                continue

        if not candidates:
            return None

        candidates.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return {
            "title": candidates[0]["title"],
            "left": candidates[0]["left"],
            "top": candidates[0]["top"],
            "width": candidates[0]["width"],
            "height": candidates[0]["height"]
        }
