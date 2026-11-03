import pygetwindow as gw

for window in gw.getAllWindows():

    try:

        if window.title:

            print(
                f"{window.title} | "
                f"{window.width}x{window.height}"
            )

    except:
        pass
