import csv
import cv2
import matplotlib.pyplot as plt
from blur_detector import detect_blur

with open("labels.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        filename = row["filename"]
        true_label = row["true_label"]

        image_path = f"sample_images/{filename}"

        # Get prediction + score
        score, predicted = detect_blur(image_path, threshold=100)

        # Load image for display
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Plot
        plt.figure(figsize=(4,4))
        plt.imshow(image_rgb)
        plt.axis("off")

        plt.title(f"Pred: {predicted} | Actual: {true_label}\nScore: {score:.2f}")

        # Save each image
        save_name = f"prediction_{filename}.png"
        plt.savefig(save_name)
        plt.close()

        print(f"Saved {save_name}")
