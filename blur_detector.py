import cv2

def detect_blur(image_path, threshold=100):
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    variance = laplacian.var()

    result = "Blurry" if variance < threshold else "Sharp"
    
    return variance, result
