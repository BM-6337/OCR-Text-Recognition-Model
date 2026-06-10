import cv2
import pytesseract

IMAGE_PATH = './testimg.jpg'

def extract_text_from_regions(original, contours):
    """
    Iterates over detected contours, draws bounding boxes,
    and runs OCR on each cropped region.
    """
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # draw bounding box on the original image
        annotated = cv2.rectangle(original.copy(), (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Detected Region', annotated)
        cv2.waitKey(0)

        # crop the region and run OCR
        roi = original[y:y + h, x:x + w]
        ocr_config = '--oem 1 --psm 3 -l eng'
        detected_text = pytesseract.image_to_string(roi, config=ocr_config)

        if detected_text.strip():
            print(f"Detected text:\n{detected_text}\n{'-'*40}")


def main():
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        raise FileNotFoundError(f"Could not load image at '{IMAGE_PATH}'")

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold to isolate text regions
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Contours found: {len(contours)}")

    extract_text_from_regions(img, contours)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
