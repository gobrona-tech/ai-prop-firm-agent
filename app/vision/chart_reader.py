def detect_candle_candidates(
    self,
    mask,
    direction
):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    candles = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(
            contour
        )

        area = w * h

        if h < 12:
            continue

        if h > 250:
            continue

        if w < 4:
            continue

        if w > 20:
            continue

        if area < 80:
            continue

        candles.append(
            {
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "area": area,
                "direction": direction
            }
        )

    return candles
