import pygetwindow as gw


KNOWN_SYMBOLS = [
    "MNQ",
    "MES",
    "NQ",
    "ES",
    "BTCUSDT"
]


class TradingViewWindow:

    def find(self):

        for window in gw.getAllWindows():

            try:

                title = window.title

                if not title:
                    continue

                for symbol in KNOWN_SYMBOLS:

                    if symbol in title:

                        return {
                            "title": title,
                            "left": window.left,
                            "top": window.top,
                            "width": window.width,
                            "height": window.height
                        }

            except Exception:
                continue

        return None
