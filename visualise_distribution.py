import csv
import matplotlib.pyplot as plt
from blur_detector import detect_blur

sharp_scores = []
blurry_scores = []

with open("labels.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        filename = row["filename"]
        label = row["true_label"]

        image_path = f"sample_images/{filename}"
        score, _ = detect_blur(image_path)

        if label.lower() == "sharp":
            sharp_scores.append(score)
        else:
            blurry_scores.append(score)

# Plot histogram
plt.figure(figsize=(8,5))

plt.hist(sharp_scores, bins=10, alpha=0.7, label="Sharp")
plt.hist(blurry_scores, bins=10, alpha=0.7, label="Blurry")

plt.xlabel("Laplacian Variance (Blur Score)")
plt.ylabel("Frequency")
plt.title("Blur Score Distribution")
plt.legend()

plt.show()
