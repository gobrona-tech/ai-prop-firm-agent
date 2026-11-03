import pygetwindow as gw


class TradingViewWindow:

    def find(self):

        candidates = []

        for window in gw.getAllWindows():

            try:

                title = window.title

                if not title:
                    continue

                if window.width < 800:
                    continue

                if window.height < 500:
                    continue

                candidates.append(
                    {
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
            key=lambda x: x["width"] * x["height"],
            reverse=True
        )

        return candidates[0]
