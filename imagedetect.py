import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
# Load the input image
image = cv2.imread("image2.webp")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or other preprocessing as needed
# For example, you can use thresholding to enhance the contrast
# ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Define the region of interest (ROI) containing the license plate
# Replace the following values with the actual coordinates
x = 100  # X-coordinate of the top-left corner of the ROI
y = 200  # Y-coordinate of the top-left corner of the ROI
w = 300  # Width of the ROI
h = 100  # Height of the ROI

# Use Tesseract to perform OCR on the license plate ROI
license_plate_roi = gray[y:y+h, x:x+w]

# Perform OCR on the license plate ROI
license_plate_text = pytesseract.image_to_string(license_plate_roi)

# Print the recognized license plate text
print("License Plate Number:", license_plate_text)

# Display the original image with the license plate region highlighted
cv2.imshow("License Plate Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
