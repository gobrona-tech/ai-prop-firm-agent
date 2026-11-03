from app.vision.detector import VisionDetector


def main():

    detector = VisionDetector()

    result = detector.scan()

    if not result["success"]:
        print(result["message"])
        return

    print("TradingView detected")
    print(result["window"]["title"])
    print(result["frame"].shape)


if __name__ == "__main__":
    main()
