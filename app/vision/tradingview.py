import pygetwindow as gw


class TradingViewWindow:

    def find(self):

        for window in gw.getAllWindows():

            try:
                title = window.title

                if "TradingView" in title:
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
