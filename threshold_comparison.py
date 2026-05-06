import csv
import matplotlib.pyplot as plt
from blur_detector import detect_blur

def compute_accuracy(threshold):
    correct = 0
    total = 0

    with open("labels.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            filename = row["filename"]
            true_label = row["true_label"]

            image_path = f"sample_images/{filename}"
            score, predicted = detect_blur(image_path, threshold)

            if predicted.lower() == true_label.lower():
                correct += 1
            
            total += 1

    return correct / total


# Thresholds to test
thresholds = [100, 393, 757]

accuracies = []

for t in thresholds:
    acc = compute_accuracy(t)
    accuracies.append(acc)
    print(f"Threshold {t} → Accuracy {acc:.2f}")


# Plot
plt.figure(figsize=(6,4))
plt.bar([str(t) for t in thresholds], accuracies)

plt.xlabel("Threshold")
plt.ylabel("Accuracy")
plt.title("Threshold vs Accuracy")

plt.savefig("threshold_comparison.png")
print("Plot saved as threshold_comparison.png")
