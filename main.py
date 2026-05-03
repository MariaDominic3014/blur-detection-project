from blur_detector import detect_blur
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    try:
        score, result = detect_blur(image_path)
        print(f"Image: {image_path}")
        print(f"Blur score: {score:.2f}")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
