# Text Recognition System

## Project Overview

This project implements a Text Recognition System using Computer Vision and Optical Character Recognition (OCR) techniques. The system detects potential text regions within an image using OpenCV image processing methods and extracts textual information from those regions using Tesseract OCR.

The project demonstrates how image preprocessing, contour detection, and OCR can be combined to automatically identify and recognize text from images.

## Features

- Image preprocessing using grayscale conversion
- Binary thresholding for text region isolation
- Contour detection to identify potential text areas
- Bounding box generation around detected text regions
- Text extraction using Tesseract OCR
- Region-wise text recognition and display

## Workflow

1. Load the input image.
2. Convert the image to grayscale.
3. Apply thresholding to highlight text regions.
4. Detect contours corresponding to text areas.
5. Draw bounding boxes around detected regions.
6. Extract each region of interest (ROI).
7. Perform OCR on each ROI using Tesseract.
8. Display and print the recognized text.

## Technologies Used

- Python
- OpenCV
- Tesseract OCR
- Pytesseract

## Project Structure

```text
Text_Recognition_System/
│
├── Text_Recognition_System.py
├── testimg.jpg
└── README.md
