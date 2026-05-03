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
