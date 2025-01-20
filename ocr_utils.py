import pytesseract
from PIL import Image

def contains_text(image, target_text: str, case_sensitive: bool = False) -> bool:
    """
    Performs OCR on the given PIL image and checks if target_text is in the recognized text.
    Returns True if found, False otherwise.
    """
    recognized_text = pytesseract.image_to_string(image)

    if not case_sensitive:
        recognized_text = recognized_text.lower()
        target_text = target_text.lower()

    return target_text in recognized_text

def extract_text(image) -> str:
    """
    Performs OCR on the given PIL image and returns the recognized text.
    """
    return pytesseract.image_to_string(image)
