import csv
from blur_detector import detect_blur

def evaluate(threshold=100):
    correct = 0
    total = 0

    print(f"\n--- Evaluating with threshold = {threshold} ---")

    with open("labels.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            filename = row["filename"]
            true_label = row["true_label"]

            image_path = f"sample_images/{filename}"

            score, predicted = detect_blur(image_path, threshold)

            print(f"{filename} → Predicted: {predicted}, Actual: {true_label}")

            if predicted.lower() == true_label.lower():
                correct += 1
            
            total += 1

    accuracy = correct / total
    print(f"Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    evaluate(100)
    evaluate(228)
    evaluate(340)
