# 🧠 Blur Detection using Laplacian Variance
This project implements a simple image blur detection system using the Variance of Laplacian method from computer vision.

---

## 📌 How it works
- Convert image to grayscale  
- Apply Laplacian operator to detect edges  
- Compute variance of the result  
- Low variance → blurry image  
- High variance → sharp image  

---

## 🚀 Usage
```bash
python main.py <image_path>
```
Example:   
```python main.py sample_images/dog.png```

---

## 📊 Example Output
Image: dog.png   
Blur score: 41.23   
Result: Blurry

---

## 🛠 Technologies Used
- Python
- OpenCV
- NumPy

---

## 📚 Key Concepts
- Edge detection
- Image representation
- Variance as a statistical measure
- Threshold-based classification

---

## 🔧 Future Improvements
- Automatic threshold selection
- Compare with Sobel operator
- Batch image processing
- Dataset-based evaluation

---

## 📊 Results

The model was evaluated on a labelled dataset of natural images using different thresholding strategies for classifying blur based on Laplacian variance.
| Threshold | Method          | Accuracy |
| --------- | --------------- | -------- |
| 100       | Fixed threshold | 0.73     |
| 393       | Median-based    | 0.73     |
| 757       | Mean-based      | 0.73     |

---

## 🔍 Observations
All three thresholding approaches resulted in the same overall accuracy (73%), but produced different misclassification patterns.
Lower thresholds (e.g. 100) tended to classify more images as sharp, while higher thresholds (e.g. 757) classified more images as blurry.
Some images were consistently misclassified across all thresholds, particularly those with high texture (e.g. foliage, landscapes).

---

## ⚠️ Limitations
The Laplacian variance method is sensitive to image texture, which can lead to high variance even in blurred images.
Fixed thresholding is not robust across diverse image types.
Performance is dependent on dataset composition and distribution of variance values.

---

## 🧠 Key Insight
While threshold tuning changes classification behaviour, it does not necessarily improve overall accuracy. This suggests that feature limitations (Laplacian variance alone) are a more significant bottleneck than threshold selection.
