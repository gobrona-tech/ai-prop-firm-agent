from app.vision.detector import VisionDetector


def main():

    detector = VisionDetector()

    result = detector.scan()

    if not result["success"]:
        print(result["message"])
        return

    print("================================")
    print("TRADINGVIEW DETECTED")
    print("================================")

    print(result["window"]["title"])
    print()

    print(f"WIDTH: {result['window']['width']}")
    print(f"HEIGHT: {result['window']['height']}")
    print()

    print(f"FRAME SHAPE: {result['frame'].shape}")


if __name__ == "__main__":
    main()
